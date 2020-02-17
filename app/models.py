from app import db
class User(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(64),unique=True)
    email=db.Column(db.String(120),unique=True)
    __tablename='CustomerUser'
    def __repr__(self):
        return '<User {}>'.format(self.username)