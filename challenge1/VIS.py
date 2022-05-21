# copyright Max Osterried, ETHZ, 21.05.2022
import sys


#############
def vis(ein):
    x = "vis"
    it = iter(ein)
    return all(any(c == ch for c in it) for ch in x)


#############
# input = sys.stdin.readline
# n = int(input())

# for _ in range(n):
input = sys.stdin.readline
a = str(input()).strip()
print("YES" if vis(a) else "NO")
