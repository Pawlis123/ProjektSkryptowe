from app import db


class User(db.Document):
    username = db.StringField(required=True, unique=True)
    password = db.StringField(required=True)
    rss_url_list = db.ListField()