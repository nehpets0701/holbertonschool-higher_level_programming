#!/usr/bin/python3
""" Task 4 """
import requests

if __name__ == "__main__":
    url = "https://intranet.hbtn.io/status"
    r = requests.get(url)
    print("Body response:")
    print("\t- type: " + str(type(r.text)))
    print("\t- content: " + str(r.text))
