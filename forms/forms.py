from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo




class FormLogin(FlaskForm):
    email_comercial = StringField('E-mail Comercial', validators=[DataRequired()])
    senha = PasswordField('Senha', validators=[DataRequired(), Length(8, 16)])
    continuar_conectado = BooleanField('Continuar conectado')
    btn_submit_login = SubmitField('Login')


class FormCadastro(FlaskForm):
    nome = StringField('Nome da Empresa', validators=[DataRequired()])
    cnpj = StringField('CNPJ',
                       validators=[DataRequired(), Length(14, 14)])  # Assumindo CNPJ como string com 14 caracteres
    representante = StringField('Representante', validators=[DataRequired()])
    email_comercial = StringField('E-mail Comercial', validators=[DataRequired()])
    senha = PasswordField('Senha', validators=[DataRequired(), Length(8, 16)])
    confirmacao_senha = PasswordField('Confirme sua senha', validators=[DataRequired(), EqualTo('senha')])
    btn_submit_criarConta = SubmitField('Criar conta')

    def criar_empresa(self):
        from objects.empresa import Empresa
        return Empresa(
            nome=self.nome.data,
            cnpj=self.cnpj.data,
            representante=self.representante.data,
            email_comercial=self.email_comercial.data,
            senha=self.senha.data
        )
