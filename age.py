total = 0
print ( "Please enter 10 ages: ")
for i in range(10):
    age = eval(input("Please enter age in the range of 0-110: "))#V
    while (age<0) or (age>110):#Added Checking
        age = eval(input("Invalid input. Please enter age in the range of 0-110: "))
        if (age>=0) and (age<=110):
            break
    total = total + age
print ("average age is ",float(total)/10)
