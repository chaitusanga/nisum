#!/usr/bin/env python

import re

#file = open("abc.txt", "r")

for line in open('abc.txt'):
    if re.match("[zeus_creative_recycles]", line):
        print line

