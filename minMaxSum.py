import math
import os
import random
import re
import sys

def miniMaxSum(arr):
    arr.sort()
    minSum=arr[:-1]
    maxsum=arr[1:]
    print(sum(minSum),sum(maxsum))

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))
    miniMaxSum(arr)
