from flask import Blueprint, render_template
from config import cursor

admin_bp = Blueprint("admin", __name__)

@admin_bp.route("/admin")
def admin():
    cursor.execute("SELECT * FROM contacts ORDER BY created_at DESC")
    contacts = cursor.fetchall()
    return render_template("admin.html", contacts=contacts)
