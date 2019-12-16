# calculate compound interest based off user input

investment, interest = input("Please enter an investment amount and interest rate: ").split()
investment = float(investment)
interest = float(interest)


for i in range(10):
    investment = investment + (investment * (interest / 100))
    print("investment + interest for the year {} is {:.2f}".format(i, investment))