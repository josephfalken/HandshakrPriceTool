# authentication.py
# scraperauthentication module

import os
import random
import string
from requests import Request

bypass_authentication = False
token_file = os.path.expanduser("~/.scraper/tokens") # File containing our tokens, one per line
token_set = set() # Set that will hold the tokens for lookup

# Create a token in the format we use. (Call if you need to make a new token.)
def create_token():
    return ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(100))

# Read the tokens from disk into the tokenSet
def initialize_if_needed():
    global token_set
    if len(token_set) != 0:
        return
    with open(token_file) as f:
        tokens = f.readlines()
    tokens = [i.strip('\n') for i in tokens] # Remove trailing \n
    token_set = set(tokens)

# Return true if this token signifies authorization, false otherwise
def is_authorized_token(token):
    initialize_if_needed()
    return token in token_set

# Return true if this Request from Python requests package is authorized, false otherwise
def is_authorized_request(request: Request ):
    global bypass_authentication
    if bypass_authentication:
        return True
    if not 'Authorization' in request.headers:
        return False
    return is_authorized_token(request.headers['Authorization'])

def add_test_token(token):
    global token_set
    token_set.add(token)