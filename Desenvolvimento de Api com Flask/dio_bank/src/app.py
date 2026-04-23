from flask import Flask, url_for, request

app = Flask(__name__)

@app.route("/olamundo/<usuario>/<int:idade>/<float:altura>")
def hello_world(usuario, idade, altura):
    print(idade)
    print(f'Tipo da Variavel Idade: {type(idade)}')
    print(f'Tipo da Variavel Usuario: {type(usuario)}')
    print(f'Tipo da Variavel Altura: {type(altura)}')
    return f"<p>Ola Mundo! : {usuario}</p>"

@app.route("/bemvindo")
def bem_vindo():
    return "<p>Seja Bem Vindo!</p>"

@app.route("/projects/")
def projects():
    return "The project page"

@app.route("/about", methods=["POST", "GET"])
def about():
    if request.method == "GET":
        return "This is method GET"
    else:
        return "This is method POST"

with app.test_request_context():
    url = "/about"
    print(url_for('bem_vindo'))
    print(url_for('projects'))
    print(url_for('about', next='/'))
    print(url_for('hello_world', usuario='John Doe', idade=29, altura=1.79 ))