# Configuracao da Aplicacao

# Escolha uma porta para rodar a aplicacao e atribua esse valor a variavel PORT
PORT = 8080

# Escolha um diretorio padrao para os arquivos, esse diretorio deve ser criado manualmente antes
# de ser escolhido para a aplicacao
DEFAULT_DIR = "Files/"

# Escolha uma URL padrao para o erro, mas certifique-se de alterar o nome do arquivo referente
# a pagina (404.html) junto com a alteracao da variavel ERROR_URL
ERROR_URL = '404.html'

# Adicione ou remova nome de arquivos dentro do FILE_LIST, mas certifique-se de colocar o arquivo
# correspondente dentro da pasta DEFAULT_DIR, caso contrario sera exibido um erro 404
FILE_LIST = ['home.html', 'background.jpeg', 'computer.gif', 'arquivo.js', 'rabisco.png']

# Sugerimos realizar testes com arquivos inexistentes, sem extensao, sem nome, com extensoes invalidas 
# ou diretorios invalidos para verificar o funcionamento da pagina de Erro 404.
# 
# Exemplos de nomes invalidos para testes:
# - home
# - .html
# - exemplo.txt (Tendo em vista que .txt nao eh aceito pela aplicacao)
# - home.html arquivo.js
# 
# Alem disso, sugerismos realizar testes em relacao a request sem especificar o arquivo desejado.
# Para isso, eh necessario mudar alguns valores na lista para observar o comportamento da aplicacao
# 
# Exemplo de lista para teste:
#  - FILE_LIST = ['home', '.jpeg', '', 'arquivo.js', 'rabisco.png']
# Nesse caso, ao rodar http://localhost:PORT/ no navegador, o correto eh visualizar o arquivo "arquivo.js",
# uma vez que todos os arquivos anteriores sao invalidos.
#
# Exemplo de teste de diretorio:
# - DEFAULT_DIR = Files2 (Files2 sendo uma pagina inexistente)
# Nesse caso, todos os arquivos solicitados serao invalidos, ja que a pasta eh inexistente
