t = ['a','b','c']
def hanoi(n, start, end):
    if n == 1:
        print('move ring', n, 'from',t[start], 'to',t[start])
        return
    tmp = 3-start-end
    hanoi(n-1, start, tmp)
    print('move ring', n, 'from',t[start], 'to',t[start])
    hanoi(n-1,tmp,end)
n = int(input())
hanoi(n, 0, 2)
