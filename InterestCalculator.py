# based on user's input, we calculate interest on term basis
amount, rate, term = input("Please enter amount<space>interest rate <space> term: ").split()
amount = float(amount)
rate = float(rate)
term = (int(term))
for i in range(term):
    amount = (amount + (amount * (rate / 100)))
print("Principle + interest is: {:.2f}".format(amount))

