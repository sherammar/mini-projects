# mini project to order a Pizza

# user input and will ask which size of pizza he wants( S, M, L) (400, 700, 1000)
# user input and will whether the user wants to add pepporini (100, 200, 300)
# user input and will ask the user whether he wants to add cheese or not (150)

print(" WELCOME TO our RESTRAUNT")

user_input1 = input(" Which size of pizza you want ? S/M/L \n").lower()
total_bill = 0
if user_input1 == "s":
    total_bill += 400     
elif user_input1 == "m":
    total_bill += 700
elif user_input1 == "l":
    total_bill += 1000
else:
    print("Please add the correct input!")


want_pepporini = input("Do you want to add pepporini ? Yes/No \n").lower()
if user_input1 == "s" and want_pepporini == "yes":
    total_bill += 100
elif user_input1 == "m" and want_pepporini == "yes":
    total_bill += 200
elif user_input1 == "l" and want_pepporini == "yes":
    total_bill += 300

want_cheese = input("Do you want to add cheese ? Yes/No \n").lower()
if want_cheese == "yes":
    total_bill += 150

print("This is your total bill : ", total_bill)
