from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route('/')
def home():
    response = requests.get('https://api.npoint.io/c790b4d5cab58020d391')
    response.raise_for_status()
    data = response.json()
    return render_template("index.html", data=data)


@app.route('/<int:num>')
def post_html(num):
    response = requests.get('https://api.npoint.io/c790b4d5cab58020d391')
    response.raise_for_status()
    data = response.json()
    return render_template("post.html", data=data, number=num)


if __name__ == "__main__":
    app.run(debug=True)
