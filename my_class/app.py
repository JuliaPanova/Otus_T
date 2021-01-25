from flask import Flask, request, render_template
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
import re
from views.contact import contact_app, Teams
import config
import db_client
from models import db

app = Flask(__name__)
app.config.update(
    SQLALCHEMY_DATABASE_URI=config.SQLALCHEMY_DATABASE_URI,
)
app.register_blueprint(contact_app, url_prefix="/contact")

db.init_app(app)

def is_valid_phone_number(phone):
    phone = phone.replace(' ', '')
    return bool(re.match('^\+7([0-9]{3}|\([0-9]{3}\))[0-9]{3}[-]?[0-9]{2}[-]?[0-9]{2}$', phone))


@app.route("/list", methods=["POST"])
def list_items():
    phone = clean_phone(request.form['phone'])
    contacts = db_client.read_all(phone)
    return render_template("contacts.html", teams=Teams, contacts=contacts)




@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        team_id = int(request.form.get('time',0))

        team = Teams[team_id]
        date = request.form.get('date', '')
        name = request.form.get('name','')
        phone = request.form.get('phone', '')
        if name == '':
            error = 'Name should not be empty!'
            return render_template("contact.html", time=team_id, team=team, name=name, phone=phone, error=error)
        elif date == '':
            error = 'Date should not be empty!'
            return render_template("contact.html", time=team_id, team=team, name=name, phone=phone, error=error)
        elif not is_valid_phone_number(phone):
            error = 'Not a valid phone number!'
            return render_template("contact.html", time=team_id, team=team, name=name, phone=phone, error=error)
        else:
            # with open('database.csv', 'a', encoding='utf8') as f:
            #     f.write(';'.join([team,name,phone]) +  '\n')

            phone_cleaned = clean_phone(phone)
            db_client.create(date=date, name=name, phone=phone_cleaned, team_id=team_id)
            return render_template("thanks.html")
    else:
        return render_template("index.html")


def clean_phone(phone):
    phone_cleaned = phone.replace('+', '').replace('(', '').replace(')', '').replace('-', '')
    return phone_cleaned
