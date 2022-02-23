l=[]
n=int(input('enter n:'))
for i in range(n):
    x=int(input())
    l.append(x)
for x in range(n-1,-1,-1):
    print(l[x])
