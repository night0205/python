a,b,c = map(int,input().split())
a,b,c = bool(a),bool(b),bool(c)
flag = 0
if a & b == c:
    print("AND")
    flag = 1
if a | b == c:
    print("OR")
    flag = 1
if a^b == c:
    print("XOR")
    flag = 1 
if flag == 0:
    print("IMPOSSIBLE")
