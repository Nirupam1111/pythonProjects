from flask import Flask, render_template
from flask import request
import requests
import smtplib

my_email='nirupamsur10@gmail.com'
password='zxcvbnm@1'

posts = requests.get('https://api.npoint.io/3ac64b4e1d4591fea40a').json()

app = Flask(__name__)


@app.route("/")
def page():
    return render_template("index.html", posts=posts)


@app.route("/home")
def home():
    return render_template("index.html", posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=['GET','POST'])
def contact():
    if request.method == 'POST':
        name=request.form['name']
        email=request.form['email']
        phone=request.form['phone']
        message=request.form['message']

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email,password=password)
            connection.sendmail(from_addr=my_email,to_addrs='nirupamsur9@gmail.com',msg=f'Subject:Form Data\n\nname:{name}\n email:{email}\n phone:{phone}\n message:{message}')
        return render_template("contact.html",pos='1')
    return render_template("contact.html",pos='0')


@app.route("/post/<int:index>")
def post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", posts=requested_post)
    # return render_template("post.html", posts=posts[index-1])


if __name__ == "__main__":
    app.run(debug=True)
