# if elif...else example

# amount as a user input
amount = int(input("Enter the amount : "))

# computing discounted amount
if amount < 1000:
    discountedAmount = 0.95 * amount    # 5% discount if amount is less than 1000
elif 1000 < amount < 5000:
    discountedAmount = 0.9 * amount   # 10% discount if amount is less than 5000
else:
    discountedAmount = 0.85 * amount  # 15% discount if amount 5000 or above

# taking age and privilegeStatus from user
age = int(input("Enter age of a customer : "))
privilegeStatus = input("Is this a privilege customer : ")

if age > 70:
    discountedAmount = 0.95 * discountedAmount  # 5% discount if age is > 70
if privilegeStatus == "yes":
    discountedAmount = 0.95 * discountedAmount  # 5% discount if privilege customer

# printing final discounted amount
print(f"The discounted amount will be {discountedAmount}")





