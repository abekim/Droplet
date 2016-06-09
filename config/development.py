"""
The Development Configuration

- provides default database for the application
- enables debug mode
- disables cache

author: @abekim
"""

DEBUG = True

# Null cache-type means no cache
CACHE_TYPE = 'null'
CACHE_DEFAULT_TIMEOUT = 24*60*60

# Dev database
MONGODB_SETTINGS = {
    "DB": "BlogWarehouse"
}
