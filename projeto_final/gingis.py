from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    variavel = request.args.get('url')
    return render_template('index.html', variavel=variavel)