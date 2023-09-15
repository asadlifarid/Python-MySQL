from flask import render_template, request
from app import app
from models import *
@app.route('/blog')
def blog_page():
    return render_template('blog.html')
@app.route('/')
def main():
    blogs = Blog.query.all()
    page = request.args.get('page', 1, type=int)
    pagination = Blog.query.order_by(Blog.title).paginate(page=page, per_page=3)  # Flask SQLAlchemy 3.0-dan sonraki versiya ucun, only keyword args qebul edir, not positional args; (don't write: paginate(page, per_page=3); write: like in return: <--)
    return render_template('main.html', pagination=pagination)