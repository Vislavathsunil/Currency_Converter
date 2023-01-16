# Project to make a currency Generator
"""Converts the currency from  one country to another country """

currency = {"USD": 87, "EUR": 81.34, "INR": 1, "CNY": 11.80, "JPY": 0.57, "SGD": 57.29, "BRL": 14.59, "EGP": 4.21,
            "SAR": 21.25, "PAK": 0.35, "EGP": 4.21, "QAR": 21.84, "ZAR": 4.65, "AUD": 54.87, }


def convert(c1, amount, c2):
    if c2 == "INR":
        print("The Currency After Converting into %s is" % c2, (amount * currency[c1]))
    elif c1 == "INR":
        print("The Currency After Converting into %s is" % c2, (amount / currency[c2]))
    else:
        print("The Currency After Converting into %s is" % c2, (amount * currency[c1]) / currency[c2])


print(" ---------------------- ")
print("|  Currency Converter  |")
print(" ---------------------- ")
for i in currency.keys():
    print(i)
print("PLEASE SELECT ONE CURRENCY CODE FROM THE LIST...")
c1 = input("Enter The Currency: ")  # The Currency given
amount = int(input("Enter The Amount: "))  # The amount in the given currency
c2 = input("Enter The Currency you want to convert to: ")  # The currency you want to covert the amount in the given country.
convert(c1, amount, c2)  # calling the function

print("Thank You")