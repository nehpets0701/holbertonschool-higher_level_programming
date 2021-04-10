#!/usr/bin/python3
"""error code"""
import urllib.request
import urllib.parse
from sys import argv

if __name__ == "__main__":
    if len(argv) == 2:
        url = argv[1]
        try:
            with urllib.request.urlopen(url) as response:
                html = response.read()
                print(html.decode("utf-8"))
        except Exception as e:
            print("Error code: " + str(e.code))
