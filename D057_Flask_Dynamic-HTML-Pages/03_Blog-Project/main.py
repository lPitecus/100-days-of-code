from flask import Flask, render_template
import requests

app = Flask(__name__)
blog_data = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()


@app.route('/')
def home():
    return render_template("index.html", posts=blog_data)


@app.route('/post/<int:postid>')
def post(postid):
    return render_template("post.html", post=blog_data[postid - 1])


if __name__ == "__main__":
    app.run(debug=True)
