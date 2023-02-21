def encrypt(a,n):
    s = ''
    for i in range(len(a)):
        if(a[i].isalpha()==True):
            if(((ord(a[i]))>64 and (ord(a[i]))<(91-n)) or 
            ((ord(a[i]))>96 and (ord(a[i]))<(123-n))):
                s = s + chr(ord(a[i])+n)
            else:
                s = s + chr(ord(a[i])+n-26)
        else:
            s = s + a[i]
    return s

def decrypt(a,n):
    s = ''
    for i in range(len(a)):
        if(a[i].isalpha()==True):
            if(((ord(a[i]))>(64+n) and (ord(a[i]))<91) or 
            ((ord(a[i]))>(96+n) and (ord(a[i]))<123)):
                s = s + chr(ord(a[i])-n)
            else:
                s = s + chr(ord(a[i])-n+26)
        else:
            s = s + a[i]
    return s

x = int(input())
f = input()
s = input()
new_str = ''
if(f=='0'):
    new_str = encrypt(s,x)
if(f=='1'):
    new_str = decrypt(s,x)
print(new_str)
