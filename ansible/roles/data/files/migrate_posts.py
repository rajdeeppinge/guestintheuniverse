#!/usr/bin/env python3
"""
Migrate existing markdown posts to database
"""

import sys
import os
import re
from datetime import datetime

# Add the data directory to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../../../../src/app/data'))

from db_utils import add_post, get_post_by_slug

def extract_title_from_frontmatter(content):
    """Extract title from markdown frontmatter"""
    frontmatter_match = re.match(r'^---\n(.*?)\n---\n(.*)$', content, re.DOTALL)
    if frontmatter_match:
        frontmatter, body = frontmatter_match.groups()
        
        for line in frontmatter.split('\n'):
            if line.startswith('title:'):
                return line.split(':', 1)[1].strip().strip('"\'')
    
    # Fallback to filename
    return "Untitled"

def extract_date_from_filename(filename):
    """Extract date from filename (YYYY-MM-DD format)"""
    if len(filename) >= 10 and filename[4] == '-' and filename[7] == '-':
        return filename[:10]
    return datetime.now().strftime('%Y-%m-%d')

def migrate_posts():
    """Migrate existing markdown posts to database"""
    posts_dir = os.path.join(os.path.dirname(__file__), '../../../../posts')  # Relative path to posts
    
    if not os.path.exists(posts_dir):
        print(f"Posts directory {posts_dir} not found")
        return
    
    md_files = [f for f in os.listdir(posts_dir) if f.endswith('.md')]
    print(f"Found {len(md_files)} markdown files")
    
    migrated = 0
    skipped = 0
    
    for filename in md_files:
        # Extract slug from filename (remove .md extension)
        slug = filename[:-3]  # Remove .md extension
        
        # Check if already exists
        existing = get_post_by_slug(slug)
        if existing:
            print(f"Skipping {slug} - already exists")
            skipped += 1
            continue
        
        # Read markdown file
        filepath = os.path.join(posts_dir, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extract metadata
        title = extract_title_from_frontmatter(content)
        created_at = extract_date_from_filename(filename)
        
        # Add to database
        post_id = add_post(slug, title, created_at, published=True)
        if post_id:
            print(f"Migrated: {slug} -> {title}")
            migrated += 1
        else:
            print(f"Failed to migrate: {slug}")
    
    print(f"Migration complete: {migrated} migrated, {skipped} skipped")

if __name__ == '__main__':
    migrate_posts()
