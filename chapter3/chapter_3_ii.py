#practice session
a=input("enter your name:")
print("good afternoon "+ a +" welcome to the class")

name=input("Enter your name :")
date=input("Enter the date :")
template=('''dear <|name|>, 
you are selected! on <|date|>''')
print(template.replace("<|name|>",name).replace("<|date|>",date))

line="this line is  going  to have  a lot of spaces"
print(line)
print(line.find("  "))
print(line.replace("  ", " "))


letter="dear name, \n\tthis python course is \"nice\" \n\t\tthanks!"
print(letter)