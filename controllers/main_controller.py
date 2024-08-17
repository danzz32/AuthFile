from flask import render_template, redirect, url_for, session, flash

from forms.forms import FormLogin, FormCadastro
from models.empresa_repository import EmpresaRepository
# from objects.ai import OcrProcessor, DocumentProcessor

# Inicialize o processador de OCR e o processador de documentos
# ocr = OcrProcessor(language='por')
# doc_processor = DocumentProcessor(
#     model_path='path/to/your/bert/model',
#     tokenizer_path='path/to/your/bert/tokenizer'
# )


def home():
    return redirect(url_for('main.login'))


def index():
    return render_template('index.html')


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
    session.pop('user', None)  # Atualize 'user_id' para 'user' para corresponder ao que está sendo usado no login
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

#####################################################################
# FAZER OS TESTES NO PC DO LAB
# def upload_document():
#     if 'user' not in session:
#         flash('Você precisa estar logado para acessar essa página', 'danger')
#         return redirect(url_for('main.login'))
#
#     if request.method == 'POST':
#         if 'file' not in request.files:
#             flash('Nenhum arquivo enviado', 'danger')
#             return redirect(url_for('main.index'))
#
#         file = request.files['file']
#         if file.filename == '':
#             flash('Nenhum arquivo selecionado', 'danger')
#             return redirect(url_for('main.index'))
#
#         if file:
#             file_path = os.path.join('uploads', file.filename)
#             file.save(file_path)
#
#             # Realiza OCR e extrai texto
#             extracted_text = ocr.process(file_path)
#
#             # Analisa o texto com o modelo BERT
#             analysis_results = doc_processor.analyze(extracted_text)
#
#             return render_template('results.html', results=analysis_results)
#
#     return render_template('index.html')
