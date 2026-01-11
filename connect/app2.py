from flask import Flask, request, render_template , flash ,redirect, url_for , session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
from flask_bcrypt import Bcrypt
import pymysql
import random
import smtplib
import json
import os
from dotenv import load_dotenv
import chatboat
import subprocess

pymysql.install_as_MySQLdb()

TEMPLATE_DIR = r"C:\Users\Admin\Desktop\online education project\connect\templates"
app = Flask(__name__, template_folder=TEMPLATE_DIR, static_folder='static')
app.secret_key = 'secret key'

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:manishasaroj@localhost/e_learning_project"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
print("connected with database")

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

#------------------------otp store ------------------------------
class OTPStore:
    otp_data={}

#------------ Define Model for signup table  -----------------------------
class User(db.Model):
     __tablename__ = 'signup'  
    
     id = db.Column(db.Integer, autoincrement=True, primary_key=True)
     username = db.Column(db.String(100), nullable=False)
     email = db.Column(db.String(255), unique=True, nullable=False)
     password = db.Column(db.String(255), nullable=False)
     confirm_password = db.Column(db.String(255), nullable=False)

     def __init__(self, username, email, password, confirm_password):
         self.username = username
         self.email = email
         self.password = password
         self.confirm_password = confirm_password
         
#--------------------------home page ------------------
@app.route("/")
@app.route("/homepage")
def home():
      return render_template('home/index.html')
  
  
#-------------------------chatboat route---------------------




@app.route("/chatboat", methods=["GET", "POST"])
def chatboat_page():
    script_path = os.path.join(os.path.dirname(__file__), "chatboat.py")  
    #subprocess.Popen(["python", script_path])  # shell=True hata diya
    subprocess.Popen(["python", script_path], creationflags=subprocess.CREATE_NEW_CONSOLE)

    return "chatboat is running "


# @app.route("/chatboat" , methods=["GET","POST"])
# def chatboat_page():
#     script_path =  os.path.abspath("chatboat.py")
#     subprocess.Popen(["python",script_path],shell = True) # chatboat ui run krega
#     return "chatboat is running in a separate window"

  
#-----------------course to learn route (accessible in home page)----------------

# Home Page (HTML Course Page)
@app.route("/htmlcourse")
def htmlcourse():
    if not session.get('logged_in'):
        return redirect(url_for('signup'))
    
    return render_template("courses_to_learn/html_course/htmlcourse.html",videos=videos)

# Video data with IDs and titles
videos = [
    {"id": "1", "title": "Introduction to HTML", "videoId": "GpcMasRWUhI"},
    {"id": "2", "title": "Basic Syntax", "videoId": "V1JBgugIL8w"},
    {"id": "3", "title": "Basic Syntax (Practical)", "videoId": "Tu14tj4ar_A"},
    {"id": "4.1", "title": "Text Formatting 1", "videoId": "YBmpqYthJJ8"},
    {"id": "4.2", "title": "Text Formatting 2", "videoId": "XwXkZ74vQ4E"},
    {"id": "4.3", "title": "Text Formatting 3", "videoId": "jCsIho1SacM"},
    {"id": "5.1", "title": "Listing Tags 1", "videoId": "PDWMjxt3XWQ"},
    {"id": "5.2", "title": "Listing Tags 2", "videoId": "1A2RvJur8rA"},
    {"id": "6", "title": "Marquee Tag", "videoId": "2-wS6hfqz9A"},
    {"id": "7", "title": "Pre Tag and Horizontal Rule", "videoId": "jWjlVq2NlsY"},
    {"id": "8", "title": "Image Tag", "videoId": "91_aOgptVJI"},
    {"id": "9.1", "title": "Anchor Tag 1", "videoId": "TRtiuK2_0Xk"},
    {"id": "9.2", "title": "Anchor Tag 2", "videoId": "3FCU5PkuR8A"},
    {"id": "10.1", "title": "Table Tag 1", "videoId": "DgcoTl1eu9o"},
    {"id": "10.2", "title": "Table Tag 2", "videoId": "DgcoTl1eu9o"},
    {"id": "11", "title": "Website Layout in Tables", "videoId": "gs6zQQvSXz0"},
    {"id": "12", "title": "Table Head and Body Tag", "videoId": "eabb6JTgkNw"},
    {"id": "13", "title": "HTML Audio Tag", "videoId": "TyYJ2z4Hrh8"},
    {"id": "14", "title": "HTML Video Tag", "videoId": "ncvvD_dwqmg"},
    {"id": "15.1", "title": "HTML Form Tag 1", "videoId": "FPaC9-fXt3w"},
    {"id": "15.2", "title": "HTML Form Tag 2", "videoId": "NwY2HIkE730"},
    {"id": "15.3", "title": "HTML Form Tag 3", "videoId": "DkXbqN8wBHc"},
    {"id": "16.1", "title": "HTML5 New Input Types 1", "videoId": "eV00PQme6Is"},
    {"id": "16.2", "title": "HTML5 New Input Types 2", "videoId": "bZmmiLeLx5w"}
]


