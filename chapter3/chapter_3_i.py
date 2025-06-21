#slicing strings
name="kevin"
print(name)
print(name[4])  
print(name[0:4])  
print(name[-4])

#skipping strings
line="hugeandbiglineinthecode"
print(line[0:20:2])  
print(line[:5])

#finding length of the string 
code="abcdefghijklmnopqrstuvwxyz"
print(len(code))
print(code.endswith("z"))
print(code.endswith("n"))
print(code.startswith("a"))
print(code.startswith("k"))
print(code.count("ab"))
print(code.capitalize())
print(code.find("z"))

#replacing strings
string="this book is a big book and a good book"
print(string.replace("book","note"))
print(string.replace("book","novel",1))  # replace only the first occurrence

#new line
name2="my name is \nkevin"
print(name2)

name3="my name \nis \tkevin"
print(name3)

name3="my name \"is kevin"
print(name3)

name3="my name is \\kevin"
print(name3)