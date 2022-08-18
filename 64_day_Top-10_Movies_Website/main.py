from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import SubmitField, FloatField, StringField
from wtforms.validators import DataRequired
import requests


class MyForm(FlaskForm):
    rating = FloatField(label='Your rating out of 10 e.g, 7.5', validators=[DataRequired()])
    review = StringField(label='Your Review', validators=[DataRequired()])
    submit = SubmitField(label='Done')


class NewMovie(FlaskForm):
    new_movie_title = StringField(label='Movie Title', validators=[DataRequired()])
    submit = SubmitField(label='Add Movie')


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(500), nullable=True)
    rating = db.Column(db.Float, nullable=True)
    ranking = db.Column(db.Integer, nullable=True)
    review = db.Column(db.String(250), nullable=True)
    img_url = db.Column(db.String(250), nullable=False)


db.create_all()

# new_movie = Movie(
#     title="Phone Booth",
#     year=2002,
#     description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
#     rating=7.3,
#     ranking=10,
#     review="My favourite character was the caller.",
#     img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
# )
# db.session.add(new_movie)
# db.session.commit()


@app.route("/")
def home():
    all_movies = Movie.query.order_by(Movie.rating).all()
    for i in range(len(all_movies)):
        all_movies[i].ranking = len(all_movies) - i
    db.session.commit()
    return render_template("index.html", movies=all_movies)


@app.route('/edit', methods=['GET', 'POST'])
def edit():
    reset_form = MyForm()
    movie_id = request.args.get('id')
    movie = Movie.query.filter_by(id=movie_id).first()
    if reset_form.validate_on_submit():
        movie.rating=reset_form.rating.data
        movie.review=reset_form.review.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('edit.html', movie=movie, form=reset_form)


@app.route('/delete')
def delete():
    movie_id=request.args.get('id')
    movie_to_delete = Movie.query.get(movie_id)
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


@app.route('/add', methods=['GET', 'POST'])
def add():
    new_movie=NewMovie()

    if new_movie.validate_on_submit():
        reset_movie_title=new_movie.new_movie_title.data
        url = "https://imdb8.p.rapidapi.com/title/find"
        querystring = {"q": f"{reset_movie_title}"}
        headers = {
            'x-rapidapi-host': "imdb8.p.rapidapi.com",
            'x-rapidapi-key': "8fc305d284msh5737e545bba35f7p119d03jsn7ae2f4a9fcba"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)
        details = response.json()
        year = details['results'][0]['year']
        image_url = details['results'][0]['image']['url']

        movie = Movie(
            title=reset_movie_title,
            year=year,
            description="",
            rating=0,
            ranking=0,
            review="",
            img_url=image_url
        )
        db.session.add(movie)
        db.session.commit()
        return redirect(url_for('edit', id=movie.id))
    return render_template('add.html', new_movie=new_movie)


if __name__ == '__main__':
    app.run(debug=True)
