from flask import Flask, request, redirect, url_for

app = Flask(__name__)

# Sample blog posts (can later be from a CMS or markdown)
BLOG_POSTS = [
    {
        "id": 1,
        "title": "Getting Started with Flask",
        "date": "2025-05-01",
        "content": "Flask is a lightweight Python web framework perfect for small apps."
    },
    {
        "id": 2,
        "title": "Introduction to DevOps",
        "date": "2025-05-10",
        "content": "DevOps combines development and operations to improve collaboration and productivity."
    },
]

def generate_page(title, content):
    # The same generate_page function you have already,
    # add menu links for /skills and /blog as well.
    return f'''
    <!DOCTYPE html>
    <html lang="en" data-theme="light">
    <head>
        <meta charset="UTF-8">
        <title>{title} - SASI Portfolio</title>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600&display=swap" rel="stylesheet">
        <style>
            /* ... same styles as before ... */
            :root {{
                --bg: #ffffff;
                --text: #222222;
                --accent: #0077cc;
                --nav-bg: rgba(255, 255, 255, 0.95);
                --footer-bg: #f1f1f1;
            }}
            [data-theme="dark"] {{
                --bg: #1f1f1f;
                --text: #eaeaea;
                --accent: #4dabf7;
                --nav-bg: rgba(34, 34, 34, 0.95);
                --footer-bg: #2a2a2a;
            }}
            body {{
                font-family: 'Inter', sans-serif;
                margin: 0;
                background: var(--bg);
                color: var(--text);
                transition: all 0.4s;
            }}
            a {{ color: var(--accent); text-decoration: none; }}
            a:hover {{ opacity: 0.8; }}
            .navbar {{
                display: flex;
                justify-content: space-between;
                align-items: center;
                padding: 12px 20px;
                background: var(--nav-bg);
                box-shadow: 0 1px 5px rgba(0,0,0,0.05);
                position: sticky;
                top: 0;
                z-index: 10;
            }}
            .sasi-logo {{
                font-size: 22px;
                font-weight: 600;
                color: var(--accent);
            }}
            .menu-icon {{
                display: none;
                cursor: pointer;
            }}
            .menu-icon svg {{
                width: 28px;
                height: 28px;
                stroke: var(--accent);
            }}
            .nav-links {{
                display: flex;
                gap: 20px;
                align-items: center;
            }}
            .nav-links a {{
                font-weight: 500;
            }}
            .toggle-theme {{
                background: none;
                border: none;
                color: var(--accent);
                font-size: 20px;
                cursor: pointer;
            }}
            .content {{
                padding: 60px 20px;
                max-width: 900px;
                margin: auto;
                animation: fadeIn 0.8s ease-out forwards;
                opacity: 0;
            }}
            @keyframes fadeIn {{
                to {{ opacity: 1; }}
            }}
            .footer {{
                background: var(--footer-bg);
                padding: 20px;
                text-align: center;
                font-size: 14px;
                color: var(--text);
            }}
            .social-icons {{
                margin-top: 10px;
            }}
            .social-icons a {{
                margin: 0 10px;
                display: inline-block;
            }}
            .social-icons svg {{
                width: 28px;
                height: 28px;
                fill: var(--accent);
                transition: transform 0.3s ease;
            }}
            .social-icons svg:hover {{
                transform: scale(1.1);
            }}
            @media (max-width: 768px) {{
                .nav-links {{
                    display: none;
                    flex-direction: column;
                    background: var(--nav-bg);
                    position: absolute;
                    top: 60px;
                    right: 0;
                    width: 180px;
                    padding: 10px;
                    box-shadow: 0 4px 6px rgba(0,0,0,0.1);
                }}
                .nav-links.active {{
                    display: flex;
                }}
                .menu-icon {{
                    display: block;
                }}
            }}
            .blog-post {{
                border-bottom: 1px solid #ccc;
                margin-bottom: 20px;
                padding-bottom: 15px;
                text-align: left;
            }}
            .blog-post h3 {{
                margin: 0 0 5px 0;
                color: var(--accent);
            }}
            .blog-post time {{
                font-size: 0.9em;
                color: gray;
            }}
        </style>
    </head>
    <body>
        <div class="navbar">
            <div class="sasi-logo">SASI Portfolio</div>
            <div class="menu-icon" onclick="toggleMenu()">
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path d="M4 6h16M4 12h16M4 18h16" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>
            </div>
            <div class="nav-links" id="navLinks">
                <a href="/">Home</a>
                <a href="/projects">Projects</a>
                <a href="/skills">Skills</a>
                <a href="/blog">Blog</a>
                <a href="/about">About</a>
                <a href="/info">Info</a>
                <a href="/contact">Contact</a>
                <button class="toggle-theme" onclick="toggleTheme()" title="Toggle Dark Mode">🌙</button>
            </div>
        </div>
        <div class="content">{content}</div>
        <div class="footer">
            © 2025 SASI Portfolio
            <div class="social-icons">
                <a href="https://github.com" target="_blank" title="GitHub">
                    <svg viewBox="0 0 24 24"><path d="M12 .5C5.7.5.5 5.8.5 12.1c0 5.1 3.3 9.4 7.9 10.9.6.1.8-.2.8-.6v-2.1c-3.2.7-3.9-1.6-3.9-1.6-.5-1.3-1.1-1.6-1.1-1.6-.9-.6.1-.6.1-.6 1 .1 1.6 1 1.6 1 .9 1.5 2.4 1.1 3 .8.1-.7.4-1.1.7-1.3-2.6-.3-5.3-1.3-5.3-5.9 0-1.3.5-2.3 1.2-3.1-.1-.3-.5-1.4.1-2.8 0 0 1-.3 3.3 1.2a11.3 11.3 0 0 1 6 0c2.3-1.5 3.3-1.2 3.3-1.2.6 1.4.2 2.5.1 2.8.8.8 1.2 1.8 1.2 3.1 0 4.6-2.7 5.6-5.3 5.9.4.3.7.9.7 1.8v2.7c0 .4.2.7.8.6a10.8 10.8 0 0 0 7.9-10.9C23.5 5.8 18.3.5 12 .5z"/></svg>
                </a>
                <a href="https://www.linkedin.com/in/sasikanth-reddy-b7922816a/" target="_blank" title="LinkedIn">
                    <svg viewBox="0 0 24 24"><path d="M20.45 20.45h-3.554v-5.569c0-1.328-.024-3.04-1.852-3.04-1.852 0-2.136 1.445-2.136 2.94v5.669h-3.553V9h3.414v1.561h.05c.476-.9 1.637-1.852 3.368-1.852 3.602 0 4.265 2.37 4.265 5.451v6.285zM5.337 7.433a2.063 2.063 0 1 1 0-4.127 2.063 2.063 0 0 1 0 4.127zm1.776 13.017H3.561V9h3.552v11.45zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.226.792 24 1.771 24h20.451C23.206 24 24 23.226 24 22.271V1.729C24 .774 23.206 0 22.225 0z"/></svg>
                </a>
            </div>
        </div>
        <script>
            function toggleMenu() {{
                document.getElementById('navLinks').classList.toggle('active');
            }}
            function toggleTheme() {{
                const html = document.documentElement;
                const current = html.getAttribute("data-theme");
                const next = current === "dark" ? "light" : "dark";
                html.setAttribute("data-theme", next);
                localStorage.setItem("theme", next);
            }}
            (function () {{
                const saved = localStorage.getItem("theme") || "light";
                document.documentElement.setAttribute("data-theme", saved);
            }})();
        </script>
    </body>
    </html>
    '''

