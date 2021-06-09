#!/usr/bin/env python3

import sys
import argparse 
import requests

from pathlib import Path

script_args = sys.argv[:]

def main():
    for arg in script_args:
        response = requests.get()


if __name__ == '__main__':
    main()