# Video Page with Dynamic Video Loading
@app.route('/htmlvideo')
def html_video():
    if not session.get('logged_in'):
        return redirect(url_for('signup'))
    return render_template("courses_to_learn/html_course/video.html",videos=videos)
    
    video_id = request.args.get('videoId')
    video_data = next((v for v in videos if v['videoId'] == video_id), None)
    if video_data:
        return render_template('video.html', video=video_data)
    else:
        return "Video not found", 404

# ---------css course-----------------------------------


@app.route("/csscourse")
def csscourse():
    if not session.get('logged_in'):
        return redirect(url_for('signup'))
    
    return render_template("courses_to_learn/css_course/csscourse.html")


css_videos = [
    {"id": "1", "title": "Introduction to CSS", "videoId": "TThZIt4r3eg&list"},
    {"id": "2", "title": "CSS Selectors", "videoId": "cb-p_gkhIC0&list"},
    {"id": "3", "title": "CSS Box Model", "videoId": "nPYuVfdJPaQ&list"},
    {"id": "4", "title": "CSS Flexbox", "videoId": "B6vIXBQH0a0&list"},
    {"id": "5", "title": "CSS Grid", "videoId": "-YWYf43Flho&list"},
    {"id": "6", "title": "CSS Positions", "videoId": "vptCiCt5pd4&list"},
    {"id": "7", "title": "CSS Colors", "videoId": "u1peNIKIQqY&list"},
    {"id": "8", "title": "CSS Fonts", "videoId": "ZlNntIzOM9A&list"},
    {"id": "9", "title": "CSS Backgrounds", "videoId": "6J0mGQtubAo&list"},
    {"id": "10", "title": "CSS Borders", "videoId": "Si_vVgOfwNk&list"},
    {"id": "11", "title": "CSS Margins and Padding", "videoId": "ojBvwWId5vY&list"},
    {"id": "12", "title": "CSS Display", "videoId": "1qEqhCWMvfo&list"},
    {"id": "13", "title": "CSS Media Queries", "videoId": "aB2Y8VwV1X8&list"},
    {"id": "14", "title": "CSS Transitions", "videoId": "HEXKgdDQMrU&list"},
    {"id": "15", "title": "CSS Animations", "videoId": "dfFyYoI9YMg&list"},
    {"id": "16", "title": "CSS Variables", "videoId": "2rpgrrzx7-k&list"},
    {"id": "17", "title": "CSS Shadows", "videoId": "5IVbuwrrqBE&list"},
    {"id": "18", "title": "CSS Pseudo Elements", "videoId": "fOl16TGp9vg&list"},
    {"id": "19", "title": "CSS Pseudo Classes", "videoId": "UJQHGJKeWsQ&list"}
]


@app.route('/cssvideo/<videoId>', endpoint='css_video')
def css_video(videoId):
    # Find the video data by matching videoId
    video_data = next((v for v in css_videos if v['videoId'] == videoId), None)
    if video_data:
        video_id = video_data['videoId'].split('&')[0]  # Removes extra parameters
        return render_template('courses_to_learn/css_course/css_video.html', video={**video_data, 'videoId': video_id})
    else:
        return "Video not found", 404

#------------js course----------------------------

@app.route("/jscourse")
def jscourse():
    return render_template("courses_to_learn/js_course/jscourse.html")

# read json file
def load_js_videos():
    json_path = os.path.join(os.path.dirname(__file__), 'json', 'js_videos.json')
    if not os.path.exists(json_path):
        raise FileNotFoundError(f"File not found: {json_path}")

    with open(json_path, 'r', encoding='utf-8') as file:
        try:
            return json.load(file)
        except json.JSONDecodeError as e:
            raise ValueError(f"JSON Decode Error: {e}")


