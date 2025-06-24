#tuple basics 
tuple1=(15,13,12,16,1,2,3,4)
print(tuple1)
print(type(tuple1))

#to identify a single tuple
a=(1,)
print(type(a))

#count
tuple2=(15,1,1,16,1,2,3,4)
print(tuple2.count(1))
print(tuple2.count(3))

#indexing
print(tuple2.index(3)) #find the index of the first occurrence of 3
print(tuple2[3])#find the value at index 3
