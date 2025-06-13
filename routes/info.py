from flask import Blueprint, render_template

info_bp = Blueprint('info', __name__)

@info_bp.route('/info')
def info():
    return render_template("base.html", title="Info", content="""
        <h2>Information</h2>
        <p>This site is built using Flask with a responsive frontend and dark mode toggle.</p>
    """)
