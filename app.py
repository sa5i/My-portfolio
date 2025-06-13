from flask import Flask

app = Flask(__name__)

# Import blueprints
from routes.home import home_bp
from routes.skills import skills_bp
from routes.blog import blog_bp
from routes.about import about_bp
from routes.info import info_bp
from routes.contact import contact_bp
from routes.projects import projects_bp

# Register blueprints
app.register_blueprint(home_bp)
app.register_blueprint(skills_bp)
app.register_blueprint(blog_bp)
app.register_blueprint(about_bp)
app.register_blueprint(info_bp)
app.register_blueprint(contact_bp)
app.register_blueprint(projects_bp)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
