import os
import re
import markdown
from datetime import datetime
from data.db_utils import get_post_by_slug, add_post, get_all_posts

class PostService:
    def __init__(self):
        self.posts_dir = "/posts"
    
    def get_total_posts_count(self):
        """Get total number of posts"""
        posts = get_all_posts(published_only=True)
        return len(posts)
    
    def format_date(self, date_str):
        """Format date string to DD month YYYY format"""
        try:
            # Try to parse date string
            if '-' in date_str:
                # Try YYYY-MM-DD format first
                parts = date_str.split('-')
                if len(parts) == 3 and parts[0].isdigit() and len(parts[0]) == 4:
                    year, month, day = parts
                    month_names = ['January', 'February', 'March', 'April', 'May', 'June',
                                 'July', 'August', 'September', 'October', 'November', 'December']
                    month_name = month_names[int(month) - 1] if month.isdigit() else month
                    return f"{int(day)} {month_name} {year}"
            elif '/' in date_str:
                # Try DD/MM/YYYY format
                parts = date_str.split('/')
                if len(parts) == 3:
                    day, month, year = parts
                    month_names = ['January', 'February', 'March', 'April', 'May', 'June',
                                 'July', 'August', 'September', 'October', 'November', 'December']
                    month_name = month_names[int(month) - 1] if month.isdigit() else month
                    return f"{int(day)} {month_name} {year}"
            
            # If parsing fails, return original string
            return date_str
        except:
            return date_str
    
    def calculate_read_time(self, content):
        """Calculate estimated read time in minutes"""
        words_per_minute = 200  # Average reading speed
        word_count = len(content.split())
        read_time = max(1, round(word_count / words_per_minute))
        return read_time
    
    def extract_image_from_content(self, content):
        """Extract image references from content"""
        # Look for Jekyll image frontmatter or local markdown images
        image_patterns = [
            r'image:\s*(.+)',
            r'!\[.*?\]\(([^h][^t][^t][^p][^s]?:.+)\)',  # Local images (not http/https)
            r'<img[^>]+src=["\']([^"\']+)["\']'
        ]
        
        for pattern in image_patterns:
            match = re.search(pattern, content, re.IGNORECASE)
            if match:
                image_path = match.group(1).strip()
                # Clean up the image path
                if image_path.startswith('/images/'):
                    image_path = image_path[8:]  # Remove '/images/' prefix
                return image_path
        
        return None
    
    def get_post_by_filename(self, filename):
        """Get a specific post by filename (slug)"""
        # Convert filename to slug (remove .md extension)
        slug = filename.replace('.md', '') if filename.endswith('.md') else filename
        post_metadata = get_post_by_slug(slug)
        
        if post_metadata is None:
            return None
        
        # Read content from markdown file
        filepath = os.path.join(self.posts_dir, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
            # Convert markdown to HTML
        html_content = markdown.markdown(content, extensions=['extra', 'codehilite'])
            
        return {
            'title': post_metadata['title'],
            'date': self.format_date(post_metadata['created_at'][:10]),  # Extract date part
            'author': post_metadata['author'],
            'content': html_content,
            'filename': filename,
            'read_time': self.calculate_read_time(content),
            'image': self.extract_image_from_content(content)
        }
    
    def get_latest_posts(self, limit=10, offset=0):
        """Get latest posts from database"""
        posts = get_all_posts(published_only=True)
        
        # Apply pagination
        paginated_posts = posts[offset:offset + limit]
        
        result_posts = []
        for post in paginated_posts:
            # Read content from markdown file
            filename = f"{post['slug']}.md"
            filepath = os.path.join(self.posts_dir, filename)
            
            content = ""
            if os.path.exists(filepath):
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                    
                    # Get first 150 characters of content as excerpt
            excerpt = content.strip()[:150] + "..." if len(content.strip()) > 150 else content.strip()
            
            result_posts.append({
                'title': post['title'],
                'date': self.format_date(post['created_at'][:10]),  # Extract date part
                'author': post['author'],
                'excerpt': excerpt,
                'filename': filename,
                'read_time': self.calculate_read_time(content),
                'image': self.extract_image_from_content(content)
            })
        
        return result_posts
