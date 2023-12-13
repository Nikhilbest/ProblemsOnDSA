#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'reverse' function below.
#
# The function accepts STRING st as parameter.
#

def reverse(st):
    # Write your code here
    size = len(st)
    if size == 0:
        return
    print(st[size-1:], end='')
    reverse(st[:size-1])

if __name__ == '__main__':
    st = input()

    reverse(st)
