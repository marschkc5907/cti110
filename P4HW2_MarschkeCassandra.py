# CTI-110
# P3HW2 - Salary
# Cassandra Marschke
# 15 November 2022
#
# The program below receives input from user about pay rate and hours worked and calculates overtime, regular, and gross pay.
# Enter employee name
# Enter employee hours
# Enter hourly pay
# The program calculates employee's regular and gross pay amounts based on hours worked and hourly rate of the employee.
#

total_employ = 0
over_pay = 0
reg_pay = 0
gross_pay = 0

while(True):
    name = input("Enter employee's name or \"None\" to terminate: ")

    if name == "None":
        break
    else:
        total_employ += 1

    hours = float(input("How many hours did " + name + " worked? "))
    rate = float(input("What is " + name + "\'s pay rate? "))
    overtime = 0
    overPay = 0
    regPay = 0
    grossPay = 0

    if hours > 40:
        overtime = hours - 40
        overPay = overtime * rate * 1.5
        regPay = 40 * rate
        grossPay = regPay + overPay
    else:
        regPay = hours * rate
        grossPay = regPay

    over_pay += overPay
    reg_pay += regPay
    gross_pay += grossPay

    print("\nEmployee name: " + name + "\n")
    print("{:<20}{:<20}{:<20}{:<20}{:<20}{:<20}".format("Hours Worked", "Pay Rate", "OverTime", "OverTime Pay", "RegHour Pay", "Gross Pay"))
    print("-------------------------------------------------------------------------------------------------------------")
    print("{:<20.1f}{:<20.1f}{:<20.1f}{:<20.1f}${:<19.2f}${:<20.2f}".format(hours, rate, overtime, overPay, regPay, grossPay))
    print()

print()
print("Total number of employees entered:", total_employ)
print("Total amount payed for over time: $" + '{:.2f}'.format(over_pay))
print("Total amount payed for regular hours: $" + '{:.2f}'.format(reg_pay))
print("Total amount payed in gross: $" + '{:.2f}'.format(gross_pay))
