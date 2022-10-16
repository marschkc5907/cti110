#CTI-110
#P2HW2 - List
#Cassandra Marschke
#13 October 2022
#
#This program uses input from the user to create a list of grades for module tests results
#The user enters a grade for each module
#Program displays the lowest module
#Program displays the highest module grade
#Program computes sum of all module grades
#Program computes average of all module grades
#

mod1 = float(input("Enter grade for Module 1:"))
mod2 = float(input("Enter grade for Module 2:"))
mod3 = float(input("Enter grade for Module 3:"))
mod4 = float(input("Enter grade for Module 4:"))
mod5 = float(input("Enter grade for Module 5:"))
mod6 = float(input("Enter grade for Module 6:"))
print('\n')
print("-------------Results-------------")
mod_grade_all = (mod1, mod2, mod3, mod4, mod5, mod6)
grade_low = min(mod_grade_all)
grade_high = max(mod_grade_all)
grade_sum = (mod1 + mod2 + mod3 + mod4 + mod5 + mod6)
grade_avg = (mod1 + mod2 + mod3 + mod4 + mod5 + mod6) / 6
print(f"Lowest Grade:{f'{grade_low:.1f}':>13}")
print(f"Highest Grade:{f'{grade_high:.1f}':>12}")
print(f"Sum of Grades:{f'{grade_sum:.1f}':>13}")
print(f"Average:{f'{grade_avg:.2f}':>19}")
print("---------------------------------------------")

