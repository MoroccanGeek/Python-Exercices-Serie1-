def is_Palindrome(s):
    i=int(len(s)/2)
    for x in range(i):
        if s[x]!=s[-x-1]:return False
    return True

def is_Palindrome2(s):
    i=int(len(s)/2)
    s1=s[:i]
    s2=s[-i:][::-1]
    if(s1==s2):return True
    else: return False

s="anna"
print(is_Palindrome2(s))

    