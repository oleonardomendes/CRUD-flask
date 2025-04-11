# CRUD with Flask

This is a basic CRUD (Create, Read, Update, Delete) project using the Flask framework, with additional functionalities for authentication and user management. The application allows you to add, edit, and delete tasks, storing data in an SQLite database, and includes a login system for user authentication.

## Project Structure

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

- **app.py**: Contains the main logic of the Flask application, including route definitions and authentication management.
- **requirements.txt**: Lists the project dependencies.
- **templates/**: Contains the HTML templates for rendering the pages.
    - **base.html**: Base layout for the application.
    - **index.html**: Main page with the task list.
    - **edit.html**: Page for editing tasks.
    - **login.html**: Login page for user authentication.
- **static/**: Contains static files such as CSS and JavaScript.
    - **css/**: Contains style files.
        - **styles.css**: CSS style file for the application.
    - **js/**: Contains JavaScript files.
        - **scripts.js**: JavaScript file for the application.
- **README.md**: This document.

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/oleonardomendes/crud-flask.git
    cd crud-flask
    ```

2. **Create a virtual environment**:
    ```bash
    python -m venv venv
    ```

3. **Activate the virtual environment**:
    - On Windows:
        ```bash
        venv\Scripts\activate
        ```
    - On MacOS/Linux:
        ```bash
        source venv/bin/activate
        ```

4. **Install the dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

5. **Run the application**:
    ```bash
    python app.py
    ```

6. **Access the application**:
    - Open a browser and go to `http://127.0.0.1:5000/`.

## Usage

### Login

1. **On the login page**, enter your username (test) and password (password) and click "Login".
2. **If the credentials are correct**, you will be redirected to the main page.

### Logout

1. **On the main page**, click the "Logout" button to exit the application and return to the login page.

### Add a Task

1. **On the main page**, type a task in the text field and click "Add Task".
2. **The task** will be added to the task list.

### Edit a Task

1. **In the task list**, click the "Edit" button next to the task you want to edit.
2. **On the edit page**, modify the task text and click "Update Task".
3. **The task** will be updated in the task list.

### Delete a Task

1. **In the task list**, click the "Delete" button next to the task you want to delete.
2. **The task** will be removed from the task list.

## Note

This project is for educational purposes and demonstrates a basic CRUD with authentication.