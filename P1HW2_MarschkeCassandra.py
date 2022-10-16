#The code below inputs a budget and subtracts expenses
#21 September 2022
#CTI-110 P1HW2 - Travel Expense
#Cassandra Marschke


print("This program calculates and displays travel expenses", '\n')
user_num = int(input("Enter Budget:"))
user_destination = input("Enter your travel destination:")
user_num2 = int(input("How much do you think you will spend on gas?"))
user_num3 = int(input("Approximately, how much will you need for accomodation/hotel?"))
user_num4 = int(input("Last, how much do you need for food?"))
print('\n')
print('----------Travel Expenses----------')
print('Location:', user_destination)
print('Initial Budget:', user_num)
print('Fuel:', user_num2)
print('Accomodation:', user_num3)
print('Food:', user_num4)
print('___________________________________')

user_total = (user_num-(user_num2+user_num3+user_num4))
print('Remaining Balance:', user_total)
