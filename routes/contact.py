from flask import Blueprint, render_template

contact_bp = Blueprint('contact', __name__)

@contact_bp.route('/contact')
def contact():
    return render_template("base.html", title="Contact", content="""
        <h2>Contact Me</h2>
        <p>Email: <a href="mailto:sasi@example.com">sasi@example.com</a></p>
    """)
