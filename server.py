from sys import argv, stderr 
from socket import getaddrinfo, socket 
from socket import AF_INET, SOCK_STREAM, AI_ADDRCONFIG, AI_PASSIVE 
from socket import IPPROTO_TCP, SOL_SOCKET, SO_REUSEADDR 
from os import abort, environ, fork
from time import sleep
from os import path
import settings as settings

# Metodo apresentado em aula
def get_host_adress(porta): 
    try: 
        enderecoHost = getaddrinfo( 
            'localhost',
            porta,              
            family=AF_INET,              
            type=SOCK_STREAM,              
            proto=IPPROTO_TCP,
            flags=AI_ADDRCONFIG | AI_PASSIVE) 
    except:         
        print("Não obtive informações sobre o servidor (???)", file=stderr) 
        abort()
    return enderecoHost

# Metodo apresentado em aula
def create_socket(enderecoServidor):
    fd = socket(enderecoServidor[0][0], enderecoServidor[0][1])
    if not fd: 
        print("Não consegui criar o socket", file=stderr) 
        abort()
    return fd

# Metodo apresentado em aula
def set_mode(fd): 
    fd.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1) 
    return

# Metodo apresentado em aula
def bind_socket(fd, porta): 
    try: 
        fd.bind(('localhost', porta)) 
    except: 
        print("Erro ao dar bind no socket do servidor", porta, file=stderr) 
        abort()     
    return

# Metodo apresentado em aula
def listen(fd): 
    try: 
        fd.listen(0)
    except: 
        print("Erro ao começar a escutar a porta", file=stderr) 
        abort()     
    print("Iniciando o serviço"); 
    return

# Metodo apresentado em aula
def connect(fd): 
    (con, cliente) = fd.accept() 
    print("Servidor conectado com", cliente) 
    return con

def not_found(con):
    try:    # Verifica a existencia do arquivo informado dentro de settings.ERROR_URL
        file = open("{}".format(settings.ERROR_URL), "rb") # Abre o arquivo File/404.html para enviar em caso de erro
    except:
        print("Arquivo de erro nao encontrado")
        abort() 
    con.send(b"HTTP/1.1 404 NOT FOUND\n")   # Entrega o codigo HTML 404, que significa que a socilitacao nao foi encontrada
    con.send(f"Content-Type: text/html\n\n".encode())   # Formata o Content-Type correspondente a pagina 404.
    fileContent = file.read()   # Le o conteudo da pagina 404.  
    con.send(fileContent)       # Envia o arquivo lido anteriormente
    file.close()                # Fecha o arquivo, ja que nao precisaremos mais usa-lo
    return

def file_type_hanlder(type):
    if type == "html" or type == "js":    # Caso o arquivo seja HTML ou JS, enviamos o Content-type Text
        return "text"
    return "image"  # Caso seja qualquer outra alternativa, enviamos Image, ja que todos os outros tipos aceitos atualmente correspondiam a esse tipo

def send_file(con, fileInfo, fileType, fileExtension):
    try:    # Caso o arquivo nao seja encontrado dentro do diretorio, fazemos o uso da funcao not_found() para retornar o codigo 404.
        file = open("{}{}".format(settings.DEFAULT_DIR, fileInfo), "rb")    # Abre o arquivo correspondente ao diretorio padrao seguido do arquivo, exemplo: "Files/home.html"

        con.send(b"HTTP/1.1 200 OK\n")  # Entrega o codigo HTML 200, que significa que tudo ocorreu de maneira correta em bytes
        con.send(("Content-Type: {}/{}\n\n".format(fileType, fileExtension)).encode())  # Informa o Content-Type formado por fileType/fileExtension em bytes

        fileContent = file.read()   # Le o conteudo do arquivo solicitado
        con.send(fileContent)       # Envia o arquivo solicitado
        file.close()                # Fecha o arquivo, ja que nao precisaremos mais usa-lo
    except:
        not_found(con)

    return
    
def checkExtension(extension):
    acceptedExtensions = ["html", "js", "jpeg", "png", "gif"]       # Lista de extensoes aceitas pelo site
    if extension in acceptedExtensions:
        return True     # Caso seja uma extensao valida, da o retorno positivo

    return False        # Invalida a extensao, caso ela nao seja aceita

