#!/usr/bin/python
import sys

for line in sys.stdin:
        data = line.strip().split(",")
        if len(data) == 8:
                a1,a2,a3,a4,a5,a6,a7,a8 = data
                print "{0}\t{1}".format(a7,1)
