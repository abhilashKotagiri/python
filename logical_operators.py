# logical operators and or not;
age = eval(input("enter your age: "))
if age < 5:
    print("Too young!!!")
elif age == 5:
    print("Go to Kindergarten")
elif (age >= 6) and (age <= 17):
    print("Go to grade {}".format(age - 5))
else:
    print("Go to College")