def checkRestritions(fileInfo):
    if fileInfo in settings.FILE_LIST:      # Verifica se o arquivo solicitado esta dentro da lista configurada
        splitFileInfo = fileInfo.split(".") # Separa o nome do arquivo de sua extensao

        if len(splitFileInfo) > 1 and not fileInfo.startswith("."): # Verifica se o arquivo possui nome + extensao e previne o usuario de solitar apenas uma extensao
            fileExtension = splitFileInfo[1]                        # como no exemplo '.exemplo'
            fileType = file_type_hanlder(fileExtension)             # Verifica se o Type e "Image" ou "Text"

            if checkExtension(fileExtension):                       # Verifica se a extensao do arquivo solicitado eh aceita pelo programa
                return True, fileExtension, fileType                # Valida todas as restricoes

    return False, None, None    # Informa que as informacoes dadas estao invalidas

def request_handler(con):
    buffer = con.recv(1024).decode("utf-8")
    
    if buffer.startswith("GET"):    # Checa se a request feita foi do tipo GET

        buffer = buffer.split(" ")  # Divide o Buffer de forma a ficar um pouco mais facil de ser compreendido
        fileDirectory = buffer[1]   # Pega o diretorio escolhido pelo o usuario, exemplo : localhost/exemplo -> fileDirectory = /exemplo

        if fileDirectory == "/":    # Verifica se a request foi feita sem diretorio especifico
            if settings.FILE_LIST:  # Checa se exista a lista de arquivos na configuracao
                for i in settings.FILE_LIST:    # Como o usuario nao especificou um arquivo, percorremos a lista na configuracao buscando algum arquivo valido
                    fileInfo = i                # caso nao seja possivel, direcionamos o usuario para a pagina 404.
                    passedRestritions, fileExtension, fileType  = checkRestritions(fileInfo)
                    if passedRestritions:       # Se todas as condicoes forem satisfeitas, enviamos o arquivo para o client.
                        send_file(con, fileInfo, fileType, fileExtension)
                        break
                if not passedRestritions:       # Caso ocorra algum erro, direcionamos o usuario para a pagina 404.
                    not_found(con)
            else:
                not_found(con)                  # Caso ocorra algum erro, direcionamos o usuario para a pagina 404.
        else:
            fileInfo = fileDirectory[1:]        # Ignora a "/" presente no fileDirectory e pega as informacoes relevantes do arquivo
            passedRestritions, fileExtension, fileType  = checkRestritions(fileInfo)
            if passedRestritions:               # Se todas as condicoes forem satisfeitas, enviamos o arquivo para o client. 
                send_file(con, fileInfo, fileType, fileExtension)
            else:
                not_found(con)                  # Caso ocorra algum erro, direcionamos o usuario para a pagina 404.
    return

def checkSettingsFile():    # Verifica se os dados foram inseridos no arquivo de configuracao, caso contrario Aborta a aplicacao
    if settings.PORT == "" or type(settings.PORT) != int:
        print("Por favor, insira uma Porta valida")
        abort()
    if settings.DEFAULT_DIR == "" or not settings.DEFAULT_DIR.endswith("/"):
        print("Por favor, insira um diretorio valido")
        abort()
    elif not path.exists(settings.DEFAULT_DIR):
        print("Por favor, insira um diretorio valido")
        abort()
    if settings.ERROR_URL == "" or not settings.ERROR_URL.endswith(".html"):
        print("Por favor, insira uma URL de erro valida")
        abort()
    if not settings.FILE_LIST:
        print("Por favor, insira arquivos na lista padrao")
        abort()
    return

def main():
    checkSettingsFile()
    porta = settings.PORT
    enderecoHost = get_host_adress(porta)     
    fd = create_socket(enderecoHost)     
    set_mode(fd) 
    bind_socket(fd, porta) 
    print("Servidor pronto em", enderecoHost) 
    listen(fd)

    while True:         
        con = connect(fd)
        pid = fork()    # Utilizamos o pid para permitir conexoes simultaneas a aplicacao
        if pid == 0:
            request_handler(con)
            #sleep(10)  # Fizemos o uso do sleep sem os pids para ter certeza de que eles estavam funcionando da maneira correta, chegamos ao resultado esperado
            con.close()
        else:
            con.close()
    return

main()