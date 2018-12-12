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
print(Fib(10))