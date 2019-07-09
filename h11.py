n=input().split()
d=[]
for i in n:
   d.append(i)
print(''.join(map(str,d[::-1])))
