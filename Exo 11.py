def list_of_divisors(number):
    l=[x for x in range(2,number-1) if number%x==0]
    return l

def is_Prime(number):
    if len(list_of_divisors(number))==0:
        return True
    else: return False

number=3
print(is_Prime(73))