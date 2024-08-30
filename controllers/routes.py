from flask import Blueprint
from controllers.main_controller import home, index, login, logout, user_info , upload_document, results

main_bp = Blueprint('main', __name__)

main_bp.route('/')(home)
main_bp.route('/index')(index)
main_bp.route('/login', methods=['GET', 'POST'])(login)
main_bp.route('/logout')(logout)
main_bp.route('/user_info')(user_info)
main_bp.route('/upload', methods=['GET','POST'])(upload_document)
main_bp.route('/results')(results)
