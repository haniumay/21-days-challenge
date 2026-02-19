a=int(input("enter a number:"))
if(a>0):
    print("positive")
elif(a<0):
    print("negative")    
else:
    print("zero")
    
    
    
#------------------leap year---------------#
a=int(input())
if(a%4==0 & a%100!=0)|(a%400==0):
    print("leap year")
else:
    print("non leap year")    