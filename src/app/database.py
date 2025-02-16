from flask_sqlalchemy import SQLAlchemy
from app import app
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://user:password@localhost/calculator_db'
db = SQLAlchemy(app)
class Calculation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    num1 = db.Column(db.Float, nullable=False)
    num2 = db.Column(db.Float, nullable=False)
    operation = db.Column(db.String(10), nullable=False)
    result = db.Column(db.Float, nullable=False)

db.create_all()
