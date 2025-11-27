# init_db.py
from app import db, create_app
from models import User, Student
from werkzeug.security import generate_password_hash

app = create_app()
app.app_context().push()

# recreate DB
db.drop_all()
db.create_all()

# create default admin
admin = User(username="admin", password_hash=generate_password_hash("admin123"))
db.session.add(admin)

# sample data
s1 = Student(name="Asha Kumar", usn="4NI22IS001", branch="ISE", year=4, email="asha@example.com", phone="9876543210")
s2 = Student(name="Balu Rao", usn="4NI22IS002", branch="CSE", year=3, email="balu@example.com", phone="9123456780")
db.session.add_all([s1, s2])
db.session.commit()

print("DB initialized with admin/admin123 and 2 sample students.")
