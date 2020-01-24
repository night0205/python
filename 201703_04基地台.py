n, k = map(int,input().split())
p = list(map(int,input().split()))
p.sort()
min = 1
max = p[n-1]-p[0]
r = mid = (min+max)//2

while min != max:
    beg = p[0]
    cnt = 1
    for i in range(n):
        if beg + r < p[i]:
            beg = p[i]
            cnt = cnt + 1
        if cnt > k:         
            break
    if cnt > k:
        min = r + 1
        r = (min+max)//2
    elif cnt <= k:
        max = r
        r = (min+max)//2
print(r)
