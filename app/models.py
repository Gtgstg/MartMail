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
    __tablename='dynamic_template'
    def __repr__(self):
        return '<User {}>'.format(self.name)
class Order(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    purchaseDate=db.Column(db.DateTime)
    totalPrice=db.Column(db.Integer)
    __tablename='order'
    def __repr__(self):
        return '<Order on {}>'.format(self.purchaseDate)
class Reviews(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    userProductid=db.Column(db.Integer)
    productRating=db.Column(db.Integer)
    reviewTitle = db.Column(db.String(100))
    reviewDetails=db.Column(db.String(1000))
    __tablename='reviews'
    def __repr__(self):
        return '<Reviews on {}>'.format(self.userProductid)
class UserProductList(db.Model):
    Id=db.Column(db.Integer,primary_key=True)
    userId=db.Column(db.Integer)
    productId=db.Column(db.Integer)
    quantity = db.Column(db.Integer)
    orderId=db.Column(db.Integer)
    __tablename='userprod'
    def __repr__(self):
        return '<UserProductList on {}>'.format(self.userid)
class Product(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    SKU=db.Column(db.String(20))
    productName=db.Column(db.String(20))
    brand = db.Column(db.String(100))
    productDescription=db.Column(db.String(1000))
    color = db.Column(db.String(20))
    unitPrice = db.Column(db.Integer)
    __tablename='product'
    def __repr__(self):
        return '<Product on {}>'.format(self.productName)
class Customers(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    first_name=db.Column(db.String(100))
    last_name=db.Column(db.String(100))
    gender = db.Column(db.String(100))
    email=db.Column(db.String(100))
    age = db.Column(db.Integer)
    address = db.Column(db.String(1000))
    state = db.Column(db.String(100))
    zipcode = db.Column(db.Integer)
    phoneNumber = db.Column(db.String(20))
    registrationDate = db.Column(db.DateTime)
    __tablename='customers'
    def __repr__(self):
        return '<customers on {}>'.format(self.first_name)