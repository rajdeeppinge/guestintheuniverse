from flask import Blueprint, jsonify, request
from services.post_service import PostService
from services.unit_conversion_service import UnitConversionService
import os
import markdown

api_bp = Blueprint('api', __name__, url_prefix='/api/v1')
post_service = PostService()
unit_conversion_service = UnitConversionService()

@api_bp.route('/health')
def health():
    return jsonify({
        'status': 'healthy',
        'service': 'guestintheuniverse'
    })

@api_bp.route('/stats')
def api_stats():
    return {
        'app': 'Guest in the Universe',
        'status': 'running',
        'tech': ['Flask', 'Docker', 'Nginx', 'Ansible']
    }

@api_bp.route('/posts')
def api_posts():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    
    posts = post_service.get_latest_posts(per_page, (page - 1) * per_page)
    total_posts = post_service.get_total_posts_count()
    
    return jsonify({
        'posts': posts,
        'pagination': {
            'page': page,
            'per_page': per_page,
            'total': total_posts,
            'pages': (total_posts + per_page - 1) // per_page
        }
    })

# API to get posts by filename
@api_bp.route('/posts/<filename>')
def api_post(filename):
    post = post_service.get_post_by_filename(filename)
    if post is None:
        return jsonify({'error': 'Post not found'}), 404
    return jsonify(post)

# API to get about content
@api_bp.route('/about')
def api_about():
    # Read about content from markdown file
    about_path = os.path.join(os.path.dirname(__file__), '..', 'content', 'about.md')
    if not os.path.exists(about_path):
        return jsonify({'error': 'About content not found'}), 404
    
    with open(about_path, 'r', encoding='utf-8') as f:
        about_content = f.read()
    
    # Convert markdown to HTML
    about_html = markdown.markdown(about_content)
    
    return jsonify({
        'content': about_html
    })

@api_bp.route('/convert', methods=['POST'])
def api_convert():
    """Unit conversion API endpoint"""
    data = request.get_json()
    
    if not data:
        return jsonify({'error': 'No data provided'}), 400
    
    value = data.get('value')
    from_unit = data.get('from_unit')
    to_unit = data.get('to_unit')
    category = data.get('category')
    
    if value is None or not from_unit or not to_unit or not category:
        return jsonify({'error': 'Missing required parameters'}), 400
    
    try:
        value = float(value)
    except ValueError:
        return jsonify({'error': 'Invalid value'}), 400
    
    result = unit_conversion_service.convert(value, from_unit, to_unit, category)
    
    if 'error' in result:
        return jsonify(result), 400
    
    return jsonify(result)

@api_bp.route('/units')
def api_units():
    """Get available unit categories and units"""
    return jsonify(unit_conversion_service.get_available_units())
