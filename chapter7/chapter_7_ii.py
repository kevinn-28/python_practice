num=11
for i in range (1,11):
 print(f"{num}*{i}={num * i}")
#################################
l1=["siva","sanjay","deepak","Sunil"]
l1 = [item.lower() for item in l1]
for item in l1:
    if item.startswith("s"):
        print(f"greetings {item}")   
        continue
    print(f"hello {item}")
    