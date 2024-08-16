from flask import Blueprint, render_template, redirect, url_for, session, flash

from forms.forms import FormLogin, FormCadastro
from models.empresa_repository import EmpresaRepository

main_bp = Blueprint('main', __name__)


@main_bp.route('/')
def home():
    return redirect(url_for('main.login'))


@main_bp.route('/index')
def index():
    return render_template('index.html')


@main_bp.route('/login', methods=['GET', 'POST'])
def login():
    form_login = FormLogin()
    form_cadastro = FormCadastro()

    if form_login.validate_on_submit():
        email = form_login.email_comercial.data
        senha = form_login.senha.data

        empresa_repo = EmpresaRepository()
        empresa = empresa_repo.get_by_email(email)

        if empresa and empresa.senha == senha:
            session['user'] = email
            print(f"Usuario logado - {empresa.nome} | {empresa.email_comercial}")
            return redirect(url_for('main.index'))
        else:
            flash('E-mail ou senha incorretos. Verifique suas credenciais e tente novamente.', 'danger')

    if form_cadastro.validate_on_submit():
        email = form_cadastro.email_comercial.data
        empresa_repo = EmpresaRepository()
        existing_empresa = empresa_repo.get_by_email(email)

        if existing_empresa:
            flash('E-mail já cadastrado', 'danger')
        else:
            nova_empresa = form_cadastro.criar_empresa()
            empresa_repo.add(nova_empresa)
            flash('Cadastro realizado com sucesso!', 'success')
            print(
                f"Usuario Cadastrado - {empresa.nome} | {empresa.email_comercial} | {empresa.cnpj} | {empresa.representante}")
            return redirect(url_for('main.index'))

    return render_template('login.html', form_login=form_login, form_cadastro=form_cadastro)


@main_bp.route('/logout')
def cadastro():
    session.pop('user_id', None)
    print(f"Logout Efetuado")
    return redirect(url_for('main.login'))
