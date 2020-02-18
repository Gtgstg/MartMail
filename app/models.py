from app import db
class User(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(64),unique=True)
    email=db.Column(db.String(120),unique=True)
    price=db.Column(db.Integer)
    __tablename='customeruser'
    def __repr__(self):
        return '<User {}>'.format(self.username)
class Temp(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(64),unique=True)
    html=db.Column(db.String(1000),unique=True)
    __tablename='template'
    def __repr__(self):
        return '<User {}>'.format(self.name)
class Dynmic_Temp(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(64),unique=True)
    html=db.Column(db.String(1000),unique=True)
    __tablename='template'
    def __repr__(self):
        return '<User {}>'.format(self.name)