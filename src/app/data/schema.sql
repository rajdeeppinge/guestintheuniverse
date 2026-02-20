-- Guest in the Universe Blog Database Schema

-- Posts table
CREATE TABLE IF NOT EXISTS posts (
    id TEXT PRIMARY KEY,
    slug TEXT UNIQUE NOT NULL,
    title TEXT NOT NULL,
    author TEXT DEFAULT 'NoviceGuru',
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    published BOOLEAN DEFAULT 1
);

-- Indexes for better performance
CREATE INDEX IF NOT EXISTS idx_posts_slug ON posts(slug);
CREATE INDEX IF NOT EXISTS idx_posts_created_at ON posts(created_at);
CREATE INDEX IF NOT EXISTS idx_posts_published ON posts(published);
