num1=int(input())
l1=list(map(int,input().split()[:num1]))
count=0
fp=[]
for i in range(0,num1+1):
   if(l1.count(i)>1):
      fp.append(i)
if(len(fp)==0):
   print("unique")
kl=sorted(fp)
print(' '.join(map(str,kl)))
