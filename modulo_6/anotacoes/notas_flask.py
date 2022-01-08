from flask import Flask, request


app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1>hello world</h1>'

@app.route('/novarota')
def nova_rota():
    return '<h2>nova rota</h2>'

@app.route('/novarota2/<int:valor>')
def nova_rota2(valor):
    return f'<p>o valor é {valor}</p>'

@app.route('/api', methods = ['GET', 'POST'])
def api():
    if request.method == 'POST':
        return request.get_json()
    else:
        return 'requisição get'