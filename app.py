from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/services")
def services():
    return render_template("services.html")

@app.route("/specialities")
def specialities():
    return render_template("specialities.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/refer")
def refer():
    return render_template("refer.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/admin")
def admin():
    return render_template("admin.html")

if __name__ == "__main__":
    app.run(debug=True)
@app.route("/services")
def services():
    return render_template("services.html")
# from flask import Flask, render_template, request, redirect, flash
# import mysql.connector
#
# app = Flask(__name__)
# app.secret_key = "supersecretkey"
#
# # DATABASE CONNECTION
# db = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="",   # change this
#     database="flask_app"
# )
# cursor = db.cursor()
#
# @app.route(f"/contact", methods=["GET", "POST"])
# def contact():
#     if request.method == "POST":
#         name = request.form.get("name")
#         phone = request.form.get("phone")
#         email = request.form.get("email")
#         service = request.form.get("service")
#         message = request.form.get("message")
#
#         # BASIC VALIDATION
#         if not name or not phone or not email or not service:
#             flash("All fields are required", "danger")
#             return redirect("/contact")
#
#         # SAVE TO DATABASE
#         sql = """
#         INSERT INTO contacts (name, phone, email, service, message)
#         VALUES (%s, %s, %s, %s, %s)
#         """
#         values = (name, phone, email, service, message)
#
#         cursor.execute(sql, values)
#         db.commit()
#
#         flash("Contact form submitted successfully!", "success")
#         return redirect("/contact")
#
#     return render_template("contact.html")
#
# if __name__ == "__main__":
#     app.run(debug=True)
# from flask import Flask, render_template, request, redirect, flash
# import mysql.connector
#
# app = Flask(__name__)
# app.secret_key = "secret123"
#
# # DB connection
# db = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="",   # change
#     database="flask_app"
# )
# cursor = db.cursor()
#
# @app.route("/")
# def home():
#     return "Home OK"
#
# @app.route("/contact", methods=["GET", "POST"])
# def contact():
#     if request.method == "POST":
#         print("POST RECEIVED")   # DEBUG LINE
#
#         name = request.form.get("name")
#         phone = request.form.get("phone")
#         email = request.form.get("email")
#         service = request.form.get("service")
#         message = request.form.get("message")
#
#         cursor.execute(
#             "INSERT INTO contacts (name, phone, email, service, message) VALUES (%s,%s,%s,%s,%s)",
#             (name, phone, email, service, message)
#         )
#         db.commit()
#
#         flash("Saved successfully", "success")
#         return redirect("/contact")
#
#     return render_template("contact.html")
#
# if __name__ == "__main__":
#     app.run(debug=True)
# @app.route("/post-test", methods=["POST"])
# def post_test():
#     return "POST OK"
# @app.route("/contact", methods=["GET", "POST"])
# def contact():
#     ...
from flask import Flask, render_template, request, redirect, flash
import mysql.connector

app = Flask(__name__)
app.secret_key = ""

# Database connection
db = mysql.connector.connect(
    host="localhost",
    user="root",           # your MySQL username
    password="",   # your MySQL password
    database="flask_app"
)

cursor = db.cursor()
@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        # Get form data
        name = request.form.get("name")
        phone = request.form.get("phone")
        email = request.form.get("email")
        service = request.form.get("service")
        message = request.form.get("message")

        # Basic validation
        if not name or not phone or not email or not service:
            flash("All fields are required", "danger")
            return redirect("/contact")

        # Save to database
        sql = "INSERT INTO contacts (name, phone, email, service, message) VALUES (%s,%s,%s,%s,%s)"
        values = (name, phone, email, service, message)
        cursor.execute(sql, values)
        db.commit()

        flash("Form submitted successfully!", "success")
        return redirect("/contact")

    return render_template("contact.html")
