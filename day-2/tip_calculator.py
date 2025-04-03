print("Welcome to the tip calculator!\n")
total_bill = int(input("What was the total bill?\n$"))
tip_percentage = int(input("How much tip would you like to give? 10, 12, or 15? \n"))
number_of_people = int(input("How many people to split the bill?\n"))

total_bill = total_bill + (total_bill * tip_percentage/100)
share = total_bill / number_of_people

print("\nEach person should pay: $" + str(share))