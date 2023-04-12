#!/usr/bin/python3
"""
A python script that fetches
https://alx-intranet.hbtn.io/status
"""

if __name__ == "__main__":
    import requests
    url = 'https://alx-intranet.hbtn.io/status'
    r = requests.get(url).text
    print("Body response:")
    print("\t- type: {}".format(type(r)))
    print("\t- content: {}".format(r))
