l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
for n in range(0,l1[1]):
   l2=[l2[-1]]+l2[:-1]
print(*l2,end=" ")
