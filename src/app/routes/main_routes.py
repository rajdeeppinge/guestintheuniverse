from flask import Blueprint, render_template, current_app, request, send_from_directory
from datetime import datetime
import os
import markdown

main_bp = Blueprint('main', __name__)

@main_bp.route('/images/<path:filename>')
def serve_image(filename):
    """Serve static images"""
    images_dir = "/images"
    return send_from_directory(images_dir, filename)

@main_bp.route('/')
@main_bp.route('/page/<int:page>')
def index(page=1):
    # Use API endpoint instead of directly accessing service
    with current_app.test_client() as client:
        posts_response = client.get(f'/api/v1/posts?page={page}&per_page=5')
        posts_data = posts_response.get_json()
        posts = posts_data.get('posts', [])
        pagination = posts_data.get('pagination', {})
    
    return render_template('index.html', posts=posts, pagination=pagination, current_year=datetime.now().year)

@main_bp.route('/post/<filename>')
def post(filename):
    # Use API endpoint instead of directly accessing service
    with current_app.test_client() as client:
        post_response = client.get(f'/api/v1/posts/{filename}')
        if post_response.status_code == 404:
            return "Post not found", 404
        post_data = post_response.get_json()
    
    return render_template('post.html', post=post_data, current_year=datetime.now().year)

@main_bp.route('/about')
def about():
    # Use API endpoint to get about content
    with current_app.test_client() as client:
        about_response = client.get('/api/v1/about')
        if about_response.status_code == 404:
            return "About content not found", 404
        about_data = about_response.get_json()
        about_content = about_data.get('content', '')
    
    return render_template('about.html', about_content=about_content, current_year=datetime.now().year)
