import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hibasd078a8vbqfkjnxz'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///authfile.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
