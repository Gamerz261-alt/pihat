#!/usr/bin/env python 3

import sys

if sys.srgc < 2:
     string = "world"
else:
     string = sys.argv[1]

print("hello {}!".format(string))
