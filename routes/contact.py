from flask import Blueprint, render_template, request, redirect, url_for, flash
from config import db, cursor
from email_validator import validate_email, EmailNotValidError

contact_bp = Blueprint("contact", __name__)

@contact_bp.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name")
        phone = request.form.get("phone")
        email = request.form.get("email")
        service = request.form.get("service")

        # Validation
        if not all([name, phone, email, service]):
            flash("All fields required", "danger")
            return redirect(url_for("contact.contact"))

        try:
            validate_email(email)
        except EmailNotValidError:
            flash("Invalid email", "danger")
            return redirect(url_for("contact.contact"))

        if not phone.isdigit():
            flash("Phone must be numbers only", "danger")
            return redirect(url_for("contact.contact"))

        # Save to DB
        cursor.execute(
            "INSERT INTO contacts (name, phone, email, service) VALUES (%s,%s,%s,%s)",
            (name, phone, email, service)
        )
        db.commit()

        flash("Form submitted successfully!", "success")
        return redirect(url_for("contact.contact"))

    return render_template("contact.html")
