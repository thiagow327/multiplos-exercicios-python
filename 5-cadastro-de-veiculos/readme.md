**Gerenciamento de Veículos**
Este projeto é uma aplicação web para gerenciamento de veículos. Ele permite consultar, filtrar, cadastrar, atualizar e excluir informações de veículos.

**Requisitos**
Para executar este projeto, você precisará ter instalado em sua máquina a biblioteca Flask, Flask-Cors, Pytest e a extensão "Live Server" do VS Code.

**Executando a Aplicação**
Clone este repositório em sua máquina local:
git clone https://github.com/thiagow327/Tinnova.git

Instale as dependências do projeto:
1. pip install Flask
2. pip install -U flask-cors
3. pip install pytest
4. instale a extensão "Live Server" em seu VS Code
5. Execute o arquivo "app.py" para iniciar o servidor, iniciará em **http://localhost:8080/veiculos** : python app.py
6. Acesse o arquivo "index.html" com a extenção "Live Server".

**Funcionalidades**
Consultar Veículos
Permite consultar todos os veículos cadastrados.

Filtrar Veículos
Permite filtrar os veículos com base em critérios como marca, ano e cor.

Consultar Detalhes do Veículo
Permite consultar os detalhes de um veículo específico com base no seu ID.

Cadastrar Veículo
Permite cadastrar um novo veículo informando os seguintes campos: veículo, marca, ano, cor e descrição.

Atualizar Veículo
Permite atualizar os dados de um veículo existente informando o ID, como marca, veículo, ano, cor e descrição.

Atualizar Campo 'Vendido'
Permite atualizar o status 'Vendido' de um veículo informando o ID e o novo valor (True or False).

Excluir Veículo
Permite excluir um veículo cadastrado informando o seu ID.

**Testes unitários**

1. Acesse o diretório "/backend"
2. Execute o comando: python test\_<funcionalidade>.py

Códigos de saída após execução de arquivos de teste unitário:
0: Todos os testes foram executados com sucesso e passaram sem erros.
1: Pelo menos um teste falhou durante a execução.
2: Erros ocorreram durante a execução dos testes, como erros de importação ou falha ao chamar uma função de teste.
3: Alguma exceção ocorreu durante a execução do Pytest, como um erro de configuração ou uma interrupção do usuário.
4: O Pytest foi chamado com argumentos de linha de comando incorretos ou inválidos.
