#!/bin/python3
from datetime import datetime, timedelta
import math
import os
import random
import re
import sys

# Complete the time_delta function below.
def time_delta(t1, t2):
    datetime_format="%a %d %b %Y %H:%M:%S %z"
    time1=datetime.strptime(t1, datetime_format)
    time2=datetime.strptime(t2,datetime_format)
    time_diff=abs(int((time1-time2).total_seconds()))
    return str(time_diff)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()
