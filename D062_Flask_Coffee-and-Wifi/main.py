from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField, SelectField
from wtforms.validators import DataRequired, URL
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
bootstrap = Bootstrap5(app)


class CafeForm(FlaskForm):
    cafe = StringField('Nome da Cafeteria', validators=[DataRequired()])
    location_url = URLField('Localização', validators=[DataRequired(), URL()])
    open_time = StringField('Horário de Abertura', validators=[DataRequired()])
    closing_time = StringField('Horário de Fechamento', validators=[DataRequired()])
    coffee_rating = SelectField('Nota do Café', validators=[DataRequired()],
                                choices=['❌', '☕', '☕☕', '☕☕☕', '☕☕☕☕', '☕☕☕☕☕'])
    food_rating = SelectField('Nota da Comida', validators=[DataRequired()],
                              choices=['❌', '🥐', '🥐🥐', '🥐🥐🥐', '🥐🥐🥐🥐', '🥐🥐🥐🥐🥐'])
    wifi_rating = SelectField('Nota do Wifi', validators=[DataRequired()],
                              choices=['❌', '🛜', '🛜🛜', '🛜🛜🛜', '🛜🛜🛜🛜', '🛜🛜🛜🛜🛜'])
    submit = SubmitField('Enviar')


@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=['POST', 'GET'])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        cafe = form.cafe.data
        location = form.location_url.data
        open_time = form.open_time.data
        close_time = form.closing_time.data
        coffee_rating = form.coffee_rating.data
        food_rating = form.food_rating.data
        wifi_rating = form.wifi_rating.data

        with open('cafe-data.csv', mode='a', encoding='utf-8') as csv_file:
            csv_file.write(f"\n{cafe},{location},{open_time},{close_time},{coffee_rating},{food_rating},{wifi_rating}")
        return redirect(url_for('cafes'))

    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
