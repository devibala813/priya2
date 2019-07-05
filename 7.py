dvi=list(input())
for i in range(0,len(dvi),2):
   dvi[i],dvi[i+1]=dvi[i+1],dvi[i]
pri=''.join(dvi)
print(pri)
