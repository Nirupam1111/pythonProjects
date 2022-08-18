from flask import Flask

app = Flask(__name__)


def make_bold(function):
    def wrapper():
        x=function()
        return f'<b>{x}</b>'
    return wrapper


def make_emphasis(function):
    def wrapper():
        x=function()
        return f'<em>{x}</em>'
    return wrapper


def make_underline(function):
    def wrapper():
        x=function()
        return f'<u>{x}</u>'
    return wrapper


@app.route("/")
def hello_world():
    return "<h1 style='text-align:center'>Hello, World!</h1>"


@app.route("/bye")
@make_bold
@make_emphasis
@make_underline
def bye_bye():
    return "bye!!!"


@app.route("/username/<path:name>/<int:number>")
def greet(name,number):
    return f"Hello there {name} & you are {number} years old!!!"


# print(__name__)
if __name__ == '__main__':
    app.run(debug=True)
