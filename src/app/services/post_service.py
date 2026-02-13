import os
import re
from datetime import datetime

class PostService:
    def __init__(self):
        self.posts_dir = "/home/shodh/software_engineering/universe_blog/_posts"
    
    def get_latest_posts(self, limit=10):
        """Get latest posts from universe_blog"""
        posts = []
        
        if os.path.exists(self.posts_dir):
            for filename in sorted(os.listdir(self.posts_dir), reverse=True)[:limit]:
                if filename.endswith('.md'):
                    filepath = os.path.join(self.posts_dir, filename)
                    with open(filepath, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    # Extract frontmatter
                    frontmatter_match = re.match(r'^---\n(.*?)\n---\n(.*)$', content, re.DOTALL)
                    if frontmatter_match:
                        frontmatter, body = frontmatter_match.groups()
                        
                        # Parse title and date from frontmatter
                        title = "Untitled"
                        date = filename[:10]  # Extract date from filename
                        
                        for line in frontmatter.split('\n'):
                            if line.startswith('title:'):
                                title = line.split(':', 1)[1].strip().strip('"\'')
                            elif line.startswith('date:'):
                                date = line.split(':', 1)[1].strip()
                        
                        # Get first 150 characters of content as excerpt
                        excerpt = body.strip()[:150] + "..." if len(body.strip()) > 150 else body.strip()
                        
                        posts.append({
                            'title': title,
                            'date': date,
                            'excerpt': excerpt,
                            'filename': filename
                        })
        
        return posts
