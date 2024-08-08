from flask import Blueprint, render_template, redirect, url_for, session

from forms.forms import FormLogin, FormCadastro

main_bp = Blueprint('main', __name__)


@main_bp.route('/')
def home():
    if 'user' in session:
        return redirect(url_for('main.index'))
    return redirect(url_for('main.login'))


@main_bp.route('/index')
def index():
    return render_template('index.html')


@main_bp.route('/login', methods=['GET', 'POST'])
def login():
    form_login = FormLogin()
    form_cadastro = FormCadastro()
    if form_login.validate_on_submit():
        session['user'] = form_login.email.data
        return redirect(url_for('main.index'))
    return render_template('login.html', form_login=form_login, form_cadastro=form_cadastro)


@main_bp.route('/cadastro', methods=['POST'])
def cadastro():
    form_cadastro = FormCadastro()
    if form_cadastro.validate_on_submit():
        # Implementar lógica de cadastro aqui
        return redirect(url_for('main.login'))
    return render_template('login.html', form_cadastro=form_cadastro)
