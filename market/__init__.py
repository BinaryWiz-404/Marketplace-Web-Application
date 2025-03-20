from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt #this is for hash password not plane password
from flask_login import LoginManager #this library handle the login functions and properies

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
app.config['SECRET_KEY']='1b9f64bac563c6709af59ceb' #this will give security to user
db = SQLAlchemy(app)
bcrypt=Bcrypt(app)
login_manager=LoginManager(app)
login_manager.login_view="login_page" #this is search where is the login route which will be help for login_required
login_manager.login_message_category="info"

from market import routes



    # """ creating environment variable
    # in terminal python -m venv C:\Users\acer\OneDrive\Desktop\FlaskTut\venv """

# write this command in terminal to create database along with above SQLAlchemy code
# >>> from market import app,db
# >>> app.app_context().push()
# >>> db.create_all()
# >>> from market.models import Item here Item is a class
# >>> item1=Item(name="Iphone 16",price=500,barcode='846154104831',description='desc')
# >>> db.session.add(item1)
# >>> db.session.commit()
# >>> Item.query.all()
# [<Item 1>]
# >> for item in Item.query.all():
# ...     item.name
# ...     item.price
# ...     item.description
# ...     item.barcode
# >>> for item in Item.query.filter_by(price=500):
# ...     item.name
# ... 
# 'Iphone 16'

#relationship
# >>> item1.owner=User.query.filter_by(username='jst').first()
# >>> db.session.rollback()
# >>> item1.owner=User.query.filter_by(username='jst').first().id  
# >>> db.session.add(item1)
# >>> db.session.commit()
# >>> item1.owner
# 1   
# >>> i=Item.query.filter_by(name='iphone 16')
# >>> i=Item.query.filter_by(name='iphone 16').first()
# >>> i.owned_user
# <User 1>

#  below are for security purpose
# >> import os
# >>> os.urandom(12).hex()
