#!/usr/bin/python
import sys
Total = 0
oldKey = None
MaxKey=None
MinKey=None
MaxCount=0
MinCount=999999999
for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        continue
    Key,Value = data_mapped
    if oldKey and oldKey != Key:
        print oldKey, "\t",Total
        if MaxCount<Total:
            MaxCount=Total
            MaxKey=oldKey
        if MinCount>Total:
            MinCount=Total
            MinKey=oldKey
        Total = 0
        oldKey=Key

    oldKey = Key
    Total += float(Value)
if MaxCount<Total:
    MaxCount=Total
    MaxKey=oldKey
if MinCount>Total:
        MinCount=Total
        MinKey=oldKey
if oldKey != None:
    print oldKey, "\t",Total
    print "MAX:",MaxKey, "\t",MaxCount
    print "MIN:",MinKey, "\t",MinCount
