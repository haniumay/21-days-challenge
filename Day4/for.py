i=1
for i in range(1,21):
    print(i)
#------------mul------------#
n=int(input("Enter a number:"))
for i in range(1,11):
    print(n,"*",i,"=",n*i)   
#----------------sum of n-----------------#
a=int(input("Enter a number:"))
sum=0
for i in range(1,a+1):
   sum=sum+i
   print("the sum of number is",sum)
#----------------rev----------------#
a=int(input("Enter a number:"))
rev=0
while a>0:
    rem=a%10
    rev=rev*10+rem
    a=a//10
    print(rev)
#---------------count----------------#
a=int(input("enter the number:"))
sum=0
for i in range(1,a+1):
    if(i%2==0):
        sum+=1
        print(sum)