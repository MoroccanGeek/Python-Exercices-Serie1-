def Fib(maxi):
    S1=1
    S2=1
    Sum=0
    seq=[]
    seq.append(S1)
    seq.append(S2)
    for x in range(maxi):
        Sum=S1+S2
        seq.append(Sum)
        S1=S2
        S2=Sum
    return seq

def Fib2(n):
    f1=1
    f2=1
    w=[]
    if(n>0 and n<=2):
        w=[1 for x in range(n)]
    
    else:
        w=[1,1]
        i=0
        j=1
        for x in range(2,n):
            w.append(w[i]+w[j])
            i=i+1
            j=j+1
    
    return w

sequence_number=int(input("Enter how many Fibonnaci numbers to generate"))
print(Fib2(sequence_number))
  
