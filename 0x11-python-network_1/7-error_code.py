#!/usr/bin/python3
"""
A python script that takes in a URL, sends a request
to the URL and displays the body of the response
"""

if __name__ == "__main__":
    import requests
    import sys

    url = sys.argv[1]
    try:
        r = requests.get(url).text
    except requests.exceptions.HTTPError as e:
        if e.code >= 400:
            print("Error code: {}".format(e.code))
