import math
import os
import random
import re
import sys
def plusMinus(arr):
    p=0
    ne=0
    z=0
    # Write your code here
    for i in arr:
        if i<0 :
            ne+=1
        elif i==0:
            z+=1
        else:
            p+=1
            
    
    print(f"{p/n : .6f}")
    print(f"{ne/n : .6f}")
    print(f"{z/n : .6f}")
            
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
