print(" Welcome to the Tip Calculator")

total_bill = input("How much is the total bill..?")

tip = input("How much would you like to contribute for tip 10% or 15% or 20% or 30%..?")

people = input("How many people are splitting up the bill")

total_bill_float = float(total_bill)
tip_int = int(tip)
people_int = int(people)
actual_bill = (total_bill_float * (tip_int/100) / people_int)

print(f"Each person should pay {round(actual_bill,2)} ")


