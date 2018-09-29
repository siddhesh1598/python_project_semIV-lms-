from flask import Flask, render_template, redirect, url_for, request, session, send_file, send_from_directory
import sqlite3

app = Flask(__name__)

app.secret_key = "anything"

with sqlite3.connect("database.db", check_same_thread=False) as db:
    cursor = db.cursor()

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/login', methods=['GET','POST'])
def login():
    error = None
    if request.method == 'POST':
        username=request.form['username']
        password = request.form['password']
        find_user= ("SELECT * FROM User WHERE username = ? AND password = ?")
        cursor.execute(find_user,[(username), (password)])
        results = cursor.fetchall()

        if  results:
            for i in results:
                return (redirect(url_for("dashboard")))
        else:
            error = "Username and Password not recognized"
    return render_template("login.html", error=error)

@app.route('/signup', methods=['POST', 'GET'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        cursor.execute("""
        INSERT INTO User (username, password)
        VALUES (?, ?);
        """, (username, password))
        db.commit()
        return redirect(url_for('home'))
    return render_template("signup.html")

@app.route('/admin')
def admin():
    return render_template("admin.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/dashboard')
def dashboard():
    return render_template("dashboard.html")


if __name__ == "__main__":
    app.run(debug=True)