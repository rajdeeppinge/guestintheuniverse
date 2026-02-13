from flask import Blueprint, jsonify
from services.post_service import PostService

api_bp = Blueprint('api', __name__, url_prefix='/api/v1')
post_service = PostService()

@api_bp.route('/health')
def health():
    return jsonify({
        'status': 'healthy',
        'service': 'guestintheuniverse',
        'version': 'v0.1.0-dev1'
    })

@api_bp.route('/stats')
def api_stats():
    return {
        'app': 'Guest in the Universe',
        'version': 'v0.1.0-dev1',
        'status': 'running',
        'tech': ['Flask', 'Docker', 'Nginx', 'Ansible']
    }

@api_bp.route('/posts')
def api_posts():
    posts = post_service.get_latest_posts(10)
    return jsonify({
        'posts': posts,
        'count': len(posts)
    })
