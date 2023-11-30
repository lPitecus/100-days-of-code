from flask import Flask

app = Flask(__name__)


def make_bold(function):
    def wrapper():
        return f'<b>{function()}</b>'

    return wrapper


def make_italic(function):
    def wrapper():
        return f'<i>{function()}</i>'

    return wrapper


@app.route("/")
def hello_world():
    return ('<h1 style="text-align: center; color: blue">Hello world</h1>'
            '<p>oi mano tudo certo</p>'
            '<ol>'
            '   <li>salve mano</li>'
            '   <li>segundamente eu quero q vc se foda</li>'
            '   <li>terceiramente olhe esse cachorrinho aqui 👇</li>'
            '</ol>'
            '<img src="https://media.giphy.com/media/P2hdI6VaKlFhxncQG9/giphy.gif">'
            '<p>se quiser ir para uma pagina especial <a href="http://127.0.0.1:5000/bye">clique aqui</a></p>')


@app.route("/bye")
def name_page():
    return ('<h1 style="text-align: center">bye.</h1>'
            '<img style="display: block; margin-left: auto; margin-right: auto; width: 50%;"'
            ' src="https://media.giphy.com/media/26u4b45b8KlgAB7iM/giphy.gif">')


if __name__ == "__main__":
    app.run(debug=True)
