from flask import Blueprint, render_template

about_bp = Blueprint('about', __name__)

@about_bp.route('/about')
def about():
    return render_template("base.html", title="About", content="""
        <h2>About Me</h2>
        <p>I am a passionate developer building web applications with Python and Flask.</p>
    """)
