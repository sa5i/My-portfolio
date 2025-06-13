from flask import Blueprint, render_template

projects_bp = Blueprint('projects', __name__)

@projects_bp.route('/projects')
def projects():
    return render_template("base.html", title="Projects", content="""
        <h2>My Projects</h2>
        <ul style="list-style: none; padding: 0;">
            <li style="margin-bottom: 10px;"><strong>Flask Portfolio</strong><br>Modern portfolio site using Flask</li>
            <li style="margin-bottom: 10px;"><strong>CI/CD Pipeline</strong><br>Automated builds with Jenkins</li>
            <li><strong>Cloud Hosting</strong><br>Deployments on AWS with Docker</li>
        </ul>
    """)
