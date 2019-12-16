# enter 2 nums simultaneously and detect them including the operator

num1, operator, num2 = input("please enter the calculation: ").split()

num1 = int(num1)
num2 = int(num2)

# conditions based off operators

if operator == "+":
    print("{} + {} = {}".format(num1,num1,num1 + num2))

elif operator == "-":
    print("{} - {} = {}".format(num1,num1,num1 - num2))

elif operator == "*":
    print("{} * {} = {}".format(num1, num2, num1 * num2))

elif operator == "/":
    print("{} / {} = {}".format(num1,num1,num1 / num2))

else:
    print("unidentified operator. please use one of these: + - * /")






