# This is day 2 project for the 100 Days of Python Course

print("Welcome to the Bill Tip Calculator!")

bill = float(input("Enter the amount of bill in Rupees: \n"))
num_people = int(input("Enter the number of people the bill is going to be split to: \n"))
tip_percent = float(input("Enter the percentage you want to tip: \n"))

bill += bill*tip_percent/100
print(f"Each person has to pay Rs {bill/num_people}")