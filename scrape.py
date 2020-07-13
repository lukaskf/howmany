#Heavily leveraged https://realpython.com/python-web-scraping-practical-introduction/
"""
Key functions for webscrapping
"""

from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup


def simple_get(url):
    """
    Attempts to get content a `url`.
    """
    try:
        with closing(get(url, stream=True)) as resp:
            if is_good_response(response):
                return resp.content
            else:
                return None
    except RequestException as e:
        log_error('Error durring requests to {0} : {1}'.format(url, str(e)))
        return None

def is_good_response(resp):
    """
    Returns True if response is HTML
    """
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200
            and content_type is not None
            and content_type.find('html') > -1)

def log_error(e):
    """ 
    Prints error messages
    """
    print(e)