from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, String, Float
from sqlalchemy.orm import Mapped, mapped_column
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired
from api import search_movie_by_name, search_movie_by_id


db = SQLAlchemy()
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movie-collection.db'
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
bootstrap = Bootstrap5(app)
db.init_app(app)


class EditForm(FlaskForm):
    rating = FloatField('Your rating of 10', validators=[DataRequired()])
    review = StringField('Your review', validators=[DataRequired()])
    submit = SubmitField('Done')


class AddForm(FlaskForm):
    movie_to_search = StringField('Movie Title', validators=[DataRequired()])
    submit = SubmitField('Add Movie')


class Movies(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[str] = mapped_column(String, nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)
    ranking: Mapped[str] = mapped_column(String, nullable=False)
    review: Mapped[str] = mapped_column(String, nullable=False)
    img_url: Mapped[str] = mapped_column(String, nullable=False)


@app.route("/")
def home():
    all_movies = db.session.execute(db.select(Movies).order_by(Movies.rating)).scalars().fetchall()
    i = len(all_movies)
    for movie in all_movies:
        movie.ranking = str(i)
        i -= 1
    db.session.commit()
    return render_template('index.html', movies=all_movies)


@app.route("/edit", methods=["POST", "GET"])
def edit_page():
    form = EditForm()
    current_id = request.args.get('id')
    selected_movie = db.session.execute(db.select(Movies).where(Movies.id == int(current_id))).scalar()
    if form.validate_on_submit():
        selected_movie.rating = form.rating.data
        selected_movie.review = form.review.data
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("edit.html", form=form)


@app.route("/add", methods=["POST", "GET"])
def add_page():
    form = AddForm()
    if form.validate_on_submit():
        movie_list = search_movie_by_name(form.movie_to_search.data)
        return render_template("select.html", movies=movie_list)
    return render_template("add.html", form=form)


@app.route("/find")
def find_movie():
    movie_info = search_movie_by_id(request.args.get('id'))
    new_movie = Movies(title=movie_info['title'], year=movie_info['year'], description=movie_info['description'], img_url=movie_info['img_url'], rating=8.8, ranking=5, review="kkkkk")
    db.session.add(new_movie)
    db.session.commit()
    return redirect(url_for('edit_page', id=new_movie.id))


@app.route("/delete")
def delete_page():
    current_id = request.args.get('id')
    selected_movie = db.session.execute(db.select(Movies).where(Movies.id == int(current_id))).scalar()
    db.session.delete(selected_movie)
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
