import sqlalchemy.orm.exc
from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
import random as ran

'''
Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)

# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy()
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        """Pega a linha escolhida e transforma em um dicionário do tipo 'título_da_coluna': 'conteúdo da coluna'"""

        # # Method 1.
        # dictionary = {}
        # # Loop through each column in the data record
        # for column in self.__table__.columns:
        #     # Create a new dictionary entry;
        #     # where the key is the name of the column
        #     # and the value is the value of the column
        #     dictionary[column.name] = getattr(self, column.name)
        # return dictionary

        # Method 2. Alternatively use Dictionary Comprehension to do the same thing.
        # Como ja vamos ter pego so uma linha (cafe aleatório) essa compreensão funciona
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


# with app.app_context():
#     db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/random")
def random():
    cafes_list = db.session.execute(db.select(Cafe)).scalars().fetchall()
    index = ran.randint(0, len(cafes_list)-1)
    random_cafe = cafes_list[index]
    return jsonify(cafe=random_cafe.to_dict())


@app.route("/all")
def all():
    cafes_list = db.session.execute(db.select(Cafe)).scalars().fetchall()
    dict_list = [cafe.to_dict() for cafe in cafes_list]
    return jsonify(cafe=dict_list)


@app.route("/search")
def search():
    search_location = request.args.get('loc')
    match = db.session.execute(db.select(Cafe).where(Cafe.location == search_location)).scalars().fetchall()
    dict_list = [cafe.to_dict() for cafe in match]
    if len(dict_list) <1:
        return jsonify(error={"Not Found": "Sorry, we don't have a cafe in this location"})
    else:
        return jsonify(cafe=dict_list)


@app.route("/add", methods=["POST"])
def add():
    new_cafe = Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("location"),
        seats=request.form.get("seats"),
        has_toilet=bool(request.form.get("has_toilet")),
        has_wifi=bool(request.form.get("has_wifi")),
        has_sockets=bool(request.form.get("has_sockets")),
        can_take_calls=bool(request.form.get("can_take_calls")),
        coffee_price=request.form.get("coffee_price")
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"success": "Successfully added the new cafe."})


@app.route("/update-price/<cafe_id>", methods=["PATCH"])
def update_price(cafe_id):
    new_price = request.args.get('new_price')
    try:
        selected_cafe = db.session.execute(db.select(Cafe).where(Cafe.id == int(cafe_id))).scalar()
        selected_cafe.coffee_price = new_price
        db.session.commit()
        return jsonify(success="Successfully updated the price.")
    except AttributeError:
        return jsonify(error={"Not found": f"There's no cafe with id={cafe_id} in the database"}), 404


@app.route("/report-closed/<cafe_id>", methods=["DELETE"])
def delete_cafe(cafe_id):
    api_key = "123456789"
    api_given = request.args.get('api-key')
    if api_given == api_key:
        try:
            selected_cafe = db.session.execute(db.select(Cafe).where(Cafe.id == int(cafe_id))).scalar()
            db.session.delete(selected_cafe)
            db.session.commit()
            return jsonify(success="Successfully removed the cafe.")
        except sqlalchemy.orm.exc.UnmappedInstanceError:
            return jsonify(error={"Not found": f"There's no cafe with id={cafe_id} in the database"}), 404
    else:
        return jsonify(error={"Access denied": "You do not have permission to delete. Make sure you have the correct "
                                               "api-key."}), 403


# HTTP GET - Read Record

# HTTP POST - Create Record

# HTTP PUT/PATCH - Update Record

# HTTP DELETE - Delete Record


if __name__ == '__main__':
    app.run(debug=True)
