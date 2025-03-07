from flask import current_app as app

@app.route('/')
def home():
    return 'Olá, bem-vindo ao System Assistant!'