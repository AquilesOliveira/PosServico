# RESTAPI

Modulo para Play 1.2.x que utiliza a biblioteca play-rest para implementar serviços REST de forma simples e organizada.

## Como Instalar

Instale o Play 1.2.x e crie um novo projeto como descrito no link: http://www.playframework.org/documentation/1.2.5/install

Adicione esta configuração em conf/dependencies.yml

    # Application dependencies
    require:
        - play
        - takenami -> restapi 0.1

    # My custom repositories
    repositories:
        - takenami:
            type:       http
            artifact:   "https://github.com/itakenami/restapi/raw/master/dist/[module]-[revision].zip"
            contains:
                - takenami -> *

Dentro da pasta do projeto rode o comando:

	play dependencies
	
Agora o módulo já foi instalado e está pronto para ser utilizado. Este módulo é compativel com Deploy na Cloud do Heroku.

## Testando

Para criar um exemplo, dentro da pasta do projeto, utilize o comando:

	restapi:sample
	
	
Após executar o comando acima, os seguintes arquivos serão criados:
* app/models/Usuario.java => Model exemplo
* app/controllers/Usuarios.java => Controlador com as abstrações contidas na LIB play-rest
* app/controllers/Wadl.java => Controller para gerar arquivo WADL do projeto
* conf/result_messages.properties => Mensagens de retorno

Além dos arquivos criados, uma configuração adicional será incluída nos seguintes arquivos:
* conf/application.conf => Adicionar a URL BASE para o WADL e o tipo de retorno: JSON ou XML
* conf/routes => Carrega as rotas contidas no módulo

Para testar utilize as URLs:
* http://localhost:9000/api/wadl => Arquivo WADL
* http://localhost:9000/api/clientes => Método GET que obter uma lista de Clientes