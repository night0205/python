n,m = map(int,input().split())#n fans,m gift
g = list()

for i in range(n):
    g.append([i,0])

for i in range(m):
    a,b = map(int,input().split())#0 fans num,1 $
    g[a][1] += b

for i in range(n):
    for j in range(n):
        if i == j:
            continue
        if g[i][1] >= g[j][1]:
            t = g[i]
            g[i] = g[j]
            g[j] = t
        if g[i][1] == g[j][1] and g[i][0] >= g[0][1]:
            t = g[i]
            g[i] = g[j]
            g[j] = t
for i in range(n):
    print(g[i][0],g[i][1])



