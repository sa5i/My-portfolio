from flask import Blueprint, render_template

skills_bp = Blueprint('skills', __name__)

@skills_bp.route('/skills')
def skills():
    content = """
        <h2>Skills & Experience</h2>
        <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/05/Devops-toolchain.svg/1200px-Devops-toolchain.svg.png" alt="DevOps" style="max-width:30%; height:auto; border-radius: 8px; margin-bottom: 20px;">
        <h3>DevOps Skills</h3>
        <ul>
            <li>CI/CD: Jenkins, GitHub Actions</li>
            <li>Containerization: Docker, Kubernetes</li>
            <li>Cloud Platforms: AWS, Azure</li>
            <li>Infrastructure as Code: Terraform, Ansible</li>
            <li>Monitoring: Prometheus, Grafana</li>
            <li>Version Control: Git</li>
        </ul>
        <h3>Other Skills</h3>
        <ul>
            <li>Python & Flask</li>
            <li>JavaScript & React</li>
            <li>Database Management: MySQL, PostgreSQL</li>
        </ul>
    """
    return render_template("base.html", title="Skills & Experience", content=content)
