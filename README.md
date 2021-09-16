# PrimeiroTrabalhoWeb

## Alunos:
  - Carlos Ribeiro da Rocha - 1720372
  - Leonardo Santos Abreu - 1720565

## Para instalar o servidor

## Requisitos:
  - Python 3.X.X instalado

É possível rodar o servidor por linha de comando, para isso é necessário estar na pasta do arquivo server.py e utilizar o comando "python3 server.py".

## implementações

  - Implementamos o método GET, obtendo todas as formas de arquivo pedidas, proibindo outras extensões, dessa forma, por meio de requests conseguimos acesso aos arquivos armazenados dentro de DEFAULT_DIR, no arquivo de configuracoes. Alem disso, optamos por colocar um Menu na pagina HTML para facilitar interacoes com os arquivos padroes. O mesmo nao funcionara para novos arquivos inseridos na lista e, caso algum arquivo presente no menu HTML seja deletado da lista, o retorno sera 404 NOT FOUND.
  - Caso nenhum nome de arquivo seja especificado no endereço, ele percorre FILE_LIST e utiliza o primeiro arquivo válido, para isso ele precisa possuir uma das extensões suportadas. Caso o servidor não encontre nenhum arquivo válido para o envio, a página de erro 404 será enviada.
  - Mensagens de erro são enviadas caso as variáveis dos arquivos de configuração estejam configuradas de forma errada.
  - O servidor aceita mais de uma conexão ao mesmo tempo, fizemos um teste retirando o pid implementado e adicionando sleep, foi possível perceber que a conexão não funcionava em mais de um cliente.
  - A página 404 também é enviada quando o arquivo não é achado, seja por não estar no diretório, ou por não existir.