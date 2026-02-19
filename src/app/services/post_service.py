import os
import re
import urllib.parse
import markdown
from datetime import datetime

class PostService:
    def __init__(self):
        self.posts_dir = "/posts"
    
    def get_total_posts_count(self):
        """Get total number of posts"""
        if not os.path.exists(self.posts_dir):
            return 0
        
        return len([f for f in os.listdir(self.posts_dir) if f.endswith('.md')])
    
    def format_date(self, date_str):
        """Format date string to DD month YYYY format"""
        try:
            # Try to parse the date string - it could be in various formats
            # Common formats: YYYY-MM-DD, DD/MM/YYYY, etc.
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
        """Get a specific post by filename"""
        filepath = os.path.join(self.posts_dir, filename)
        
        if not os.path.exists(filepath) or not filename.endswith('.md'):
            return None
        
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extract frontmatter
        frontmatter_match = re.match(r'^---\n(.*?)\n---\n(.*)$', content, re.DOTALL)
        if frontmatter_match:
            frontmatter, body = frontmatter_match.groups()
            
            # Parse title, date, and author from frontmatter
            title = "Untitled"
            date = filename[:10]  # Extract date from filename
            author = "NoviceGuru"  # Default author
            
            for line in frontmatter.split('\n'):
                if line.startswith('title:'):
                    title = line.split(':', 1)[1].strip().strip('"\'')
                elif line.startswith('date:'):
                    date = line.split(':', 1)[1].strip()
                elif line.startswith('author:'):
                    author = line.split(':', 1)[1].strip().strip('"\'')
            
            # Calculate read time and extract image
            read_time = self.calculate_read_time(body)
            image = self.extract_image_from_content(content)
            
            # Format the date
            formatted_date = self.format_date(date)
            
            # Convert markdown to HTML
            html_content = markdown.markdown(body, extensions=['extra', 'codehilite'])
            
            return {
                'title': title,
                'date': formatted_date,
                'author': author,
                'content': html_content,
                'filename': filename,
                'read_time': read_time,
                'image': image
            }
        
        return None
    
    def get_latest_posts(self, limit=10, offset=0):
        """Get latest posts from with pagination"""
        posts = []
        
        if os.path.exists(self.posts_dir):
            all_files = [f for f in os.listdir(self.posts_dir) if f.endswith('.md')]
            sorted_files = sorted(all_files, reverse=True)[offset:offset + limit]
            
            for filename in sorted_files:
                filepath = os.path.join(self.posts_dir, filename)
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Extract frontmatter
                frontmatter_match = re.match(r'^---\n(.*?)\n---\n(.*)$', content, re.DOTALL)
                if frontmatter_match:
                    frontmatter, body = frontmatter_match.groups()
                    
                    # Parse title, date, and author from frontmatter
                    title = "Untitled"
                    date = filename[:10]  # Extract date from filename
                    author = "NoviceGuru"  # Default author
                    
                    for line in frontmatter.split('\n'):
                        if line.startswith('title:'):
                            title = line.split(':', 1)[1].strip().strip('"\'')
                        elif line.startswith('date:'):
                            date = line.split(':', 1)[1].strip()
                        elif line.startswith('author:'):
                            author = line.split(':', 1)[1].strip().strip('"\'')
                    
                    # Get first 150 characters of content as excerpt
                    excerpt = body.strip()[:150] + "..." if len(body.strip()) > 150 else body.strip()
                    
                    # Calculate read time and extract image
                    read_time = self.calculate_read_time(body)
                    image = self.extract_image_from_content(content)
                    
                    # Format the date
                    formatted_date = self.format_date(date)
                    
                    posts.append({
                        'title': title,
                        'date': formatted_date,
                        'author': author,
                        'excerpt': excerpt,
                        'filename': filename,
                        'read_time': read_time,
                        'image': image
                    })
        
        return posts
