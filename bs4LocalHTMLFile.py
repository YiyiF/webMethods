#! /usr/bin/env python3

import bs4, logging

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')

exampleFile = open('example.html')
exampleSoup = bs4.BeautifulSoup(exampleFile)
elems = exampleSoup.select('#author')
logging.debug('Type of exampleSoup.select: %s.' % type(elems))
logging.debug('Length of exampleSoup.select: %s.' % len(elems))
logging.debug('Type of exampleSoup.select.elements: %s.' % type(elems[0]))
print('The author is %s. (Through bs4.select.getText)' % elems[0].getText())
print('The author is %s. (Through str.bs4.select)' % str(elems[0]))
print('The attribution is %s.' % elems[0].attrs)