import sys

n, k, q = map(int, input().split())
a_list = list(map(int, input().split()))

while k > 0:
    k-=1
    temp = a_list[len(a_list) - 1]
    a_list.pop()
    a_list.insert(0, temp)    

while q > 0:
    q-=1
    answear = int(input().strip())
    print(a_list[answear])





