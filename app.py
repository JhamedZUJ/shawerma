from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///employees.db'
app.config['SECRET_KEY'] = 'your_secret_key'
db = SQLAlchemy(app)


class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    start_time = db.Column(db.DateTime, nullable=True)
    end_time = db.Column(db.DateTime, nullable=True)
    status = db.Column(db.String(10), default="Not Working")


with app.app_context():
    db.create_all()
    # Check if employees already exist in the database
    if not Employee.query.all():
        # Add sample employees
        db.session.add(Employee(name='jamil'))
        db.session.add(Employee(name='mlak'))
        db.session.add(Employee(name='khalil'))
        db.session.add(Employee(name='jeff'))
        db.session.add(Employee(name='saif'))
        db.session.add(Employee(name='omar'))
        db.session.add(Employee(name='zuhdi'))
        db.session.add(Employee(name='mohammad'))
        db.session.add(Employee(name='samir'))
        db.session.commit()


@app.route('/')
def index():
    employees = Employee.query.all()
    return render_template('index.html', employees=employees)


@app.route('/start/<int:id>')
def start_shift(id):
    employee = Employee.query.get(id)
    employee.start_time = datetime.now()
    employee.status = "Working"
    db.session.commit()
    flash(f"{employee.name} started their shift!")
    return redirect(url_for('index'))


@app.route('/end/<int:id>')
def end_shift(id):
    employee = Employee.query.get(id)
    employee.end_time = datetime.now()
    employee.status = "Not Working"
    db.session.commit()
    flash(f"{employee.name} ended their shift!")
    return redirect(url_for('index'))


# if __name__ == '__main__':
#     app.run(debug=True)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8001)
