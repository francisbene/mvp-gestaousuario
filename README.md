# Minha API

Este pequeno projeto faz parte do material diático da Disciplina **Desenvolvimento Full Stack Básico** 

O objetivo aqui é ilutsrar o conteúdo apresentado na primeira aula com um código simples.

---

# Como Executar um Script SQL no pgAdmin para Criar um Banco de Dados

Este guia fornece instruções passo a passo sobre como executar um script SQL no pgAdmin para criar um banco de dados no PostgreSQL.

## Passos

1. **Abra o pgAdmin:**
   Inicie o pgAdmin e faça login com suas credenciais.

2. **Conecte-se ao Servidor PostgreSQL:**
   No painel do pgAdmin, expanda o nó "Servers" e clique com o botão direito do mouse no servidor ao qual você deseja se conectar. Selecione "Connect" no menu de contexto e insira suas credenciais, se solicitado.

3. **Abra uma Nova Janela de Consulta SQL:**
   No painel de navegação do lado esquerdo, expanda o nó do seu servidor PostgreSQL e o nó "Databases". Em seguida, clique com o botão direito do mouse no banco de dados onde deseja criar o novo banco de dados e escolha "Query Tool" no menu de contexto.

4. **Cole o Script SQL:**

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

   Na nova janela de consulta SQL que se abre, cole o script SQL acima. No caso, este seria o script para criar o banco de dados "usersmanager".

5. **Execute o Script:**
   Após colar o script, clique no botão "Execute" na barra de ferramentas superior ou pressione a combinação de teclas "Ctrl + Enter" para executar o script.

6. **Verifique o Resultado:**
   Após a execução do script, verifique a mensagem de confirmação na parte inferior da janela de consulta SQL. Se não houver erros, o banco de dados "usersmanager" deverá ter sido criado com sucesso.

7. **Verifique o Banco de Dados Criado:**
   No painel de navegação do lado esquerdo, atualize a visualização expandindo o nó "Databases". Você deverá ver o novo banco de dados "usersmanager" listado ali.

## Notas
- Certifique-se de ter as permissões adequadas para criar bancos de dados no servidor PostgreSQL ao qual está conectado.

## Como executar

Será necessário ter todas as libs python listadas no `requirements.txt` instaladas, é bem simples o processo.

Após clonar o repositório, é necessário ir ao diretório raiz do projeto, pelo terminal, para poder executar os comandos descritos abaixo.

> É fortemente indicado o uso de ambientes virtuais do tipo [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html).

```
(env)$ pip install -r requirements.txt
```

Este comando instala as dependências/bibliotecas, descritas no arquivo `requirements.txt`.

Para executar a API  basta executar:

```
(env)$ flask run --host 0.0.0.0 --port 5000
```

Em modo de desenvolvimento é recomendado executar utilizando o parâmetro reload, que reiniciará o servidor
automaticamente após uma mudança no código fonte. 

```
(env)$ flask run --host 0.0.0.0 --port 5000 --reload
```

Abra o [http://localhost:5000/#/](http://localhost:5000/#/) no navegador para verificar o status da API em execução.
