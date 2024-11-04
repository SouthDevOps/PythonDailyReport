from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///reports.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class TestCaseReport(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    emp_id = db.Column(db.String(50), nullable=False)
    pending = db.Column(db.Integer, default=0)
    in_progress = db.Column(db.Integer, default=0)
    completed = db.Column(db.Integer, default=0)
    blocked = db.Column(db.Integer, default=0)

with app.app_context(): db.create_all()


@app.route('/')
def home():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit_report():
    emp_id = request.form['emp_id']
    pending = request.form['pending']
    in_progress = request.form['in_progress']
    completed = request.form['completed']
    blocked = request.form['blocked']
    
    report = TestCaseReport(emp_id=emp_id, pending=pending, in_progress=in_progress,
                            completed=completed, blocked=blocked)
    db.session.add(report)
    db.session.commit()
    
    return redirect(url_for('view_reports'))

@app.route('/reports')
def view_reports():
    reports = TestCaseReport.query.all()
    return render_template('report.html', reports=reports)

if __name__ == '__main__':
    app.run(debug=True)
