#!/usr/bin/env python3
"""
Initialize database schema
"""

import sys
import os

# Add the data directory to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../../../../src/app/data'))

from db_utils import init_database

if __name__ == '__main__':
    init_database()
    print('Database schema initialized')
