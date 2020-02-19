from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_mail import Mail

app = Flask(__name__)
app.debug=True
app.config.from_object(Config)
db=SQLAlchemy(app)
migrate=Migrate(app,db)
# app.config['MAIL_SERVER'] ='smtp.gmail.com'
# app.config['MAIL_PORT']=465
app.config['MAIL_SERVER']='localhost'
app.config['MAIL_PORT']=2525

mail=Mail(app)
from app import routes,models