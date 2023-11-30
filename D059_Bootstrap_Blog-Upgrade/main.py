from flask import Flask, render_template
import requests

blog_posts = requests.get("https://api.npoint.io/eb6cd8a5d783f501ee7d").json()

app = Flask(__name__)


@app.route("/")
def homepage():
    return render_template("index.html", posts=blog_posts)


@app.route("/about")
def about_page():
    return render_template("about.html")


@app.route("/contact")
def contact_page():
    return render_template("contact.html")


@app.route("/post/<int:post_id>")
def post_page(post_id):
    return render_template("post.html", post=blog_posts[post_id-1])


if __name__ == '__main__':
    app.run(debug=True)

