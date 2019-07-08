m1,m2=map(int,input().split())
for i in range(1,100000):
   if(i%m1==0 and i%m2==0):
      print(i)
      break
      
