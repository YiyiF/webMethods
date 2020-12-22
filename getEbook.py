#! /usr/bin/env python3

import requests

res = requests.get('http://www.gutenberg.org/cache/epub/1112/pg1112.txt')
try:
    res.raise_for_status()
    bookFile = open('RomeoAndJuliet.txt', 'wb')
    for chunk in res.iter_content(100):
        bookFile.write(chunk)
    bookFile.close()
except Exception as exc:
    print('There was a problem: %s' % (exc))