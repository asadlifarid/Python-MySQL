from flask import Flask, render_template
app = Flask(__name__)
# mysql database ile connection qurmaq ucun;
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123@127.0.0.1:3306/blog'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SECRET_KEY'] = 'page'
app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
# Add administrative views here
from controllers import *
from extensions import *
from models import *
if __name__ == '__main__':
    app.init_app(db)
    app.init_app(migrate)