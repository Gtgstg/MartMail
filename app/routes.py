from datetime import date, datetime

from flask_mail import Message
from flask import request,jsonify
from app import app, db, mail
from app.models import User,Temp,Dynmic_Temp,Order,Reviews,UserProductList,Product,Customers
import csv

@app.route('/hello-world')
def hello_world():
    return 'Hello-world'
@app.route('/user/<username>/<email>',methods=['POST','GET','DELETE','PUT'])
def user(username,email):
    if request.method=='GET':
        user=User.query.filter_by(username=username,email=email)
        user=user.first()
        return 'email is {}'.format(user.email)
    if request.method=='PUT':
        user=User.query.filter_by(username=username).first()
        user.email=email
        db.session.commit()
        return 'updated email id is '+ email
    if request.method=='POST':
        user=User(username=username,email=email)
        db.session.add(user)
        db.session.commit()
        return 'Created new user with email {}'.format(username)
    if request.method=='DELETE':
        User.query.filter_by(username=username,email=email).delete()
        db.session.commit()
        return 'success deletion with username {}'.format(username)

@app.route('/users',methods=['POST','GET','DELETE','PUT'])
def users():
    username = request.json.get('username')
    email = request.json.get('email')
    if request.method=='GET':
        # user = User.query.filter_by(username=username, email=email)
        # user = user.first()
        # return 'email is {}'.format(user.email)
        cols = ['id', 'username', 'email']
        data = User.query.all()
        result = [{col: getattr(d, col) for col in cols} for d in data]
        return jsonify(result=result)
    if request.method=='PUT':
        user=User.query.filter_by(username=username).first()
        user.email=email
        db.session.commit()
        return 'updated email id is '+ email
    if request.method=='POST':
        user=User(username=username,email=email)
        db.session.add(user)
        db.session.commit()
        return 'Created new user with email {}'.format(username)
    if request.method=='DELETE':
        User.query.filter_by(username=username,email=email).delete()
        db.session.commit()
        return 'success deletion with username {}'.format(username)

@app.route('/template',methods=['POST','GET','DELETE','PUT'])
def template():
    name=request.args.get('name')
    html=request.args.get('html')
    if request.method=='GET':
        user = Temp.query.filter_by(name=name)
        user = user.first()
        return user.html
        # cols = ['id', 'name', 'html']
        # data = Temp.query.all()
        # result = [{col: getattr(d, col) for col in cols} for d in data]
        # return jsonify(result=result)
    if request.method=='PUT':
        user=Temp.query.filter_by(name=name).first()
        user.html=html
        db.session.commit()
        return 'updated template is '+ html
    if request.method=='POST':
        user=Temp(name=name,html=html)
        db.session.add(user)
        db.session.commit()
        return 'Created new template with  {}'.format(name)
    if request.method=='DELETE':
        Temp.query.filter_by(name=name,html=html).delete()
        db.session.commit()
        return 'success deletion with name {}'.format(name)

@app.route('/dynamic-template',methods=['POST','GET','DELETE','PUT'])
def dynamic_template():
    name=request.args.get('name')
    html=request.args.get('html')
    if request.method=='GET':
        user = Dynmic_Temp.query.filter_by(name=name)
        user = user.first()
        return user.html
        # cols = ['id', 'name', 'html']
        # data = Temp.query.all()
        # result = [{col: getattr(d, col) for col in cols} for d in data]
        # return jsonify(result=result)
    if request.method=='PUT':
        user=Dynmic_Temp.query.filter_by(name=name).first()
        user.html=html
        db.session.commit()
        return 'updated template is '+ html
    if request.method=='POST':
        user=Dynmic_Temp(name=name,html=html)
        db.session.add(user)
        db.session.commit()
        return 'Created new template with {}'.format(name)
    if request.method=='DELETE':
        Dynmic_Temp.query.filter_by(name=name,html=html).delete()
        db.session.commit()
        return 'success deletion with name {}'.format(name)

@app.route("/email",methods=['POST'])
def email():
    name=request.args.get('name')
    recip=[]
    user =User.query.all()
    for i in user:
        recip.append(i.email)
    temp=Temp.query.filter_by(name=name).first()
    msg=Message('Hello',sender='yourId@gmail.com',recipients=recip,html=temp.html)
    mail.send(msg)
    return "Sent"

