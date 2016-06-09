"""
Basic default environment agnostic configuration variables

author: @abekim
"""

from blogger.json_encoder import MongoEngineJSONEncoder

CACHE_THRESHOLD = 1000

# Default mongoDB JSON encoder has a bug encoding documents
JSON_ENCODER = MongoEngineJSONEncoder
