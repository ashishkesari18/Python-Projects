print("*** Har Har Mahadev -/\-***")
print("\n Welcome to Kedarnath Helicopter Service")

height = int(input("Please Enter your height in cm"))
cost =0
if height >= 120:
    print(" You can ride the Helicopter")
    weight = int(input("Please Enter your weight in kgs"))
    if weight <= 49:
        print("Under weight tickets are : $20")
        cost = 20
    elif weight <=68:
        print("Price according to your weight is : $40")
        cost =40
    elif weight >= 80:
        print("price for according to your weight is : $70")
        cost =70
   
    pic = input("if you want photo enter Y or N for No")
    if pic =='Y': 
        cost += 3
    print(f"You need to pay $ {cost} for the Helicopter Ride")
else:
    print("Sorry You can't get a ride")
        



