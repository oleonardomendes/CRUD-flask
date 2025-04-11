from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
import logging
from logging.handlers import RotatingFileHandler
from flask_migrate import Migrate

# Criação e configuração da aplicação Flask
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
app.config['SECRET_KEY'] = 'Admin1234'

# Inicialização da extensão SQLAlchemy para interagir com o banco de dados
db = SQLAlchemy(app)

# Configuração do gerenciador de login
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# Configuração da migração do banco de dados
migrate = Migrate(app, db)

# Definição do modelo User para a tabela de usuários
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    tasks = db.relationship('Task', back_populates='user', lazy=True)

    # Método para verificar a senha do usuário
    def check_password(self, password):
        return check_password_hash(self.password, password)

# Definição do modelo Task para a tabela de tarefas
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', back_populates='tasks')

# Formulário WTForm para adicionar tarefas
class TaskForm(FlaskForm):
    content = StringField('Content', validators=[DataRequired(), Length(max=200)])
    submit = SubmitField('Add Task')

# Formulário WTForm para login
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=150)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6, max=150)])

# Formulário WTForm para registro de usuário
class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])

# Carregamento do usuário pelo ID para a sessão de login
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Rota para login de usuário
@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            app.logger.info(f"User found: {user.username}")
            if user.check_password(form.password.data):
                app.logger.info("Password is correct")
                login_user(user)
                return redirect(url_for('index'))
            else:
                app.logger.info("Password is incorrect")
        else:
            app.logger.info("User not found")
        flash('Invalid username or password')

    return render_template('login.html', form=form)

# Rota para registro de novo usuário
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data, method='sha256')
        new_user = User(username=form.username.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        flash('User registered successfully')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

# Rota para logout do usuário
@app.route('/logout', methods=['POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

# Rota principal que lista as tarefas do usuário logado
@app.route('/')
@login_required
def index():
    app.logger.info('Index page accessed')
    page = request.args.get('page', 1, type=int)
    tasks = Task.query.filter_by(user_id=current_user.id).paginate(page=page, per_page=5)
    form = TaskForm()
    return render_template('index.html', tasks=tasks.items, form=form, pagination=tasks)

# Rota para adicionar uma nova tarefa
@app.route('/add', methods=['POST'])
@login_required
def add_task():
    form = TaskForm()
    if form.validate_on_submit():
        task_content = form.content.data
        new_task = Task(content=task_content, user_id=current_user.id)
        db.session.add(new_task)
        db.session.commit()
        return redirect(url_for('index'))
    else:
        flash('Task content is required!')
    return redirect(url_for('index'))

# Rota para editar uma tarefa existente
@app.route('/edit/<int:id>')
@login_required
def edit_task(id):
    task = Task.query.get_or_404(id)
    if task.user_id != current_user.id:
        flash('You are not authorized to edit this task')
        return redirect(url_for('index'))
    form = TaskForm(obj=task)
    return render_template('edit.html', task=task, form=form)

# Rota para atualizar uma tarefa existente
@app.route('/update/<int:id>', methods=['POST'])
@login_required
def update_task(id):
    task = Task.query.get_or_404(id)
    if task.user_id != current_user.id:
        flash('You are not authorized to edit this task')
        return redirect(url_for('index'))
    form = TaskForm()
    if form.validate_on_submit():
        task.content = form.content.data
        db.session.commit()
        return redirect(url_for('index'))
    else:
        flash('Task content is required!')
    return redirect(url_for('edit_task', id=id))

# Rota para deletar uma tarefa
@app.route('/delete/<int:id>')
@login_required
def delete_task(id):
    task = Task.query.get_or_404(id)
    if task.user_id != current_user.id:
        flash('You are not authorized to delete this task')
        return redirect(url_for('index'))
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for('index'))

# Configuração do logging e inicialização do banco de dados ao iniciar a aplicação
if __name__ == '__main__':
    if not app.debug:
        handler = RotatingFileHandler('app.log', maxBytes=10000, backupCount=1)
        handler.setLevel(logging.INFO)
        app.logger.addHandler(handler)
    with app.app_context():
        db.create_all()
    app.run(debug=True)
