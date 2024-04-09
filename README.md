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
   Na nova janela de consulta SQL que se abre, cole o script SQL que você quer executar. No seu caso, seria o script para criar o banco de dados "usersmanager".

5. **Execute o Script:**
   Após colar o script, clique no botão "Execute" na barra de ferramentas superior ou pressione a combinação de teclas "Ctrl + Enter" para executar o script.

6. **Verifique o Resultado:**
   Após a execução do script, verifique a mensagem de confirmação na parte inferior da janela de consulta SQL. Se não houver erros, o banco de dados "usersmanager" deverá ter sido criado com sucesso.

7. **Verifique o Banco de Dados Criado:**
   No painel de navegação do lado esquerdo, atualize a visualização expandindo o nó "Databases". Você deverá ver o novo banco de dados "usersmanager" listado ali.

## Notas
- Certifique-se de ter as permissões adequadas para criar bancos de dados no servidor PostgreSQL ao qual está conectado.
