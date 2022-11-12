# CTI-110
# P3HW2 - Salary
# Cassandra Marschke
# 25 October 2022
#
# The program below receives input from user about pay rate
# and hours worked and calculates overtime, regular, and gross pay.
# Enter employee name
# Enter employee hours
# Enter hourly pay
# The program calculates employee's pay amounts
#

employee_name = input("Enter employee's name: ")
worked_hours = int(input("Enter number of hours worked: "))
hourly_pay = float(input("Enter employee's pay rate: "))
print("-------------------------------------")
print("Employee name:  ", employee_name, '\n')
print('Hours Worked   Pay Rate')

if worked_hours > 40:
    print()
overtime_pay = 

if worked_hours > 40:
    total_gross_pay = worked_hours * hourly_pay + overtime_pay
