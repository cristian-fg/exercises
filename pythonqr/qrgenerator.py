#!/usr/bin/python3

import pyqrcode

url = pyqrcode.create("https://github.com/cristian-fg")
url.svg('uca-url.sgv', scale=8)
print(url.terminal(quiet_zone=1))