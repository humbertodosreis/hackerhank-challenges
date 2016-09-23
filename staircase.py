import sys

n = int(input().strip())

for i in range(1, n + 1):
    print(str("#" * i).rjust((n + 1)-1, " "))