@app.route('/jsvideo/<videoId>', endpoint='jsvideo')
def jsvideo(videoId):
    js_videos = load_js_videos()  # Load videos before searching
    
    # Find video data by videoId
    video_data = next((v for v in js_videos if v['videoId'] == videoId), None)
    
    if video_data:
        video_id = video_data['videoId'].split('&')[0]  # Removes extra parameters
        return render_template('courses_to_learn/js_course/js_video.html', video=video_data, videoId=video_id)
    else:
        return "Video not found", 404

    
#--------------------python course-------------------------

@app.route("/pythoncourse")
def pythoncourse():
    return render_template("courses_to_learn/python_course/pythoncourse.html")

# Read JSON file
def load_python_videos():
    # Constructing the path dynamically
    json_path = os.path.join(os.path.dirname(__file__), 'json', 'python_videos.json')
    
    # Reading the JSON file
    with open(json_path, 'r') as file:
        return json.load(file)

@app.route('/pythonvideo/<videoId>', endpoint='python_video')
def python_video(videoId):
    python_videos = load_python_videos()  # Load videos before searching
    
    # Find video data by videoId
    video_data = next((v for v in python_videos if v['videoId'] == videoId), None)
    
    if video_data:
        video_id = video_data['videoId'].split('&')[0]  # Removes extra parameters
        return render_template('courses_to_learn/python_course/python_video.html', video=video_data, videoId=video_id)
    else:
        return "Video not found", 404
    
#-----------------------c course and videos---------------------------
@app.route("/ccourse")
def ccourse():
    return render_template("courses_to_learn/c_course/ccourse.html")


# Read JSON file
def load_c_videos():
    # Constructing the path dynamically
    json_path = os.path.join(os.path.dirname(__file__), 'json', 'c_videos.json')
    
    # Reading the JSON file
    with open(json_path, 'r') as file:
        return json.load(file)

@app.route('/cvideo/<videoId>', endpoint='c_video')
def c_video(videoId):
    c_videos = load_c_videos()  # Load videos before searching
    
    # Find video data by videoId
    video_data = next((v for v in c_videos if v['videoId'] == videoId), None)
    
    if video_data:
        video_id = video_data['videoId'].split('&')[0]  # Removes extra parameters
        return render_template('courses_to_learn/c_course/c_video.html', video=video_data, videoId=video_id)
    else:
        return "Video not found", 404
    



#---------------cpp course route----------------------------------

@app.route("/cppcourse")
def cppcourse():
    return render_template("courses_to_learn/cpp_course/cppcourse.html")
# Read JSON file
def load_cpp_videos():
    # Constructing the path dynamically
    json_path = os.path.join(os.path.dirname(__file__), 'json', 'cpp_videos.json')
    
    # Reading the JSON file
    with open(json_path, 'r') as file:
        return json.load(file)

@app.route('/cppvideo/<videoId>', endpoint='cpp_video')
def cpp_video(videoId):
    cpp_videos = load_cpp_videos()  # Load videos before searching
    
    # Find video data by videoId
    video_data = next((v for v in cpp_videos if v['videoId'] == videoId), None)
    
    if video_data:
        video_id = video_data['videoId'].split('&')[0]  # Removes extra parameters
        return render_template('courses_to_learn/cpp_course/cpp_video.html', video=video_data, videoId=video_id)
    else:
        return "Video not found", 404
    
    
#----------------------signup route ----------------------     
@app.route("/signup", methods=["GET", "POST"])
def signup():
    # flash("signup page - please register or log in to access the course")
    if request.method == "POST":
        username = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]
        confirm_password = request.form["confirmpassword"]
        
        # Check if passwords match
        if password != confirm_password:
            flash("Password does not match", "error")
            return redirect(url_for('signup'))
        
        # Check if email already exists
        if User.query.filter_by(email=email).first():
            flash("This email is already registered", "error")
            return redirect(url_for('signup'))    
        
        # Hash password
        hashed_password = bcrypt.generate_password_hash(password).decode("utf-8")
        
        # Insert into signup table
        new_user = User(username=username, email=email, password=hashed_password , confirm_password = confirm_password)
        db.session.add(new_user)
        db.session.commit()

        flash("Signup successful", "success")
        return redirect(url_for('login'))
    
    return render_template("auth/signup.html")

