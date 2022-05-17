  
from colorama import Fore, init
# ask a user to enter their first name and store it in a variable
# ask a user to enter their last name and store it in a variable
# print their full name
# Make sure you have a space between first and last name
# Make sure the first letter of first name and last name is uppercase
# Make sure the rest of the name is lowercase

init(convert=True,wrap=True)
# print(Fore.LIGHTBLUE_EX+'What is your First Name: '+Fore.LIGHTYELLOW_EX)
# first_name = input()

# last_name = input(Fore.LIGHTBLUE_EX+'What is your Second Name: '+Fore.LIGHTYELLOW_EX)

5
# Ask a user to enter a number
# Ask a user to enter a second number
# Calculate the total of the two numbers added together
# Print 'first number + second number = answer' 
# For example if someone enters 4 and 6 the output should read
# 4 + 6 = 10

first_number = input('one number: ')
second_number= input('another number: ')
total= int(first_number)+ int(second_number)
print('Total:' +str(total ))