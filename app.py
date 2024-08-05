from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import os
import string
import random

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:1234@localhost/school_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Configurações de e-mail para Mailtrap
app.config['MAIL_SERVER'] = 'sandbox.smtp.mailtrap.io'
app.config['MAIL_PORT'] = 587  # Ou 25, 465, ou 2525
app.config['MAIL_USERNAME'] = '3d37637170985f'
app.config['MAIL_PASSWORD'] = 'c23a15666abd6a'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_DEFAULT_SENDER'] = 'seu_email@exemplo.com'  # Substitua pelo seu e-mail de remetente

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(150), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    senha = db.Column(db.String(150), nullable=False)

    def set_password(self, senha):
        self.senha = generate_password_hash(senha)
    
    def check_password(self, senha):
        return check_password_hash(self.senha, senha)

@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        nome = request.form['nome']
        senha = request.form['senha']
        user = User.query.filter_by(nome=nome).first()
        if user and user.check_password(senha):
            session['user_id'] = user.id
            return redirect(url_for('dashboard'))
        else:
            flash('Nome ou senha incorretos')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('login'))

@app.route('/reset_password', methods=['GET', 'POST'])
def reset_password():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        new_password = request.form['new_password']
        user = User.query.filter_by(nome=nome, email=email).first()
        if user:
            # Atualiza a senha do usuário
            user.set_password(new_password)
            db.session.commit()
            flash('Senha alterada com sucesso. Você pode fazer login com a nova senha.')
            return redirect(url_for('login'))
        else:
            flash('Nome de usuário ou email não encontrados ou não correspondem')
    return render_template('reset_password.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        senha = request.form['senha']
        user = User(nome=nome, email=email)
        user.set_password(senha)
        db.session.add(user)
        db.session.commit()
        flash('Usuário criado com sucesso')
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/dashboard')
def dashboard():
    if 'user_id' in session:
        return f"Bem-vindo ao painel, usuário {session['user_id']}"
    return redirect(url_for('login'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
