a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

if(len(a)<len(b) or len(a)==len(b)):
    z=list(set(a))
    w=list(set(b))
else:
    z=list(set(b))
    w=list(set(a))
#method1
#for x in z:
 #   if(w.count(x)==0):
  #      w.append(x)
#method2__Exo10
temp_list=[x for x in z if(w.count(x)==0)]
w.extend(temp_list)
print("Our combined List with no duplicates is: ","\n",sorted(w))
    