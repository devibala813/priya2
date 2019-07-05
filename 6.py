m1,m2=map(str,input().split())
if(len(m1)!=len(m2)):
   print("no")
else:
   o1=[m1.count(i) for i in m1]
   o2=[m2.count(i) for i in m2]
if(o1==o2):
   print("yes")
else:
   print("no")
