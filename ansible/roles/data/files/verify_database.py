#!/usr/bin/env python3
"""
Verify database setup
"""

import sys
import os

# Add the data directory to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../../../../src/app/data'))

from db_utils import get_all_posts

if __name__ == '__main__':
    posts = get_all_posts()
    print(f'Database verification: {len(posts)} posts ready')
