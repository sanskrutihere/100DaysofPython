print("Welcome to the tip calculator! :)")

bill = float(input("What was the total bill? $"))
tip = input("How much tip would you like to give? 10, 12, or 15? ")
people = input("How many people to split the bill? ")

#calculate the bill with tip
bill_with_tip = tip / 100 * bill + bill

#calculate tip per person
tip_per_person = bill_with_tip / people

#round off the amount to two floating points
split = round(tip_per_person, 2)

#display output
print(f"Each person should pay: ${split}")