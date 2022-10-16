#The code below inputs a budget and subtracts expenses
#09 October 2022
#CTI-110 P2HW1 - Travel
#Cassandra Marschke
#
#This program receives input from user to calculate travel expenses
#Program displays budget and expense amounts
#Program subtracts expenses from initial budget amount
#Display remaining balance of budget to user


print("This program calculates and displays travel expenses", '\n')
user_budget = int(input("Enter Budget:"))
user_destination = input("Enter your travel destination:")
user_fuel = int(input("How much do you think you will spend on gas?"))
user_lodging = int(input("Approximately, how much will you need for accommodation/hotel?"))
user_meals = int(input("Last, how much do you need for food?"))
print('\n')
print('----------Travel Expenses----------') 
print("Location:"+"{:>20}".format(user_destination))
print(f"Initial Budget:{f'${user_budget:.2f}':>13}")
print(f"Fuel:{f'${user_fuel:.2f}':>22}")
print(f"Accommodation:{f'${user_lodging:.2f}':>13}")
print(f"Food:{f'${user_meals:.2f}':>22}")
print('____________________________________')
print("")
user_total = (user_budget-(user_fuel+user_lodging+user_meals))
print(f"Remaining Balance:{f'${user_total:.2f}':>9}")


