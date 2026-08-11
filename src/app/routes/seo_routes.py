from flask import Blueprint, Response, current_app, request, url_for
from datetime import datetime
import xml.etree.ElementTree as ET
from urllib.parse import urljoin

seo_bp = Blueprint('seo', __name__)

@seo_bp.route('/rss.xml')
def rss_feed():
    """Generate RSS 2.0 feed for blog posts"""
    with current_app.test_client() as client:
        # Get first page with all posts (high per_page)
        posts_response = client.get('/api/v1/posts?page=1&per_page=50')
        posts_data = posts_response.get_json()
        posts = posts_data.get('posts', [])
    
    # Create RSS XML
    rss = ET.Element('rss')
    rss.set('version', '2.0')
    
    channel = ET.SubElement(rss, 'channel')
    
    # Channel elements
    ET.SubElement(channel, 'title').text = 'Guest in the Universe'
    ET.SubElement(channel, 'description').text = 'A blog exploring the vastness of our universe through technology, philosophy, and digital experiences.'
    ET.SubElement(channel, 'link').text = url_for('main.index', _external=True)
    
    # Get base URL for post links
    base_url = request.host_url.rstrip('/')
    
    # Add posts as items
    for post in posts:
        item = ET.SubElement(channel, 'item')
        
        # Title
        title = post.get('title', 'Untitled')
        ET.SubElement(item, 'title').text = title
        
        # Link
        filename = post.get('filename', '')
        post_url = f"{base_url}/post/{filename}"
        ET.SubElement(item, 'link').text = post_url
        
        # Description (first 200 chars of content)
        content = post.get('content', '')
        description = content[:200] + '...' if len(content) > 200 else content
        ET.SubElement(item, 'description').text = description
        
        # Pub date
        date_str = post.get('date', '')
        if date_str:
            try:
                # Parse date from YYYY-MM-DD format
                pub_date = datetime.strptime(date_str, '%Y-%m-%d')
                ET.SubElement(item, 'pubDate').text = pub_date.strftime('%a, %d %b %Y %H:%M:%S +0000')
            except:
                pass
        
        # GUID
        ET.SubElement(item, 'guid').text = post_url
    
    # Generate XML string
    xml_str = ET.tostring(rss, encoding='utf-8', xml_declaration=True)
    
    return Response(xml_str, mimetype='application/rss+xml')

@seo_bp.route('/sitemap.xml')
def sitemap():
    """Generate XML sitemap for SEO"""
    with current_app.test_client() as client:
        # Get all posts
        posts_response = client.get('/api/v1/posts?page=1&per_page=50')
        posts_data = posts_response.get_json()
        posts = posts_data.get('posts', [])
    
    # Create sitemap XML
    urlset = ET.Element('urlset')
    urlset.set('xmlns', 'http://www.sitemaps.org/schemas/sitemap/0.9')
    
    # Get base URL
    base_url = request.host_url.rstrip('/')
    
    # Add main pages
    main_pages = [
        {'loc': f'{base_url}/', 'priority': '1.0'},
        {'loc': f'{base_url}/about', 'priority': '0.8'},
    ]
    
    for page in main_pages:
        url = ET.SubElement(urlset, 'url')
        ET.SubElement(url, 'loc').text = page['loc']
        ET.SubElement(url, 'priority').text = page['priority']
    
    # Add posts
    for post in posts:
        url = ET.SubElement(urlset, 'url')
        
        filename = post.get('filename', '')
        post_url = f"{base_url}/post/{filename}"
        ET.SubElement(url, 'loc').text = post_url
        
        # Last modified date
        date_str = post.get('date', '')
        if date_str:
            try:
                lastmod = datetime.strptime(date_str, '%Y-%m-%d')
                ET.SubElement(url, 'lastmod').text = lastmod.strftime('%Y-%m-%d')
            except:
                pass
        
        ET.SubElement(url, 'priority').text = '0.6'
    
    # Generate XML string
    xml_str = ET.tostring(urlset, encoding='utf-8', xml_declaration=True)
    
    return Response(xml_str, mimetype='application/xml')
