# This is a program that creates a math quiz for a user. The program asks
# the user to choose add or subtract, and then asks the user to answer the quiz.
# The program outputs the amount of guesses the user has made before getting the correct answer.
# 22 November 2022
# CTI-110 P5HW2 - Math Quiz
# Cassandra Marschke

import random

def addProblem():
    a = random.randint(10,99)
    b = random.randint(10,99)
    guesses = 0
    print(f'  {a}')
    print(f'+ {b}\n')
    print('Enter answer.')
    answer = int(input())
    guesses += 1
    while answer!= (a+b):
        if answer < (a+b):
            print('Sorry, guess is too low.\n')
        else:
            print('Sorry, guess is too high.\n')
        answer = int(input('try again: '))
        guesses += 1
    print('Congratulations!!!! your answer is correct...')
    print('Number of guesses: {}'.format(guesses))
    print()

def subProblem():
    a = random.randint(10, 99)
    b = random.randint(10, 99)
    attempts = 0
    if a<b:a,b=b,a
    print(f'  {a}')
    print(f'- {b}\n')
    print('Enter answer.')
    answer = int(input())
    attempts += 1
    while answer != (a - b):
        if answer < (a - b):
            print('Sorry, guess is too low.\n')
        else:
            print('Sorry, guess is too high.\n')
        answer = int(input('try again: '))
        attempts += 1
    print('Congratulations!!!! your answer is correct...')
    print('Number of guesses: {}'.format(attempts))
    print()

def main():
    print('Welcome to Math Quiz\n')
    while True:
        print('MAIN MENU')
        print('--------------------')
        print('1. Adding Random Numbers')
        print('2. Subtracting Random Numbers')
        print('3. Exit\n')
        choice = input('Please choose one of the menu options: ')
        if choice == '1':
            addProblem()
        elif choice == '2':
            subProblem()
        elif choice == '3':
            print('Thank you for playing...\nBye!!')
            break


main()