# ---------------------login route------------------------------------------
    
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["login_email"]
        password = request.form["login_password"]
        
        # Check if user exists
        user = User.query.filter_by(email=email).first()
        if user and bcrypt.check_password_hash(user.password, password):
            session['logged_in'] = True
            session['user_id'] = user.id
            flash("Login successful! now you can access the course", "success")
            #return redirect(url_for('dashboard'))
        else:
            flash("Invalid email or password", "error")
            return redirect(url_for('login'))
        
    
    return render_template("auth/signup.html")  # Assuming signup.html contains login and signup

# ------logout -------

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('home'))  # Change 'index' to 'home'

  

# Quiz Interface Route (Accessible from Homepage or inside the website)

@app.route("/quizinterface")
def quizinterface():
    return render_template("/quiz_interface/quizinterface.html")

# htmlquiz interface route (accessible from the homepage)
@app.route("/htmlquiz")
def htmlquiz():
    return render_template("/quizes_test/html_quiz/htmlquiz.html")

# cssquiz interface route (accessible from the homepage) quizes_test\css_quiz\cssquiz.html
@app.route("/cssquiz")
def cssquiz():
    return render_template("/quizes_test/css_quiz/cssquiz.html")

# jsquiz interface route (accessible from the home page)
@app.route("/jsquiz")
def jsquiz():
    return render_template("/quizes_test/js_quiz/jsquiz.html")

# pythonquiz interface route (accessible from the homepage) 
@app.route("/pythonquiz")
def pythonquiz():
    return  render_template("/quizes_test/python_quiz/pythonquiz.html")


# cquiz interface route (accessible from the homepage)
@app.route("/cquiz")
def cquiz():
    return render_template("/quizes_test/c_quiz/cquiz.html")

# c++quiz interface route (accessible from the homepage)
@app.route("/cppquiz")
def cppquiz():
    return render_template("/quizes_test/cpp_quiz/cppquiz.html")




#-----------------------send otp funciton----------------------
import random
import smtplib


print("send otp functio is here")
def send_otp(email, otp):
    print("u r in otp function")
    sender_email = "manishasaroj003@gmail.com"
    sender_password = "jrax cnyp tbjl mhux"
    
    subject = "Your OTP for Password Reset"
    body = f"Your OTP is: {otp}"
    message = f"Subject: {subject}\n\n{body}"

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, email, message)
        print("OTP sent successfully.")
        return True
    except Exception as e:
        print("Failed to send OTP:", e)
        return False
# ---------------------------------------- Forgot Password Route---------------------------
@app.route("/forgot", methods=["GET", "POST"])
def forgot():
    print("u r in forgot pasword")
    if request.method == "POST":
        email = request.form.get("email")
        print("receivd eamil")
        if not email or '@' not in email:
            flash("Invalid email address.", "error")
            return render_template("signup.html")

        user = User.query.filter_by(email=email).first()
        if user:
            otp = str(random.randint(100000, 999999))
            OTPStore.otp_data[email] = otp
            send_otp(email, otp) 
            flash("OTP sent to your email.", "success")
            return redirect(url_for("verify_otp", email=email))
        else:
            flash("Email not registered.", "error")
    return render_template("signup.html")
                
#----------------------verify otp route-----------------
@app.route("/verify/<email>", methods=["GET", "POST"])
def verify_otp(email):
    if request.method == 'POST':
        entered_otp = request.form.get("otp")
        if OTPStore.otp_data.get(email) == entered_otp:
            flash("OTP verified. Set your new password.", "success")
            return redirect(url_for("reset_password", email=email))
        else:
            flash("Invalid OTP. Please try again.", "error")
    return render_template("signup.html")        

# --------------------- Reset Password Route ----------------------
@app.route("/resetpassword/<email>", methods=["GET", "POST"])
def reset_password(email):
    if request.method == "POST":
        new_password = request.form.get("new_password")
        confirm_password = request.form.get("confirm_newpassword")
        
        if new_password != confirm_password:
            flash("Passwords do not match.", "error")
        else:
            user = User.query.filter_by(email=email).first()
            if user:
                hashed_password = bcrypt.generate_password_hash(new_password).decode("utf-8")
                user.password = hashed_password
                db.session.commit()
                flash("Password reset successful.", "success")
                return redirect(url_for("login"))
            else:
                flash("User not found.", "error")
    return render_template("signup.html")
        
        
if __name__ == "__main__":
    #db.create_all()
    app.run(debug=True)