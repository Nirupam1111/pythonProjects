import random
from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=True)
    location = db.Column(db.String(250), nullable=True)
    seats = db.Column(db.String(250), nullable=True)
    has_toilet = db.Column(db.Boolean, nullable=True)
    has_wifi = db.Column(db.Boolean, nullable=True)
    has_sockets = db.Column(db.Boolean, nullable=True)
    can_take_calls = db.Column(db.Boolean, nullable=True)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


@app.route("/")
def home():
    return render_template("index.html")
    

@app.route("/random")
def get_random_cafe():
    all_cafe=Cafe.query.all()
    random_cafe=random.choice(all_cafe)
    # print(random_cafe.name)
    # return jsonify(cafe={
    #     'id':random_cafe.id,
    #     'name':random_cafe.name,
    #     'map_url' :random_cafe.map_url,
    #     'img_url' :random_cafe.img_url,
    #     'location' :random_cafe.location,
    #     'seats' :random_cafe.seats,
    #     'has_toilet' :random_cafe.has_toilet,
    #     'has_wifi' :random_cafe.has_wifi,
    #     'has_sockets' :random_cafe.has_sockets,
    #     'can_take_calls' :random_cafe.can_take_calls,
    #     'coffee_price' :random_cafe.coffee_price
    # })
    return jsonify(cafe=random_cafe.to_dict())


@app.route("/all")
def all_cafes():
    all_cafe=Cafe.query.all()
    cafe_list=[]
    for cafe in all_cafe:
        cafes= cafe.to_dict()
        cafe_list.append(cafes)
    return jsonify(cafe=cafe_list)


@app.route("/search")
def search():
    path=request.args.get('loc')
    cafe = db.session.query(Cafe).filter_by(location=path).first()
    if cafe:
        return jsonify(cafe=cafe.to_dict())
    else:
        return jsonify(error={"Not Found": "Sorry, we don't have a cafe at that location."})


@app.route("/add", methods=["POST"])
def post_new_cafe():
    new_cafe = Cafe(
        name=request.form["name"],
        map_url=request.form["map_url"],
        img_url=request.form["img_url"],
        location=request.form["loc"],
        has_sockets=bool(request.form["sockets"]),
        has_toilet=bool(request.form["toilet"]),
        has_wifi=bool(request.form["wifi"]),
        can_take_calls=bool(request.form["calls"]),
        seats=request.form["seats"],
        coffee_price=request.form["coffee_price"],
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"success": "Successfully added the new cafe."})


@app.route("/update-price/<int:cafe_id>", methods=["PATCH"])
def patch_new_price(cafe_id):
    new_price = request.args.get("new_price")
    cafe = Cafe.query.filter_by(id=cafe_id).first()
    if cafe:
        cafe.coffee_price = new_price
        db.session.commit()
        return jsonify(response={"success": "Successfully updated the price."}), 200
    else:
        return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404


@app.route("/report-closed/<int:cafe_id>", methods=["DELETE"])
def delete_cafe(cafe_id):
    api_key = request.args.get("api-key")
    if api_key == "TopSecretAPIKey":
        cafe = db.session.query(Cafe).get(cafe_id)
        if cafe:
            db.session.delete(cafe)
            db.session.commit()
            return jsonify(response={"success": "Successfully deleted the cafe from the database."}), 200
        else:
            return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404
    else:
        return jsonify(error={"Forbidden": "Sorry, that's not allowed. Make sure you have the correct api_key."}), 403


if __name__ == '__main__':
    app.run(debug=True)
