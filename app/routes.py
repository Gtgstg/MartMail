from flask_mail import Message

from flask import request,jsonify
from app import app, db, mail
from app.models import User,Temp

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
        return '<html>{}</html>'.format(user.html)
        # cols = ['id', 'name', 'html']
        # data = Temp.query.all()
        # result = [{col: getattr(d, col) for col in cols} for d in data]
        # return jsonify(result=result)
    if request.method=='PUT':
        user=Temp.query.filter_by(name=name).first()
        user.html=html
        db.session.commit()
        return 'updated email id is '+ html
    if request.method=='POST':
        user=Temp(name=name,html=html)
        db.session.add(user)
        db.session.commit()
        return 'Created new user with email {}'.format(name)
    if request.method=='DELETE':
        Temp.query.filter_by(name=name,html=html).delete()
        db.session.commit()
        return 'success deletion with name {}'.format(name)

@app.route("/email",methods=['POST'])
def email():
    name=request.args.get('name')
    print(name,'is this')
    recip=[]
    user =User.query.all()
    for i in user:
        recip.append(i.email)
    temp=Temp.query.filter_by(name=name).first()
    # print(temp.html)
    msg=Message('Hello',sender='yourId@gmail.com',recipients=recip,html=temp.html)
    mail.send(msg)
    return "Sent"