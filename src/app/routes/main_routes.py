from flask import Blueprint, render_template_string, current_app
from services.post_service import PostService

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    # Call API endpoint instead of directly accessing service
    # Use Flask's test client to make internal API call
    with current_app.test_client() as client:
        posts_response = client.get('/api/v1/posts')
        posts_data = posts_response.get_json()
        posts = posts_data.get('posts', [])
    
    # Generate HTML for posts
    posts_html = ""
    for post in posts:
        posts_html += f'''
        <article class="post-card">
            <h3><a href="#">{post['title']}</a></h3>
            <p class="post-date">{post['date']}</p>
            <p class="post-excerpt">{post['excerpt']}</p>
        </article>
        '''
    
    return render_template_string('''
<!DOCTYPE html>
<html>
<head>
    <title>Guest in the Universe</title>
    <style>
        body { 
            font-family: Arial, sans-serif; 
            max-width: 1000px; 
            margin: 0 auto; 
            padding: 20px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            min-height: 100vh;
        }
        .container {
            background: rgba(255,255,255,0.1);
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
        }
        h1 { color: #ffd700; text-align: center; }
        .subtitle { text-align: center; opacity: 0.8; margin-bottom: 40px; }
        .posts-section {
            margin-top: 30px;
        }
        .section-title {
            color: #ffd700;
            font-size: 1.5em;
            margin-bottom: 20px;
            text-align: center;
        }
        .post-card {
            background: rgba(255,255,255,0.1);
            padding: 20px;
            margin-bottom: 20px;
            border-radius: 8px;
            border-left: 4px solid #ffd700;
        }
        .post-card h3 {
            margin: 0 0 10px 0;
        }
        .post-card a {
            color: #ffd700;
            text-decoration: none;
        }
        .post-card a:hover {
            text-decoration: underline;
        }
        .post-date {
            opacity: 0.7;
            font-size: 0.9em;
            margin: 0 0 10px 0;
        }
        .post-excerpt {
            margin: 0;
            line-height: 1.5;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Guest in the Universe</h1>
        <p class="subtitle">Exploring the vast cosmos of web development</p>
        
        <div class="posts-section">
            <h2 class="section-title">Latest Posts</h2>
            ''' + posts_html + '''
        </div>
    </div>
</body>
</html>
    ''')
