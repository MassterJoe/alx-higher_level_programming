#!/usr/bin/python3
"""
A script that takes in a URL and
an email, sends a POST request to
passed URL with email as a parameter and
displays the body of the respose decoded in
utf-8
"""

if __name__ == "__main__":
    import urllib.request
    import urllib.parse
    import sys
    url = sys.argv[1]
    email = sys.argv[2]
    value = {'email': email}
    data = urllib.parse.urlencode(value)
    data = data.encode("ascii")
    req = urllib.request.Request(url, data)

    with urllib.request.urlopen(req) as response:
        content = response.read()
        print(content.decode("utf-8"))
