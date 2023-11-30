from flask import Flask, render_template, request
from flask_mail import Mail, Message
import requests
import os


blog_posts = requests.get("https://api.npoint.io/eb6cd8a5d783f501ee7d").json()

app = Flask(__name__)


@app.route("/")
def homepage():
    return render_template("index.html", posts=blog_posts)


@app.route("/about")
def about_page():
    return render_template("about.html")


app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('EMAIL')
app.config['MAIL_PASSWORD'] = os.environ.get('PASSWORD')
app.config['MAIL_DEFAULT_SENDER'] = os.environ.get('EMAIL')
app.config['MAIL_MAX_EMAILS'] = 50
mail = Mail(app)
@app.route("/contact", methods=["POST", "GET"])
def contact_page():
    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        message = request.form['message']
        print(name)
        print(email)
        print(phone)
        print(message)
        recipient_list = ["tuzaum.silva@gmail.com"]
        with mail.connect() as connection:
            for recipient in recipient_list:
                msg = Message(subject=f"Contact from {name}", recipients=[recipient])
                msg.body = f"Name: {name}\nEmail: {email}\nPhone Number: {phone}\nMessage: {message}"
                connection.send(msg)
        return render_template("contact.html", form_submitted=True)
    if request.method == "GET":
        return render_template("contact.html")


@app.route("/post/<int:post_id>")
def post_page(post_id):
    return render_template("post.html", post=blog_posts[post_id-1])


if __name__ == '__main__':
    app.run(debug=True)

