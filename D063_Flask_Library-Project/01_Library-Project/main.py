from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, String, Float
from sqlalchemy.orm import Mapped, mapped_column

db = SQLAlchemy()
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///books-colection.db"
db.init_app(app)


# Criação da tabela e definição dos cabeçalhos(colunas da primeira linha)
class Books(db.Model):
    # Coluna "id" em que os elementos tem como propriedades ser um int e ser uma primary_key
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    # Coluna "title" em que os elementos são uma string, com limite de 250 caracteres,
    # tem que ser unico, e nao podem estar vazios.
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    # Coluna "author" em que os elementos são uma string com limite de 250 caracteres
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    # Coluna "rating" em que os elementos são um float e não podem estar vazios
    rating: Mapped[float] = mapped_column(Float, nullable=False)


@app.route('/')
def home():
    # comando que entra na database e transforma as linhas em objetos (<Books 1>), onde as propriedades são as colunas.
    all_books = db.session.execute(db.select(Books)).scalars().fetchall()
    return render_template('index.html', books=all_books)


@app.route("/add", methods=['POST', 'GET'])
def add():
    if request.method == 'POST':
        name = request.form['name']
        author = request.form['author']
        rating = request.form['rating']
        # cria um objeto de linha do database
        book = Books(title=name, author=author, rating=rating)
        # adiciona o objeto a database
        db.session.add(book)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('add.html')


@app.route("/edit", methods=["POST", "GET"])
def edit():
    # Extrai da url o valor da chave id. Ex.: https://localhost:5000/edit?id=1
    # a url será montada com esse par de valores devido ao comando url_for('edit', id=book.id) na
    # linha 14 do arquivo index.html, que adicionou um payload na url.
    current_id = request.args.get('id')
    selected_book = db.session.execute(db.select(Books).where(Books.id == int(current_id))).scalar()
    if request.method == 'POST':
        # muda a propriedade "rating" do objeto (linha) selecionado.
        selected_book.rating = request.form['change']
        db.session.commit()
        return redirect(url_for('home'))

    return render_template('edit.html', book=selected_book)


@app.route("/delete")
def delete():
    current_id = request.args.get('id')
    selected_book = db.session.execute(db.select(Books).where(Books.id == int(current_id))).scalar()
    db.session.delete(selected_book)
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)
