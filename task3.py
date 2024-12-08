import random
a=int(input("enter the length of the ps"))
l=[]
s=["h","e","0","9","&","*","*","&","r","@","d","r","k","l","r","t",8,"1","9","0","5","%","3","#","@","3",1,"y","h",'#',"p",3,"o","q","z","m",4,5,6]
for i in range(0,a):
    n=random.randint(0,len(s)-1)
    l.append(str(s[n]))
#print("password generated is",l)
print("PASSWORD GENERATED:",end="")
for i in l:
    print(i,end="")

