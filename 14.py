n=input()
s=list(input())
l1=['a,'e','i','o','u','A','E','I','E','O','U']
d1=[]
for i in s:
   if i not in l1:
      d1.append(i)
 print(''.join(map(str,d1[::-1])))
