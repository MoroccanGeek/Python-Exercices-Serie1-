def List_Ends(l):
    w=[]
    w.append(l[0])
    w.append(l[-1])
    return w
    
def List_Ends2(l):
    w=[l[x] for x in range(len(a)) if(x==0 or x==len(a)-1)]
    return w
def main():
  a = [5, 10, 15, 20, 25]
  print(List_Ends(a))
  
if __name__ == "__main__":
  main()
  
