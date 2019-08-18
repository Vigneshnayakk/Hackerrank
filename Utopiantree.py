def utopianTree(n):
    g=0
    for i in range(0,n+1):
        if i//2==i/2:
            g+=1
        else:
            g*=2
    return g
l=[]
t = int(input())
for t_itr in range(t):
    n = int(input())
    result = utopianTree(n)
    l.append(result)
print(l)
