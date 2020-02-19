from datetime import date, datetime
from io import TextIOWrapper
import requests
from flask_mail import Message
from flask import request,jsonify
from app import app, db, mail
from app.models import User,Temp,Dynmic_Temp,Order,Reviews,UserProductList,Product,Customers
import csv

def customer(name):
    customer = User.query.filter_by(username=name).first()
    print(customer)
    return  (customer.email)

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


def delete_customer(name):
    User.query.filter_by(username=name).delete()
    db.session.commit()
    return 'success deletion with customername {}'.format(name)

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

def put_customer(new_id,name):
    admin = User.query.filter_by(username=name).first()
    # admin.emailid = new_id
    db.session.commit()
    return 'updated  id is cust@gmail.com'

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
    user =Customers.query.all()
    for i in user:
        temp=Dynmic_Temp.query.filter_by(name=name).first()
        if temp is None:
            continue
        orders=UserProductList.query.filter_by(userId=i.id).first()
        if orders is None:
            continue
        orders=orders.orderId
        price=Order.query.filter_by(id=orders).first()
        if price is None:
            continue
        price=price.totalPrice
        s=i.first_name+" "+i.last_name
        msg=Message('Hello',sender='yourId@gmail.com',recipients=list(i.email),html=temp.html.format(s,price,couponCode))
        mail.send(msg)
    return "Sent"

@app.route("/order",methods=['POST'])
def order():
    filecsv = request.files['fisier']
    filecsv = TextIOWrapper(filecsv, encoding='UTF-8')
    data = csv.reader(filecsv, delimiter=",")
    Cdata = list(data)
    for i in range(1,len(Cdata)):
        a,b,c=Cdata[i][1].split('/')
        user = Order(id=int(Cdata[i][0]), purchaseDate=date(int(c),int(b),int(a)),totalPrice=int(Cdata[i][2]))
        db.session.add(user)
    db.session.commit()
    return "Transefer to db"

@app.route("/reviews",methods=['POST'])
def reviews():
    filecsv = request.files['fisier']
    filecsv = TextIOWrapper(filecsv, encoding='UTF-8')
    data = csv.reader(filecsv, delimiter=",")
    Cdata = list(data)
    for i in range(1, len(Cdata)):
        user = Reviews(id=int(Cdata[i][0]), userProductid=int(Cdata[i][1]),productRating=int(Cdata[i][2]),reviewTitle=Cdata[i][3],reviewDetails=Cdata[i][4])
        db.session.add(user)
    db.session.commit()
    return "Transefer to db"

@app.route("/userprod",methods=['POST'])
def userprod():
    filecsv = request.files['fisier']
    filecsv = TextIOWrapper(filecsv, encoding='UTF-8')
    data = csv.reader(filecsv, delimiter=",")
    result = list(data)
    for i in range(1, len(result)):
        user = UserProductList(Id=int(result[i][0]), userId=int(result[i][1]),productId=int(result[i][2]),quantity=int(result[i][3]),orderId=int(result[i][4]))
        db.session.add(user)
    db.session.commit()
    return "Transefer to db"

@app.route("/product",methods=['POST'])
def product():
    filecsv = request.files['fisier']
    filecsv = TextIOWrapper(filecsv, encoding='UTF-8')
    data = csv.reader(filecsv, delimiter=",")
    result = list(data)
    for i in range(1, len(result)):
        user = Product(id=int(result[i][0]), SKU=result[i][1],productName=result[i][2],brand=result[i][3],productDescription=result[i][4],color=result[i][5],unitPrice=int(result[i][6]))
        db.session.add(user)
    db.session.commit()
    return "Transefer to db"

@app.route("/customers",methods=['POST'])
def customers():
    filecsv = request.files['fisier']
    filecsv = TextIOWrapper(filecsv, encoding='UTF-8')
    data = csv.reader(filecsv, delimiter=",")
    result = list(data)
    for i in range(1, len(result)):
        user = Customers(id=int(result[i][0]), first_name=result[i][1],last_name=result[i][2],gender=result[i][3],email=result[i][4],age=int(result[i][5]),address=result[i][6],state=result[i][7],zipcode=int(result[i][8]),phoneNumber=result[i][9],registrationDate=datetime.strptime(result[i][10],'%Y-%m-%dT%H:%M:%Sz'))
        db.session.add(user)
    db.session.commit()
    return "Transefer to db"

@app.route("/a",methods=['GET','DELETE'])
def g():
    if request.method=='GET':
        # cols = ['id', 'first_name', 'last_name','gender','email','age','address','state','zipcode','phoneNumber','registrationDate']
        # cols=['id','userProductid','productRating','reviewTitle','reviewDetails']
        # cols=['id','purchaseDate','totalPrice']
        cols=['Id','userId','productId','quantity','orderId']
        data = UserProductList.query.all()
        result = [{col: getattr(d, col) for col in cols} for d in data]
        return jsonify(result=result)
    if request.method=='DELETE':
        UserProductList.query.delete()
        db.session.commit()
        return 'success deletion'

def post_customer(customername, emailid, id):
    customer = User(customername=customername, emailid=emailid,id=id)
    db.session.add(customer)

    db.session.commit()
    return (customername)



