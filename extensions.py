# third-party packages 

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app import app
db = SQLAlchemy(app)    
migrate = Migrate(app, db)  

 # database is created
 # database use for migrate
 # database configuration structrue is created  (models.py)
 # Migarte command   (flask db migrate)
 # MySQL'de tables is created