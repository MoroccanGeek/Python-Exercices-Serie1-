import string
import random

#My Rules for Password Power
#Weak===> one charachter from each List below (Example: Password=Ac9) [Notice: this isn't shuffled]
#Medium===> two charachters from each List below (Example: Password=AFcy93)
#Strong===> three charachters from each List below (Example: Password=ARDcea934)

Upper=list(string.ascii_uppercase)  #[A-Z]
Lower=list(string.ascii_lowercase)  #[a-z]
Digits=list(string.digits)  #[0-9]

#Fucntion returns a List["Upper_Letter","Lower_Letter",Digit]
def pass_gived():
    return list(Upper[random.randint(0,25)]+Lower[random.randint(0,25)]+Digits[random.randint(0,9)])
    

def Generate_Password(Password_Power):
    Password=""
    if(Password_Power=="Weak"):
        Pass_temp=pass_gived()
        random.shuffle(Pass_temp) #Shuffle my password
        Password+="".join(Pass_temp)
        
    elif(Password_Power=="Medium"):
        Pass_temp=[]
        for x in range(2):
            Pass_temp.extend(pass_gived())
        
        random.shuffle(Pass_temp) #Shuffle my password
        Password+="".join(Pass_temp)
    else:
        Pass_temp=[]
        for x in range(3):
            Pass_temp.extend(pass_gived())
            
        random.shuffle(Pass_temp) #Shuffle my password
        Password+="".join(Pass_temp)
    return Password

print(Generate_Password("Strong"))