# Python version of articles.rb

from sys import argv
from re import search

for line in file(argv[1]):
    r = search(r'GET /ongoing/When/\d\d\dx/(\d\d\d\d/\d\d/\d\d/[^ .]+)', line)
    if r:
        print r.groups()[0]
