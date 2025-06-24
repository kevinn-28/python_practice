#list basics
a=12
b="a string to the list"
c= True
list=[a, b ,c ,3.14]
print(list)
print(type(list))

# slicing of list 
l1=[1,2,3,4,"tools"]
print(l1)
print(l1[0])
print(type(l1[0]))
print(l1[1:3])
print(l1[1:300])

#sorting a list
list1=[1,8,7,2,21,151200,3,4]
print(list1)
list1.sort()
print(list1)
#reversing a list
list1.reverse()
print(list1)
#appending to a list
list1.append(100)
print(list1)
#inserting to a list
list1.insert(1,240)
print(list1)
list1.pop()
list1.pop()
list1.pop(1)
list1.remove(151200) 
print(list1)
list2=[1,2,3,4,5,3,5,6]
list2.remove(3)
print(list2)