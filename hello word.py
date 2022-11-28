# practice python program
# Felix Reyes
#color to console text
from colorama import init, Fore, Style

#colorama initiation required 
init()


firt_name='Felix'
last_name='Reyes'

print()
# name=input('What is your name?: ')
# print('\n')
# print ('Nice to meet you '+name.capitalize()+'!')
# print('\n')


ouput_text = ''

#any python version
ouput_text='Your full name is :{0} {1}'.format(firt_name, last_name)

#python 3 formating "f"
ouput_text= f'Your full name is {firt_name} {last_name}'

print(ouput_text)

# str()
# float()
# int()
from datetime import datetime   , timedelta
today = datetime.now()

print('Today is: ' +str(today))
number_of_days = timedelta(days=1) 
yesterday = today - number_of_days
print (Style.DIM)
print (Fore.GREEN +Style.DIM+'Yesterday was    :'+Fore.YELLOW +  datetime.strftime(yesterday,'%A %d-%b-%Y'))
print(Fore.GREEN + 'Day of the week  :'+Fore.YELLOW + today.strftime('%A'))
print(Fore.GREEN + 'Day              :'+Fore.YELLOW + str(today.day))
print(Fore.GREEN + 'Month            :'+Fore.YELLOW + str(today.month))
print(Fore.GREEN + 'Year             :'+Fore.YELLOW + str(today.year))
#print (Style.RESET_ALL)
# today.strptime parses a string to the especificed datetime format
# today.strftime display a datetime variable on the specified format

print(Fore.CYAN +'Date             :'+Fore.YELLOW +today.strftime('%A %d-%b-%Y'))

print(Fore.WHITE)
#list and arrays

#list= []   start from zero  support mix types of items            list=[0,5]to get 5 items from 0-4   .append to add   insert[0 index] len()
#arrays ={} start from zero  simple type of items like numbers     ""
#dictionaries = {'key':'Value'}  to retrive values dictionary[key]


person ={}
person ={'first':'felix', 'last':'reyes'}

print (person)
print(person['first'])
person['first']='Felix M'
print(person['first'])

#loops for in 

items_list=['uno','dos','tres','cuatro','cinco']

# for items_list. in range(0,5):
#     print(items_list)

for x in (items_list):
    print(Fore.CYAN + x)
    


print(Fore.YELLOW + '  \n ---- next ---- \n')

# print(items_list[1])

for x in range(0,4):
    print(Fore.GREEN + items_list[x])
 # print(person)

   # print(x)





