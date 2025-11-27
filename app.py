# app.py
from flask import Flask, render_template, request, redirect, url_for, flash, session, jsonify
from models import db, User, Student
from werkzeug.security import check_password_hash
import re

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'dev-secret-key'
    db.init_app(app)

    @app.route('/')
    def index():
        if 'user_id' in session:
            return redirect(url_for('dashboard'))
        return redirect(url_for('login'))

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'POST':
            username = request.form.get('username','').strip()
            password = request.form.get('password','').strip()
            user = User.query.filter_by(username=username).first()
            if user and check_password_hash(user.password_hash, password):
                session['user_id'] = user.id
                session['username'] = user.username
                return redirect(url_for('dashboard'))
            else:
                flash('Invalid username or password', 'danger')
        return render_template('login.html')

    def login_required(f):
        from functools import wraps
        @wraps(f)
        def decorated(*args, **kwargs):
            if 'user_id' not in session:
                return redirect(url_for('login'))
            return f(*args, **kwargs)
        return decorated

    @app.route('/logout')
    def logout():
        session.clear()
        return redirect(url_for('login'))

    @app.route('/dashboard')
    @login_required
    def dashboard():
        q = request.args.get('q', '').strip()
        branch = request.args.get('branch', '')
        year = request.args.get('year', '')
        students = Student.query
        if q:
            students = students.filter((Student.name.ilike(f'%{q}%')) | (Student.usn.ilike(f'%{q}%')))
        if branch:
            students = students.filter_by(branch=branch)
        if year:
            try:
                y = int(year)
                students = students.filter_by(year=y)
            except:
                pass
        students = students.order_by(Student.created_at.desc()).all()
        branches = [s.branch for s in Student.query.distinct(Student.branch)]
        years = sorted({s.year for s in Student.query.all()})
        return render_template('dashboard.html', students=students, branches=branches, years=years, q=q, sel_branch=branch, sel_year=year)

    @app.route('/student/add', methods=['GET', 'POST'])
    @login_required
    def add_student():
        if request.method == 'POST':
            name = request.form.get('name','').strip()
            usn = request.form.get('usn','').strip()
            branch = request.form.get('branch','').strip()
            year = request.form.get('year','').strip()
            email = request.form.get('email','').strip()
            phone = request.form.get('phone','').strip()

            # validations:
            if not name or not usn or not branch or not year:
                flash('Name, USN, Branch and Year are required.', 'danger')
                return redirect(url_for('add_student'))
            if email and not re.match(r"[^@]+@[^@]+\.[^@]+", email):
                flash('Invalid email format.', 'danger')
                return redirect(url_for('add_student'))

            existing = Student.query.filter_by(usn=usn).first()
            if existing:
                flash('Student with this USN already exists.', 'danger')
                return redirect(url_for('add_student'))

            s = Student(name=name, usn=usn, branch=branch, year=int(year), email=email, phone=phone)
            db.session.add(s)
            db.session.commit()
            flash('Student added successfully', 'success')
            return redirect(url_for('dashboard'))
        return render_template('student_form.html', action='Add')

    @app.route('/student/edit/<int:sid>', methods=['GET', 'POST'])
    @login_required
    def edit_student(sid):
        s = Student.query.get_or_404(sid)
        if request.method == 'POST':
            s.name = request.form.get('name','').strip()
            s.usn = request.form.get('usn','').strip()
            s.branch = request.form.get('branch','').strip()
            s.year = int(request.form.get('year','') or s.year)
            s.email = request.form.get('email','').strip()
            s.phone = request.form.get('phone','').strip()
            # simple validations
            if not s.name or not s.usn:
                flash('Name and USN required', 'danger')
                return redirect(url_for('edit_student', sid=sid))
            db.session.commit()
            flash('Student updated', 'success')
            return redirect(url_for('dashboard'))
        return render_template('student_form.html', action='Edit', student=s)

    @app.route('/student/delete/<int:sid>', methods=['POST'])
    @login_required
    def delete_student(sid):
        s = Student.query.get_or_404(sid)
        db.session.delete(s)
        db.session.commit()
        flash('Student deleted', 'success')
        return redirect(url_for('dashboard'))

    @app.route('/student/<int:sid>')
    @login_required
    def view_student(sid):
        s = Student.query.get_or_404(sid)
        return render_template('view_student.html', student=s)

    # simple API endpoint for tests (optional)
    @app.route('/api/students')
    def api_students():
        students = Student.query.all()
        data = [{"id":s.id,"name":s.name,"usn":s.usn} for s in students]
        return jsonify(data)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
