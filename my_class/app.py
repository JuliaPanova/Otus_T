from flask import Flask, request, render_template
from views.contact import contact_app, Teams
import re

app = Flask(__name__)
app.register_blueprint(contact_app, url_prefix="/contact")


def is_valid_phone_number(phone):
    phone = phone.replace(' ', '')
    return bool(re.match('^\+7([0-9]{3}|\([0-9]{3}\))[0-9]{3}[-]?[0-9]{2}[-]?[0-9]{2}$', phone))


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        time = int(request.form.get('time',0))

        team = Teams[time]
        name = request.form.get('name','')
        phone = request.form.get('phone', '')
        if name == '':
            error = 'Name should not be empty!'
            return render_template("contact.html", time=time, team=team, name=name, phone=phone, error=error)
        elif not is_valid_phone_number(phone):
            error = 'Not a valid phone number!'
            return render_template("contact.html", time=time, team=team, name=name, phone=phone, error=error)
        else:
            with open('database.csv', 'a', encoding='utf8') as f:
                f.write(';'.join([team,name,phone]) +  '\n')
            return render_template("thanks.html")
    else:
        return render_template("index.html")
