mark1=(int(input("Enter your mark 1:\n")))
mark2=(int(input("Enter your mark 2:\n")))
mark3=(int(input("Enter your mark 3:\n")))
mark =mark1,mark2,mark3
percent1=(mark1/100)*100
percent2=(mark2/100)*100
percent3=(mark3/100)*100
percent =(percent1+percent2+percent3)/3
if percent1>=40 and percent2>=40 and percent3>=40:
    print("You are pass")   
    print("Your percentage is", percent,mark)
else:
    print("You are fail")
    print("Your percentage is", percent,mark)