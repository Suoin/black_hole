import os

SECRET_KEY = os.urandom(24)  # Генерируется случайно, или укажи свой
SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Flask-Mail настройки (замени на реальные, например, Mailtrap или Gmail)
MAIL_SERVER = 'your.smpt.server'  # Или 'smtp.gmail.com'
MAIL_PORT = 2525  # Или 587 для Gmail
MAIL_USERNAME = 'your@email' # вводим емайл для отправки сообщений
MAIL_PASSWORD = 'yourpassword'# Вводим специальный пароль для работы с почтой
MAIL_USE_TLS = True
MAIL_USE_SSL = False
MAIL_DEFAULT_SENDER = 'your@emal' #здесь указываем ваш емайл для тела письма