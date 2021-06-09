#!/usr/bin/env python3

import argparse 
from pathlib import Path

class SeriesFile():

    def __init__(self, file):
        self.file = file.upper()

    def print_string(self):
        print(self.file)


if __name__ == '__main__':
    series_file = SeriesFile('lowercase')
    series_file.print_string()


