from sqlalchemy import create_engine
from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from models import Contact, db
# db_string = "postgres://otusdemo:notthatweak@localhost:5432/MyClass"
# connect_args={'options': '-csearch_path=myclass'}
#
# db = create_engine(db_string, connect_args=connect_args)

#base = declarative_base()



#base.metadata.create_all(db)

def create(date, name, phone, team_id):
    # Create
    new_contact = Contact(date=date, name=name, phone=phone, team_id=team_id)
    db.session.add(new_contact)
    db.session.commit()

def read_all(phone):
    #contacts = session.query(Contact)
    contacts = Contact.query.filter_by(phone=phone).order_by(Contact.name).all()
    return contacts


# Update
# doctor_strange.title = "Some2016Film"
# session.commit()
#
# # Delete
# session.delete(doctor_strange)
# session.commit()