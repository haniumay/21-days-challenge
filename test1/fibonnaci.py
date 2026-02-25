n=int(input("enter a number:"))
fib1=0
fib2=1
for i in range(n):
    print(fib1)
    fibonacci=fib1+fib2
    fib1=fib2
    fib2=fibonacci
#===================factorial===========================#
n=int(input("enter a number:"))
factorial=1
for i in range(1,n+1):
    factorial=factorial*i
    print(factorial)
    
    
#=============================prime================#
n=int(input("Enter a number:"))
if(n<=1):
    print("Not Prime")
else:
    for i in range(2,n):
        if(n%i==0):
            print(" Not Prime")
        break
    else:
        print("prime") 