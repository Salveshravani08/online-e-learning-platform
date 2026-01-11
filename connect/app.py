
from flask import Flask, render_template, request, redirect, session, flash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text, create_engine
import pymysql
import os

pymysql.install_as_MySQLdb()  # Use pymysql instead of MySQLdb

# TEMPLATE_DIR = os.path.abspath(os.path.join(os.getcwd(), "connection", "templates"))
TEMPLATE_DIR = r"C:\Users\Admin\Desktop\online education project\connect\templates\admins"
app = Flask(__name__, template_folder=TEMPLATE_DIR)

# Creates a Flask application 
app.secret_key = "secret key"  # Used to manage user sessions securely
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:manishasaroj@localhost/e_learning_project"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Prevents SQLAlchemy from tracking modifications (saves memory)
db = SQLAlchemy(app)  # Creating database object

print("Database URI:", app.config['SQLALCHEMY_DATABASE_URI'])
print("SQLAlchemy is set properly")

DB_URI = "mysql+pymysql://root:manishasaroj@localhost/e_learning_project"
with app.app_context():
    try:
        engine = create_engine(DB_URI)
        connection = engine.connect()
        print("Database connected successfully")
        sql = text("SELECT * FROM admin_login")
        result = db.session.execute(sql).fetchall()
        print("Admin table:")
        for row in result:
            print(row)
        connection.close()
    except Exception as e:
        print("Database connection failed", e)

# ✅ Corrected Code: Admin Panel Route is Now Outside the Login Function
@app.route("/adminpanel") 
def admin_panel():
    if "admin" in session:
        return render_template("adminpanel.html")
    else:
        flash("Please log in first", "error")
        return redirect("/adminlogin")

@app.route("/", methods=["GET", "POST"])
@app.route("/adminlogin", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        admin1 = request.form.get("admin_name")
        password1 = request.form.get("password")
        sql = text("SELECT * FROM admin_login WHERE name = :name AND password = :password")
        result = db.session.execute(sql, {"name": admin1, "password": password1}).fetchone()
        if result:
            session["admin"] = admin1
            session["password"] = password1
            return redirect("/adminpanel")  # ✅ Just redirect instead of defining a new route
        else:
            flash("Invalid username or password", "error")
    return render_template("adminlogin.html")

#------------------------------redirect to students page----------------------------
@app.route("/student")
def student():
    return render_template('students.html')

#--------------------------------redirect to course page--------------------------
@app.route("/course")
def course():
    return render_template("courses.html")










if __name__ == '__main__':
    app.run(debug=True)  # Debug mode enabled: shows errors in browser and auto-restarts on code changes
    