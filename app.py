from asyncio import run_coroutine_threadsafe
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    fv = '/fv'
    mv8s = '/mv8s'
    whatsapp = '/whatsapp'
    return render_template('index.html', fv=fv, mv8s=mv8s, whatsapp=whatsapp)

@app.route('/curso-gratis')
def curso_gratis():
    url = "https://bit.ly/checkout47_RS"
    title = "curso-gratis"
    return render_template('iframe.html', url=url, title=title)

@app.route('/fv')
def formula_violao():
    title = "Fórmula Violão"
    url = "http://bit.ly/curso-recomendado-formula-violao"
    return render_template('redirect.html', url=url, title=title)

@app.route('/whatsapp')
def whatsapp():
    title = "WhatsApp"
    url = "https://web.whatsapp.com/"
    return render_template('redirect.html', url=url, title=title)


@app.route('/MetodoViolao8Semanas')
@app.route('/metodoviolao8semanas')
@app.route('/mv8s')
def metodoviolao8semanas():
    return render_template('mv8s.html')
    
@app.route('/MetodoViolao8Semanas/checkout')
def checkout():
    url = "https://bit.ly/checkV8S97"
    title = "Checkout: Metodo Violão 8 Semanas"
    return render_template('iframe.html', url=url, title=title)

if __name__ == "__main__":
    app.run(debug=True)