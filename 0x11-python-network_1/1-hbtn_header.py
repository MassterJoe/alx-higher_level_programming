#!/usr/bin/python3
"""
A python script that takes a url
sends a request to the url and displays
value of the x-request-Id vairiable found
in the header of the response
"""
if __name__ == "__main__":
    import urllib.request
    import sys
    url = sys.argv[1]
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        result = dict(response.headers).get("X-Request-Id")
        print(result)