@app.route("/email-dynamic",methods=['POST'])
def email_dynamic():
    name=request.args.get('name')
    couponCode=request.args.get('couponCode')
    user =User.query.all()
    for i in user:
        temp=Dynmic_Temp.query.filter_by(name=name).first()
        print(temp)
        msg=Message('Hello',sender='yourId@gmail.com',recipients=list(i.email),html=temp.html.format(i.username,i.price,couponCode))
        mail.send(msg)
    return "Sent"

@app.route("/order",methods=['GET'])
def order():
    result=[]
    with open('Order.csv') as csvDataFile:
        csvReader = csv.reader(csvDataFile)
        n = len(next(csvReader))
        csvDataFile.seek(0)
        for i in range(0, n):
            result.append([])
        for row in csvReader:
            for x in range(0, n):
                result[x].append(row[x])
    for i in range(1,len(result[0])):
        a,b,c=result[1][i].split('/')
        user = Order(id=int(result[0][i]), purchaseDate=date(int(c),int(b),int(a)),totalPrice=int(result[2][i]))
        db.session.add(user)
    db.session.commit()
    return "Transefer to db"

@app.route("/reviews",methods=['GET'])
def reviews():
    result=[]
    with open('Reviews.csv') as csvDataFile:
        csvReader = csv.reader(csvDataFile)
        n = len(next(csvReader))
        csvDataFile.seek(0)
        for i in range(0, n):
            result.append([])
        for row in csvReader:
            for x in range(0, n):
                result[x].append(row[x])
    for i in range(1,len(result[0])):
        user = Reviews(id=int(result[0][i]), userProductid=int(result[1][i]),productRating=int(result[2][i]),reviewTitle=int(result[3][i]),reviewDetails=int(result[4][i]))
        db.session.add(user)
    db.session.commit()
    return "Transefer to db"

@app.route("/userprod",methods=['GET'])
def userprod():
    result=[]
    with open('UserProductList.csv') as csvDataFile:
        csvReader = csv.reader(csvDataFile)
        n = len(next(csvReader))
        csvDataFile.seek(0)
        for i in range(0, n):
            result.append([])
        for row in csvReader:
            for x in range(0, n):
                result[x].append(row[x])
    for i in range(1,len(result[0])):
        user = UserProductList(Id=int(result[0][i]), userId=int(result[1][i]),productId=int(result[2][i]),quantity=int(result[3][i]),orderId=int(result[4][i]))
        db.session.add(user)
    db.session.commit()
    return "Transefer to db"

@app.route("/product",methods=['GET'])
def product():
    result=[]
    with open('Product.csv') as csvDataFile:
        csvReader = csv.reader(csvDataFile)
        n = len(next(csvReader))
        csvDataFile.seek(0)
        for i in range(0, n):
            result.append([])
        for row in csvReader:
            for x in range(0, n):
                result[x].append(row[x])
    for i in range(1,len(result[0])):
        user = Product(id=int(result[0][i]), SKU=result[1][i],productName=result[2][i],brand=result[3][i],productDescription=result[4][i],color=result[5][i],unitPrice=int(result[6][i]))
        db.session.add(user)
    db.session.commit()
    return "Transefer to db"

@app.route("/customers",methods=['GET'])
def customers():
    result=[]
    with open('Customers.csv') as csvDataFile:
        csvReader = csv.reader(csvDataFile)
        n = len(next(csvReader))
        csvDataFile.seek(0)
        for i in range(0, n):
            result.append([])
        for row in csvReader:
            for x in range(0, n):
                result[x].append(row[x])
    for i in range(1,len(result[0])):
        user = Customers(id=int(result[0][i]), first_name=result[1][i],last_name=result[2][i],gender=result[3][i],email=result[4][i],age=int(result[5][i]),address=result[6][i],state=result[7][i],zipcode=int(result[8][i]),phoneNumber=result[9][i],registrationDate=datetime.strptime(result[10][i],'%Y-%m-%dT%H:%M:%Sz'))
        db.session.add(user)
    db.session.commit()
    return "Transefer to db"

# @app.route("/a",methods=['GET','DELETE'])
# def g():
#     id=request.args.get('id')
#     if request.method=='GET':
#         cols = ['id', 'first_name', 'last_name','gender','email','age','address','state','zipcode','phoneNumber','registrationDate']
#         data = Customers.query.all()
#         result = [{col: getattr(d, col) for col in cols} for d in data]
#         return jsonify(result=result)
#     if request.method=='DELETE':
#         Customers.query.filter_by(id=id).delete()
#         db.session.commit()
#         return 'success deletion with id {}'.format(id)

