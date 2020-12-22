#! /usr/bin/env python3

import sys, requests, webbrowser, bs4

print('Googling...')
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}
res = requests.get(url='https://google.com/search?q=' + ' '.join(sys.argv[1:]), headers=headers)
try:
    res.raise_for_status()
    # Retrieve top search result links.
    resultSoup = bs4.BeautifulSoup(res.text, features='html.parser')
    # Open a browser tab for each result.
    linkElems = resultSoup.select('.yuRUbf a')
    numOpen = min(5, len(linkElems))
    for i in range(numOpen):
        try:
            print('=== Search results: %s' % str(linkElems[i].get('href')))
            webbrowser.open(linkElems[i].get('ping'))
        except Exception as whichUrlError:
            print('=== The website %s had a problem.' % whichUrlError)
except Exception as exc:
    print('=== There was a problem: %s' % exc)