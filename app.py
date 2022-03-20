from asyncio import run_coroutine_threadsafe
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    fv = '/fv'
    mv8s = '/mv8s'
    sdz = '/sdz'
    whatsapp = 'https://api.whatsapp.com/send?phone=5514997648079'
    return render_template('index.html', fv=fv, mv8s=mv8s, whatsapp=whatsapp, sdz=sdz)

@app.route('/sdz')
def cursodeviolaosdz():
    title = "Curso de Violão - Sai do Zero"
    url = "https://bit.ly/saidozeroviolão"
    return render_template('redirect.html', url=url, title=title)

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
    url = "https://go.hotmart.com/Y48914272N?ap=cede"
    title = "Metodo Violão 8 Semanas"
    return render_template('redirect.html', url=url, title=title)


if __name__ == "__main__":
    app.run(debug=True)