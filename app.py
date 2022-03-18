from flask import Flask, render_template

app = Flask(__name__)

@app.route('/MetodoViolao8Semanas')
def landingpage():
    return render_template('landingpage.html')
    
@app.route('/MetodoViolao8Semanas/checkout')
@app.route('/metodoviolao8semanas')
def checkout():
    return render_template('checkout.html')

if __name__ == "__main__":
    app.run(debug=True)