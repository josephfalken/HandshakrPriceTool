from flask import Flask
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')
def hello():
    r = requests.get('https://google.com')
    soup = BeautifulSoup(r.text)
    navLinks = soup.find_all("a", class_ = "gb1")
    return str(navLinks)