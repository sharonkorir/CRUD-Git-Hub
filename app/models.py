'''Basic User model without a one to many relationship'''
from . import db


# class User(db.Model):
#     __tablename__ = 'users'
#     id = db.Column(db.Integer, primary_key = True)
#     username = db.Column(db.String(255),unique = True,nullable = False)
#     email  = db.Column(db.String(255),unique = True,nullable = False)
#     secure_password = db.Column(db.String(255),nullable = False)
#     bio = db.Column(db.String(255))
    

class Repository:
    '''
    Repo class from repo request via github API
    '''

    def __init__(self, html_url, owner, description, language, other_languages):
        self.html_url = html_url
        self.owner = owner
        self.description = description
        self.language = language
        self.other_languages = other_languages
