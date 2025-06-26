oxford ={"note": "used to write" , 
    "pen": "used for writing",
    "exam": "to analyse the skill"}
key= input("enter the key\n")
if(oxford.get(key)== None):
    print("The key does not exist")
else:
    print("The value of the key is", oxford.get(key))