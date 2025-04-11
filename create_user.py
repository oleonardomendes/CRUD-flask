from app import db, User
from werkzeug.security import generate_password_hash

# Configuração do Flask para o contexto do app
from app import app
with app.app_context():
    username = 'teste'
    password = 'password'

    # Gera o hash da senha
    hashed_password = generate_password_hash(password, method='pbkdf2:sha256')  # Atualize o método se necessário

    # Verifica se o usuário já existe
    if not User.query.filter_by(username=username).first():
        new_user = User(username=username, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        print(f'Usuário "{username}" criado com sucesso.')
    else:
        print(f'Usuário "{username}" já existe.')
