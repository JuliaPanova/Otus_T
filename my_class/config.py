import os

PG_HOST = os.environ.get("PG_HOST", "localhost")

#SQLALCHEMY_DATABASE_URI = f"postgres+psycopg2://user:password@{PG_HOST}:5432/shop"
SQLALCHEMY_DATABASE_URI = f"postgres+psycopg2://otusdemo:notthatweak@{PG_HOST}:5432/MyClass"

CONNECT_ARGS ={'options': '-csearch_path=myclass'}


# db_string = "postgres://otusdemo:notthatweak@localhost:5432/MyClass"
# connect_args={'options': '-csearch_path=myclass'}