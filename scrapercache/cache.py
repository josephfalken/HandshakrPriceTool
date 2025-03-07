# cache.py
# scrapercache module
# Our initial implementation is a simple Python in-memory dictionary.
# To scale this, we would replace with a NoSQL key/value store database like Redis.

import datetime

expiration_interval = datetime.timedelta(days=1)
cache_dict = dict()

# See if the cache contains 'query' request
# Returns None if it doesn't or it was expired
# Returns cached data if it was cached
# If entry exists but was expired, it is removed.
def lookup(query):
    global cache_dict
    if query in cache_dict:
        entry = cache_dict[query]
        # Make sure this cache entry hasn't expired
        # (first part of tuple is the cached date)
        if entry[0] + expiration_interval > datetime.datetime.now():
            # Return the cached entry
            return cache_dict[query][1] # second part of tuple is the cached value
        else:
            # Remove the expired entry
            del cache_dict[query]
    return None

# Add an entry to the cache
# Overwrite any existing entry
# (usually won't happen since we check cache first)
def add_to_cache(query, value):
    global cache_dict
    entry = (datetime.datetime.now(), value)
    cache_dict[query] = entry

# Return the cache contents for debugging/diagnosis
def enumerate_cache():
    # Just return the underlying dictionary itself
    global cache_dict
    return cache_dict

# Clear the cache
def clear_cache():
    global cache_dict
    cache_dict.clear()
