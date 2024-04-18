# MVP - Minha API Rest

Este projeto faz parte da Disciplina 

**MVP**

O MVP desenvolvido busca atender todos os requisitos para resolução do desafio proposto por esta disciplina,  que consiste em desenvolver tanto o backend quanto o frontend do sistema, explorando novas possibilidades, seja criativo e inovador. 
O seu objetivo é a criação de um MVP (Minimum Viable Product) de um sistema web inovador que aborde um problema real, oferecendo uma solução criativa e inovadora para arquiteturas REST.

---
## Como executar a aplicação


# Primeiramente, Executar um Script SQL no pgAdmin para Criar um Banco de Dados

## Passos

1. **Abra o pgAdmin:**
   Inicie o pgAdmin e faça login com suas credenciais.

2. **Conecte-se ao Servidor PostgreSQL:**
   No painel do pgAdmin, expanda o nó "Servers" e clique com o botão direito do mouse no servidor ao qual você deseja se conectar. Selecione "Connect" no menu de contexto e insira suas credenciais, se solicitado.

3. **Abra uma Nova Janela de Consulta SQL:**
   No painel de navegação do lado esquerdo, expanda o nó do seu servidor PostgreSQL e o nó "Databases". Em seguida, clique com o botão direito do mouse no banco de dados onde deseja criar o novo banco de dados e escolha "Query Tool" no menu de contexto.

4. **Cole o Script SQL:**
   ''''
         -- Database: usersmanager

         -- DROP DATABASE IF EXISTS usersmanager;

         CREATE DATABASE usersmanager
            WITH
            OWNER = postgres
            ENCODING = 'UTF8'
            LC_COLLATE = 'Portuguese_Brazil.1252'
            LC_CTYPE = 'Portuguese_Brazil.1252'
            LOCALE_PROVIDER = 'libc'
            TABLESPACE = pg_default
            CONNECTION LIMIT = -1
            IS_TEMPLATE = False;
   ''''

   Na nova janela de consulta SQL que se abre, cole o script SQL acima. No caso, este seria o script para criar o banco de dados "usersmanager".

5. **Execute o Script:**
   clique no botão "Execute" na barra de ferramentas superior ou pressione a combinação de teclas "Ctrl + Enter" para executar o script.

6. **Verifique o Banco de Dados Criado:**
   No painel de navegação do lado esquerdo, atualize a visualização expandindo o nó "Databases". Você deverá ver o novo banco de dados "usersmanager" listado ali.

# Como executar API

## Passos

1. **Clonar o repositório no github :**

Após clonar o repositório, é necessário ir ao diretório raiz do projeto, pelo terminal, para poder executar os comandos descritos abaixo.

2. **Instalar todas dependências/bibliotecas necessárias :**

Será necessário ter todas as libs python listadas no `requirements.txt` instaladas, é bem simples o processo.
'''
$ pip install -r requirements.txt
```
Este comando instala as dependências/bibliotecas, descritas no arquivo `requirements.txt`.
'''
Para executar a API  basta executar no terninal:

$ python main.py

```
Este comando executa api
```

Abra o [http://localhost:5000]no navegador para verificar o status da API em execução.

# Para acessar documentação swagger

Para acessar a documentação no swagger basta executar:

Abra o [http://localhost:5000/apidocs/] no navegador para verificar a documentação da API com swagger.