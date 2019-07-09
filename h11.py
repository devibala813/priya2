n=input().split()
d=[]
for i in n:
   d.append(i[::-1])
print(''.join(map(str,d)))
