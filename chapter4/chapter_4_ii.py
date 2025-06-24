a=input("enter fruit 1:")
b=input("enter fruit 2:")
c=input("enter fruit 3:")
d=input("enter fruit 4:")
e=input("enter fruit 5:")
f=input("enter fruit 6:")
g=input("enter fruit 7:")
list =[a,b,c,d,e,f,g]
print("The list is:", list)
print(type(list))

mark1=int(input("enter mark 1:"))
mark2=int(input("enter mark 2:"))
mark3=int(input("enter mark 3:"))
mark4=int(input("enter mark 4:"))
mark5=int(input("enter mark 5:"))
mark6=int(input("enter mark 6:"))
sorted_marks = [mark1, mark2, mark3, mark4, mark5, mark6]
sorted_marks.sort()
print("The sorted marks are:", sorted_marks)

addition=[2, 5, 3, 8,1]
sum=0
sum+=addition[0]
sum+=addition[1]
sum+=addition[2]
sum+=addition[3]
sum+=addition[4]
print("The sum of the list is:", sum)


tuple_a=(7, 0, 8, 0, 0, 9)
print("the number of zeros ",tuple_a.count(0))

