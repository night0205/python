n = int(input())
def merge_sort(arr):
    n = len(arr)
    if n <= 1:
        return
    m = n//2
    l = arr[:m]
    r = arr[m:]
    merge_sort(l)
    merge_sort(r)
    l.append(10000000000000000)
    r.append(10000000000000000)
    li = 0
    ri = 0
    for i in range(n):
        if l[li] < r[ri]:
            arr[i] = l[li]
            li += 1
        else:
            arr[i] = r[ri]
            ri += 1

arr = list(map(int,input().split()))
merge_sort(arr)
print(*arr)
