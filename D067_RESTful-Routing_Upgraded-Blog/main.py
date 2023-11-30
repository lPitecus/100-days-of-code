import datetime

from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField

TODAY = datetime.datetime.now().strftime("%B %d, %Y")

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
ckeditor = CKEditor(app)
Bootstrap5(app)

# CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy()
db.init_app(app)


# CONFIGURE TABLE
class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)


class NewPostForm(FlaskForm):
    title = StringField('Blog Post Title', validators=[DataRequired()])
    subtitle = StringField('Subtitle', validators=[DataRequired()])
    author = StringField('Your Name', validators=[DataRequired()])
    img_url = StringField('Blog Image URL', validators=[DataRequired()])
    body = CKEditorField('Blog Content', validators=[DataRequired()])
    submit = SubmitField('Submit Post')


# with app.app_context():
#     db.create_all()


@app.route('/')
def get_all_posts():
    posts = db.session.execute(db.select(BlogPost)).scalars().fetchall()
    return render_template("index.html", all_posts=posts)


@app.route('/post/<post_id>')
def show_post(post_id):
    requested_post = db.session.execute(db.select(BlogPost).where(BlogPost.id == post_id)).scalar()
    return render_template("post.html", post=requested_post)


@app.route("/new-post", methods=["POST", "GET"])
def add_new_post():
    form = NewPostForm()
    if form.validate_on_submit():
        new_post = BlogPost(
            title=form.title.data,
            subtitle=form.subtitle.data,
            date=TODAY,
            body=form.body.data,
            author=form.author.data,
            img_url=form.img_url.data
        )
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for('get_all_posts'))

    return render_template('make-post.html', form=form)


@app.route("/edit-post/<post_id>", methods=["POST", "GET"])
def edit_post(post_id):
    selected_post = db.session.execute(db.select(BlogPost).where(BlogPost.id == post_id)).scalar()
    form = NewPostForm(
        title=selected_post.title,
        subtitle=selected_post.subtitle,
        author=selected_post.author,
        img_url=selected_post.img_url,
        body=selected_post.body
    )
    if form.validate_on_submit():
        selected_post.title = form.title.data
        selected_post.subtitle = form.subtitle.data
        selected_post.author = form.author.data
        selected_post.img_url = form.img_url.data
        selected_post.body = form.body.data
        db.session.commit()
        return redirect(url_for('show_post', post_id=post_id))

    return render_template('make-post.html', editing_mode=True, form=form)


# TODO: delete_post() to remove a blog post from the database
@app.route("/delete/<post_id>")
def delete_post(post_id):
    post_to_delete = db.session.execute(db.select(BlogPost).where(BlogPost.id == post_id)).scalar()
    db.session.delete(post_to_delete)
    db.session.commit()
    return redirect(url_for('get_all_posts'))


# Below is the code from previous lessons. No changes needed.
@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, port=5003)
