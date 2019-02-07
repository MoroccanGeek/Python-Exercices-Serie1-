a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

#####################  Question1  ##########################
#l=[x for x in a if (x<5)]
#for x in a:
#    if(x<5):
#        print(x)

#####################  Extra1  ##########################
#l=[x for x in a if (x<5)]
#l=[]
#for x in range(len(a)):
#    if(a[x]<5):
#        l.append(a[x])
#print(l)

#####################  Extra2  ##########################
#l=[x for x in a if (x<5)]
#print(l)

#####################  Extra3  ##########################
number=number=int(input("Enter a number? "))
l=[x for x in a if x<number]
print(l)
