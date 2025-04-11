# CRUD com Flask (portuguese)

Este é um projeto básico de CRUD (Create, Read, Update, Delete) usando o framework Flask, com funcionalidades adicionais de autenticação e gerenciamento de usuários. A aplicação permite adicionar, editar e excluir tarefas, armazenando os dados em um banco de dados SQLite, e inclui um sistema de login para autenticação de usuários.

## Estrutura do Projeto

crud-flask/
├── app.py
├── requirements.txt
├── README.en.md
├── README.pt.md
├── templates/
│ ├── base.html
│ ├── index.html
│ ├── edit.html
│ ├── login.html
├── static/
│ ├── css/
│ │ └── styles.css
│ ├── js/
│ │ └── scripts.js

- **app.py**: Contém a lógica principal do aplicativo Flask, incluindo definição das rotas e gerenciamento de autenticação.
- **requirements.txt**: Lista as dependências do projeto.
- **templates/**: Contém os templates HTML para renderizar as páginas.
    - **base.html**: Layout base para a aplicação.
    - **index.html**: Página principal com a lista de tarefas.
    - **edit.html**: Página para editar tarefas.
    - **login.html**: Página de login para autenticação de usuários.
- **static/**: Contém arquivos estáticos como CSS e JavaScript.
    - **css/**: Contém arquivos de estilo.
        - **styles.css**: Arquivo de estilos CSS para a aplicação.
    - **js/**: Contém arquivos JavaScript.
        - **scripts.js**: Arquivo JavaScript para a aplicação.
- **README.md**: Este documento.

## Instalação

1. **Clone o repositório**:
    ```bash
    git clone https://github.com/oleonardomendes/crud-flask.git
    cd crud-flask
    ```

2. **Crie um ambiente virtual**:
    ```bash
    python -m venv venv
    ```

3. **Ative o ambiente virtual**:
    - No Windows:
        ```bash
        venv\Scripts\activate
        ```
    - No MacOS/Linux:
        ```bash
        source venv/bin/activate
        ```

4. **Instale as dependências**:
    ```bash
    pip install -r requirements.txt
    ```

5. **Execute a aplicação**:
    ```bash
    python app.py
    ```

6. **Acesse a aplicação**:
    - Abra um navegador e vá para `http://127.0.0.1:5000/`.

## Uso

### Login

1. **Na página de login**, insira seu nome de usuário (teste) e senha (password) e clique em "Login".
2. **Se as credenciais estiverem corretas**, você será redirecionado para a página principal.

### Logout

1. **Na página principal**, clique no botão "Logout" para sair da aplicação e voltar para a página de login.

### Adicionar uma Tarefa

1. **Na página principal**, digite uma tarefa no campo de texto e clique em "Add Task".
2. **A tarefa** será adicionada à lista de tarefas.

### Editar uma Tarefa

1. **Na lista de tarefas**, clique no botão "Edit" ao lado da tarefa que deseja editar.
2. **Na página de edição**, edite o texto da tarefa e clique em "Update Task".
3. **A tarefa** será atualizada na lista de tarefas.

### Deletar uma Tarefa

1. **Na lista de tarefas**, clique no botão "Delete" ao lado da tarefa que deseja deletar.
2. **A tarefa** será removida da lista de tarefas.
## Nota

Este projeto é para fins educacionais e demonstra um CRUD básico com autenticação.

