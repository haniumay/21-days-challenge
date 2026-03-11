a=int(input("enter a first number"))
b=int(input("enter a second number"))
c=int(input("enter a third number"))
if(a>b and a>c):
    print("a is largest")
elif(b>a and b>c):
    print("b is largest")
else:
    print("c is largest")
    

#------------------power-------------------------#
base=int(input())
power=int(input())
c=base**power
print(c)
        
#-----------------percentage------------------------#
m1=int(input())
m2=int(input())
m3=int(input())
m4=int(input())
m5=int(input())
total=m1+m2+m3+m4+m5
percentage=total/5
print(percentage)