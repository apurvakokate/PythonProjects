#!/bin/python

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    altitude=0
    start_valley = False
    valleys=0
    for step in s:
        if step=='U':
            altitude = altitude+1
        if step=='D':
            if altitude==0:
                start_valley=True
            altitude=altitude-1
        if altitude==0 and start_valley==True:
            start_valley=False
            valleys = valleys+1
    return valleys

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    s = raw_input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
