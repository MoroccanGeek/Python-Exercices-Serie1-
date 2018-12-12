a = [5, 10, 15, 20, 25]
#first method
#l1=[]
#l1.append(a[0])
#l1.append(a[-1])
#second method
l2=[a[x] for x in range(len(a)) if(x==0 or x==len(a)-1)]

print(l2)