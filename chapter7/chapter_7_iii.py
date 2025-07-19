#prime number or not
num=int(input("Enter a number: "))
for i in range(2, num):
    if num % i == 0:
        print(f"{num} is not a prime number")
    break
else:
        print(f"{num} is a prime number")
################################
i=1
sum=0
n=4
while(i<=n):
    sum+=i
    i+=1
print(f"the sum of first {n} natural number is {sum}")
#################################
n=int (input("enter n"))
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end="")
    for j in range(2*i-1):
        print("*",end="")
    for j in range(n-i):
        print(" ",end="")
    print("\n",end="")
###############################
n=3
for i in range(1,n+1):
    for j in range(n-i):
        print("",end="")
    for j in range(2*i-1):
        print("*",end="")
    for j in range(n-i):
        print(" ",end="")
    print("\n",end="")
###############################
n=4
for i in range(n):
    for j in range(n):
        if (i==0 or j==0 or i==n-1 or j==n-1):
            print("*",end=" ")
        else:
            print("  ",end="")
    print("\n",end="")
##############################
n=15
for j in range (1,11):
    i=11-j
    print(f"{n}X{i}={n*i}")
