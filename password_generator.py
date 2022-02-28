import random
import string
def generating_password(s_char,alpha,num):
    password=""
    password+=s_char
    password+=alpha
    password+=str(num)
    return password
def checking_password(password):
    up,lo,di,sp=0,0,0,0
    for i in password:
        if i.isupper():
            up+=1
        if i.islower():
            lo+=1
        if i.isdigit():
            di+=1
        if(i=='@' or i=='$' or i=='_'):
            sp+=1
    if(len(password)>=8 and up>=1 and lo>=1 and sp>=1):
        return 'strong'
    else:
        return 'weak'
        
s_char=input('Enter the special characters for password : ')
alpha=input('Enter the alphabets for password : ')
num=int(input('Enter the numbers for password : '))
password=generating_password(s_char,alpha,num)
print('Your password is :',password)
res=checking_password(password)
if res=='strong':
    print('Your password is strong')
else:
    print('Your password is weak')
myfile=open("data.txt","a+")
myfile.write(password)
