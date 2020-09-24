#!/bin/python

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    sock_pair = {}
    pairs=0
    for color in ar:
        if(color in sock_pair):
            if(sock_pair[color]==True):
                pairs= pairs+1
            sock_pair[color]= not sock_pair[color]
        else:
            sock_pair[color]= True
    return pairs
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    ar = map(int, raw_input().rstrip().split())

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
