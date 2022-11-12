# CTI-110
# P3HW1 - Debugging
# Cassandra Marschke
# 20 October 2022
#
# This program takes a number grade input and determines average and displays letter grade for average.
# Enter grades for six modules.
# Program calculates and outputs lowest, highest, sum, and average of grades entered.
# Program calculates letter grade based on average.
# Program outputs letter grade.


mod_1 = float(input('Enter grade for Module 1: '))
mod_2 = float(input('Enter grade for Module 2: '))
mod_3 = float(input('Enter grade for Module 3: '))
mod_4 = float(input('Enter grade for Module 4: '))
mod_5 = float(input('Enter grade for Module 5: '))
mod_6 = float(input('Enter grade for Module 6: '))
print('/n')
print("------------Results-------------")
all_grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]
low = min(all_grades)
high = max(all_grades)
sum = (mod_1 + mod_2 + mod_3 + mod_4 + mod_5 + mod_6)
avg = (mod_1 + mod_2 + mod_3 + mod_4 + mod_5 + mod_6) / 6
print(f"Lowest Grade:{f'{low:.1f}':>13}")
print(f"Highest Grade:{f'{high:.1f}':>12}")
print(f"Sum of Grades:{f'{sum:.1f}':>13}")
print(f"Average:{f'{avg:.2f}':>19}")
print("---------------------------------------------")

# determine letter grade for average

if avg >= 90:
    print('Your grade is: A')
elif avg >= 80:
    print('Your grade is: B')
elif avg >= 70:
    print('Your grade is: C')
elif avg <= 65:
    print('Your grade is: F')





