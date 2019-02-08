def no_dups(l):
    w=[]
    for x in l:
        if(x not in w):
            w.append(x)
    return w

a = [1, 1, 2, 3, 5, 8, 13, 14, 13, 21, 34, 55, 89]
print(no_dups(a))
  
