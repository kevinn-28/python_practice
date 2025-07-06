spamWords=['click here', 'subscribe', 'buy now', 'free', 'limited time offer']
email=input("enter your email:").lower()
spam=False
if('click here' in email ):
    spam=True
if('subscribe' in email ):
    spam=True
if('buy now' in email ):
    spam=True
if('free' in email ):
    spam=True
if('limited time offer' in email ):
    spam=True
    
print("this email spam?", spam)
################################################
USERNAME=input("Enter your username:")
len(USERNAME)
if len(USERNAME)<10:
    print("your user name consist of less than 10 characters:",(len(USERNAME)))
else:
    print("your user name consist of more than 10 characters:",(len(USERNAME)))
################################################
name=['alice' , 'bob' ,'chris' , 'dave' , 'eve']
list=(input("enter a name to find :")).lower()
if list in name:
    print("name found")
else:
    print("name not found")