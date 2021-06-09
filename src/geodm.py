#!/usr/bin/env python3

import sys
import argparse 
import requests
import re
import time

from concurrent.futures import ThreadPoolExecutor
from parser import FileParser

FILE = sys.argv[1]
REGEX = re.compile(r'(!Series_supplementary_file\s+")(\w+:/.+)"')

def from_series(file_url):

    file2download = file_url.strip().split('/')[-1]
    print(f'\n...Downloading {file2download}')

    with open(file2download, 'wb' ) as file:
        r = requests.get(file_url)
        file.write(r.content)
        print('DONE')

fp = FileParser(FILE, REGEX)
urls = fp.get_urls()

st = time.perf_counter()

with ThreadPoolExecutor() as executor:
    executor.map(from_series, urls)

et = time.perf_counter()

print(f'Finished in {round(et-st, 2)} seconds')

