#!/usr/bin/env python3

import re
import sys 

class FileParser:

    def __init__(self, file, regex):
        self.file = file
        self.regex = regex

    def get_urls(self):
        urls = []
        with open(self.file) as file:
            for line in file:
                matches = self.regex.finditer(line.strip())
                for match in matches:
                    filepath = match.group(2)
                    urls.append(filepath.replace('ftp://', 'http://'))
        return urls

    def get_metadata(self):
        pass

    def __str__(self):
        return f'FileParser object for file {self.file} and regex {self.regex}'
