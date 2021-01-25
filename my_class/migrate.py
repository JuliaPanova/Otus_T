"""
Migration

run in shell;

python migrate.py db init
python migrate.py db migrate
python migrate.py db upgrade

"""
from flask import Flask
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from views.contact import contact_app, Teams
import config
from models import db

app = Flask(__name__)
app.config.update(
    SQLALCHEMY_DATABASE_URI=config.SQLALCHEMY_DATABASE_URI,
)
app.register_blueprint(contact_app, url_prefix="/contact")

db.init_app(app)
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)
manager.run()