@app.route('/')
def home():
    return generate_page("Home", """
        <h1>Hello, SASI! 👋</h1>
        <p>Welcome to your modern, minimal portfolio site.</p>
    """)

@app.route('/skills')
def skills():
    return generate_page("Skills & Experience", """
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
    """)


@app.route('/blog')
def blog():
    # Render list of posts with title, date, and excerpt
    posts_html = ""
    for post in BLOG_POSTS:
        posts_html += f'''
        <div class="blog-post">
            <h3>{post["title"]}</h3>
            <time>{post["date"]}</time>
            <p>{post["content"][:150]}...</p>
            <!-- Could link to full post if you add individual pages -->
        </div>
        '''
    return generate_page("Blog", f"""
        <h2>Blog Posts</h2>
        {posts_html}
    """)

# Existing routes below (about, info, contact, projects) remain unchanged

@app.route('/about')
def about():
    return generate_page("About", """
        <h2>About Me</h2>
        <p>I am a passionate developer building web applications with Python and Flask.</p>
    """)

@app.route('/info')
def info():
    return generate_page("Info", """
        <h2>Information</h2>
        <p>This site is built using Flask with a responsive frontend and dark mode toggle.</p>
    """)

@app.route('/contact')
def contact():
    return generate_page("Contact", """
        <h2>Contact Me</h2>
        <p>Email: <a href="mailto:sasi@example.com">sasi@example.com</a></p>
    """)

@app.route('/projects')
def projects():
    return generate_page("Projects", """
        <h2>My Projects</h2>
        <ul style="list-style: none; padding: 0;">
            <li style="margin-bottom: 10px;"><strong>Flask Portfolio</strong><br>Modern portfolio site using Flask</li>
            <li style="margin-bottom: 10px;"><strong>CI/CD Pipeline</strong><br>Automated builds with Jenkins</li>
            <li><strong>Cloud Hosting</strong><br>Deployments on AWS with Docker</li>
        </ul>
    """)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

