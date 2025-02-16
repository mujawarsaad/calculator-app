from flask import request, jsonify, render_template
from app import app
from database import db, Calculation

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate')
def calculate():
    num1 = float(request.args.get('num1'))
    num2 = float(request.args.get('num2'))
    operation = request.args.get('operation')
    if operation == 'add':
        result = num1 + num2
    elif operation == 'subtract':
        result = num1 - num2
    elif operation == 'multiply':
        result = num1 * num2
    elif operation == 'divide' and num2 != 0:
        result = num1 / num2
    else:
        result = 'Error'
    db.session.add(Calculation(num1=num1, num2=num2, operation=operation, result=result))
    db.session.commit()
    return jsonify({'result': result})
