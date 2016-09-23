import sys

n, k, q = map(int, input().split())
arr = list(map(int, input().split()))
rotated_arr = []
transpose = k % n

for i in range(n):
    if (n - transpose + i) > (n - 1):
        item = arr[i - transpose]
    else:
        item = arr[n - transpose + i]        
    rotated_arr.append(item)

while q > 0:
    q-=1
    answear = int(input().strip())
    print(rotated_arr[answear])
