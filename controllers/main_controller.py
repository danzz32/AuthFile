import os

from flask import render_template, redirect, url_for, session, flash, request

from forms.forms import FormLogin, FormCadastro
from models.empresa_repository import EmpresaRepository
from models.documento_repository import DocumentoRepository, Documento
from models.item_repository import Item, ItemRepository
# from objects.document_processor import DocumentProcessor
from werkzeug.utils import secure_filename
# from utils.pdf_extractor import extract_table_from_pdf


# Configurações de upload
UPLOAD_FOLDER = 'files'
ALLOWED_EXTENSIONS = {'pdf', 'docx', 'doc'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def home():
    return redirect(url_for('main.login'))


def index():
    if 'user' in session:
        email = session['user']
        empresa_repo = EmpresaRepository()
        empresa = empresa_repo.get_by_email(email)
        
    return render_template('index.html',empresa=empresa)


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
            print(f"Usuário logado - {empresa.nome} | {empresa.email_comercial}")
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
                f"Usuário Cadastrado - {nova_empresa.nome} | {nova_empresa.email_comercial} | {nova_empresa.cnpj} | {nova_empresa.representante}")
            return redirect(url_for('main.index'))

    return render_template('login.html', form_login=form_login, form_cadastro=form_cadastro)


def logout():
    session.pop('user', None)
    print("Logout Efetuado")
    return redirect(url_for('main.login'))


def user_info():
    if 'user' in session:
        email = session['user']
        empresa_repo = EmpresaRepository()
        empresa = empresa_repo.get_by_email(email)

        if empresa:
            return render_template('user_info.html', empresa=empresa)
        else:
            flash('Usuário não encontrado', 'danger')
            return redirect(url_for('main.login'))
    else:
        flash('Você precisa estar logado para acessar essa página', 'danger')
        return redirect(url_for('main.login'))


# FAZER OS TESTES NO PC DO LAB
# def upload_document():
#     if 'licitacao' not in request.files:
#         flash('Nenhum arquivo enviado.', 'error')
#         return redirect(url_for('upload_page'))

#     file = request.files['licitacao']

#     if file.filename == '':
#         flash('Nenhum arquivo selecionado.', 'error')
#         return redirect(url_for('upload_page'))

#     if file:
#         # Defina o diretório para salvar o arquivo
#         upload_folder = 'files'  # Ajuste o caminho conforme necessário
#         os.makedirs(upload_folder, exist_ok=True)

#         filepath = os.path.join(upload_folder, file.filename)
#         print(f"Saving file to: {filepath}")

#         try:
#             file.save(filepath)
#         except Exception as e:
#             flash(f'Erro ao salvar o arquivo: {e}', 'error')
#             return redirect(url_for('upload_page'))

#         # Extraia a tabela e adicione os itens ao banco de dados
#         item_data_list = extract_table_from_pdf(filepath)
#         documento_id = request.form.get('documento_id')  # Obtenha o ID do documento, se necessário

#         item_repository = ItemRepository()
#         item_repository.add_items_from_data(item_data_list, documento_id)

#         flash('Documentos enviados e itens adicionados com sucesso!', 'success')
#         return redirect(url_for('results_page'))

#     flash('Erro ao processar o arquivo.', 'error')
#     return redirect(url_for('upload_document'))

# def results(documento_id):
#     item_repo = ItemRepository()
#     itens = item_repo.get_by_documento_id(documento_id)
#     return render_template('results.html', itens=itens)
    