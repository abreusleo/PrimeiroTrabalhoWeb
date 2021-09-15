# PrimeiroTrabalhoWeb

## Alunos:
  - Carlos Ribeiro da Rocha - 1720372
  - Leonardo Santos Abreu - 1720565

## Para instalar o servidor

## Requisitos:
  - Python 3.X.X instalado

É possível rodar o servidor por linha de comando, para isso é necessário estar na pasta do arquivo server.py e utilizar o comando "python3 server.py".

## implementações

  - Implementamos o método GET, obtendo todas as formas de arquivo pedidas, proibindo outras extensões, dessa forma, por meio de um menu conseguimos acesso tanto às imagens quanto a página HTML e o código JS.
  - Caso nenhum nome de arquivo seja especificado no endereço, ele percorre a lista FILE_LIST e utiliza o primeiro nome de arquivo válido, portanto precisa possuir as extensões suportadas, caso não encontre nenhum arquivo válido, a página de erro 404 será enviada.
  - Mensagens de erro são enviadas caso as variáveis dos arquivos de configuração estejam configuradas erradas.
  - O server aceita mais de uma conexão ao mesmo tempo, fizemos um teste retirando o pid implementado e adicionando sleep, foi possível perceber que a conexão não funcionava.
  - A página 404 também é enviada quando o arquivo não é achado, seja por não estar no diretório, ou por não existir.