from flask import Blueprint, render_template

blog_bp = Blueprint('blog', __name__)

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

@blog_bp.route('/blog')
def blog():
    posts_html = ""
    for post in BLOG_POSTS:
        posts_html += f'''
        <div class="blog-post">
            <h3>{post["title"]}</h3>
            <time>{post["date"]}</time>
            <p>{post["content"][:150]}...</p>
        </div>
        '''
    return render_template("base.html", title="Blog", content=f"""
        <h2>Blog Posts</h2>
        {posts_html}
    """)
