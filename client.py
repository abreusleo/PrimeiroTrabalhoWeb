from sys import argv, stderr
from socket import AF_INET, getaddrinfo, socket
from socket import AF_INET, SOCK_STREAM, IPPROTO_TCP, AI_ADDRCONFIG
from os import abort

def getEnderecoServidor(host, porta):
    try:
        enderecoServidor = getaddrinfo( host,
                                        porta,
                                        family = AF_INET,
                                        type = SOCK_STREAM,
                                        proto = IPPROTO_TCP,
                                        flags = AI_ADDRCONFIG)
    except:
        print("Deu ruim")
        abort()
    return enderecoServidor

def criaSocket(enderecoServidor):
    fd = socket(enderecoServidor[0][0], enderecoServidor[0][1])
    if not fd:
        print("Não consegui criar o socket")
        abort()
    
    return fd

def fazOResto(fd):
    while True:
        bufferSaida = input("Escreva um texto: ")
        if len(bufferSaida) == 0:
            break

        fd.send(bytearray(bufferSaida, 'utf-8'))
        bufferEntrada = fd.recv(1024)
        print("==>", bufferEntrada)
    return

def conecta(socketfd, enderecoServidor):
    try:
        socketfd.connect(enderecoServidor[0][4])
    except:
        print("Erro", enderecoServidor[0][4], file = stderr)
        abort()
    return

def main():
    if len(argv) == 3:
        host = argv[1]
        porta = int(argv[2])
    else:
        host = 'localhost'
        porta = 8080
    enderecoServidor = getEnderecoServidor(host, porta)
    socketfd = criaSocket(enderecoServidor)
    conecta(socketfd, enderecoServidor)
    fazOResto(socketfd)
    socketfd.close()

    return

if __name__ == '__main__':
    main()