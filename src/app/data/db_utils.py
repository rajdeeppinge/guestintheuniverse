import sqlite3
import os
import uuid
from datetime import datetime
from typing import List, Dict, Optional

# Database path from environment or default
DATABASE_PATH = os.getenv('DATABASE_PATH', '/app/data/guestintheuniverse.db')

def get_db_connection():
    """Get a database connection."""
    conn = sqlite3.connect(DATABASE_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_database():
    """Initialize the database with schema."""
    conn = get_db_connection()
    schema_path = os.path.join(os.path.dirname(__file__), 'schema.sql')
    
    with open(schema_path, 'r') as f:
        schema = f.read()
    
    conn.executescript(schema)
    conn.commit()
    conn.close()

def get_post_by_id(post_id: str) -> Optional[Dict]:
    """Get post by UUID."""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM posts WHERE id = ?', (post_id,))
    result = cursor.fetchone()
    
    conn.close()
    return dict(result) if result else None

def get_post_by_slug(slug: str) -> Optional[Dict]:
    """Get post by slug."""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM posts WHERE slug = ?', (slug,))
    result = cursor.fetchone()
    
    conn.close()
    return dict(result) if result else None

def add_post(slug: str, title: str, created_at: Optional[str] = None, published: bool = True) -> str:
    """Add a new post with UUID primary key."""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    post_id = str(uuid.uuid4())
    
    if created_at is None:
        created_at = datetime.now().isoformat()
    
    cursor.execute('''
        INSERT INTO posts (id, slug, title, created_at, published)
        VALUES (?, ?, ?, ?, ?)
    ''', (post_id, slug, title, created_at, published))
    
    success = cursor.rowcount > 0
    conn.commit()
    conn.close()
    
    return post_id if success else None

def get_all_posts(published_only: bool = True) -> List[Dict]:
    """Get all posts."""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    query = 'SELECT * FROM posts'
    if published_only:
        query += ' WHERE published = 1'
    
    query += ' ORDER BY created_at DESC'
    
    cursor.execute(query)
    results = cursor.fetchall()
    
    conn.close()
    return [dict(row) for row in results]
