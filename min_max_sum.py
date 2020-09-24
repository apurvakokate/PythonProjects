#!/bin/python3

import os
import sys

#
# Complete the miniMaxSum function below.
#
def miniMaxSum(arr):
    #
    # Write your code here.
    #
    min = sys.maxsize;
    max = -sys.maxsize -1;
    for index, _ in enumerate(arr):
        total = sum([x for i,x in enumerate(arr) if i!=index])
        if total<min : min=total
        if total>max : max=total
    print ("{} {}".format(min,max))

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
