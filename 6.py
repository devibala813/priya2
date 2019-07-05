m1,m2=map(str,input().split())
if(len(m1)!=len(m2)):
   print("no")
else:
   k1=[m1.count(i) for i in m1]
   k2=[m2.count(i) for i in m2]
if(k1==k2):
   print("yes")
else:
   print("no")
