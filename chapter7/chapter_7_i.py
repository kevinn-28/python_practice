for i in range(0, 10):
    print(i)  
################################# for loop
a=[1,2,"mango",5,"fruits"]
i=0
for item in a:
    print(item)
    i += 1
#################################
for i  in range (0, 50,2):
    print(i)
################################# for else
l=["apple", "banana", "cherry"]
for item in l:
    print(item)
else:
    print("No items left in the list")
#################################
a=[1,2,3,4,5]
for item in a:
    print(item)
    if item == 3: 
        continue
    print("list scanned",item)
else:
    print("list finished")
#################################
for i in range(0, 10):
    pass
print("This is a pass statement")