# copyright Max Osterried, ETHZ, 21.05.2022

import sys


#############
def vis(ein):
    # init vars
    xor = ein[0]
    for i in range(1, len(ein)):
        xor ^= ein[i]

    return min(xor ^ ein[i] for i in range(0, len(ein)))


#############
input = sys.stdin.readline
n = int(input())

# for _ in range(n):
input = sys.stdin.readline
a = input().split()
a = [int(i) for i in a]
print(vis(a))
