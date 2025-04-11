# CRUD com Flask

Este é um projeto básico de CRUD (Create, Read, Update, Delete) desenvolvido com o framework Flask. Ele inclui funcionalidades de autenticação e gerenciamento de usuários, além de permitir adicionar, editar e excluir tarefas. Os dados são armazenados em um banco de dados SQLite.

---

## 🎯 Funcionalidades

- **Autenticação de Usuários**: Sistema de login e logout seguro.
- **Gerenciamento de Tarefas**:
  - Adicionar novas tarefas.
  - Editar tarefas existentes.
  - Excluir tarefas.
- **Banco de Dados**: Persistência de dados utilizando SQLite.
- **Interface Simples e Intuitiva**: Templates HTML estilizados com CSS.

---

## 📂 Estrutura do Projeto

A estrutura do projeto é organizada da seguinte forma:

```plaintext
crud-flask/
├── app.py                 # Lógica principal do aplicativo
├── requirements.txt       # Lista de bibliotecas e dependências
├── README.en.md           # Versão em inglês deste README
├── README.pt.md           # Versão em português deste README
├── templates/             # Templates HTML
│   ├── base.html          # Layout base da aplicação
│   ├── index.html         # Página principal com lista de tarefas
│   ├── edit.html          # Página para edição de tarefas
│   ├── login.html         # Página de login
├── static/                # Arquivos estáticos (CSS e JavaScript)
│   ├── css/
│   │   └── styles.css     # Estilos CSS da aplicação
│   ├── js/
│   │   └── scripts.js     # Scripts JavaScript da aplicação
```

---

## 🚀 Como Executar o Projeto

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
    - **Windows**:
        ```bash
        venv\Scripts\activate
        ```
    - **MacOS/Linux**:
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
    - No navegador, acesse: `http://127.0.0.1:5000/`.

---

## 📞 Contato

- **Autor**: Leonardo Mendes  
- **GitHub**: [oleonardomendes](https://github.com/oleonardomendes)
- **Linkedin**:Leonardo Mendes (https://www.linkedin.com/in/leonardo-mendes-418202181/)
