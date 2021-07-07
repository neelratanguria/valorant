""""
#code 1
#basics

name = input("what is you name? ")
print("Hi " +  name)


color = input("what is your favorate color " + name + " ? ")
print(name + " likes " + color)
"""

"""
#code 2
#basics

birth_year = input("birth year ")
print (type(birth_year))
age = 2021- int(birth_year)
print (type(age))
print (age)
"""

"""
#code 3

#string

weight_in_pounds = input("enter weight in pounds ")

print(type(weight_in_pounds))

weight_in_kilo = int(weight_in_pounds) * 0.75

print(type(weight_in_kilo))

print("ur wt in kg is " + str(weight_in_kilo))

"""
"""""
#code 4

first = "john"
last = "smith"

message = first + ' [' +last +'] is a coder'
msg = f'{first} [{last}] is a coder'

print(message)

print(msg)
"""""""""
"""""""""
 #code 5
 
 #if else
 
course = 'python for me'
print(len(course)) 

course.upper()
print(course.upper()) 
 
 
course.lower()
print(course.lower()) 

course = 'python for me'
print(course.find('y')) 
 
 
course = 'python for me'
print(course.replace('y','o')) 

course = 'python for me'
print('python' in course) 
if True:
    print(course.replace('me','you'))
else:
    print(course.find('o'))
 
"""""""""
"""""""""
#code 6
is_hot = False
is_cold = True

if is_hot:
    print("its a hot day")
    print("drink water")

elif is_cold:
    print("its cold day")    

else:
    print("its lovly day")
    
    
high_income = True
good_credit = True

if high_income and good_credit:
    print("for loan")
   
 
high_income = True
good_credit = False
if high_income or good_credit:
    print("for loan")
 
high_income = True
good_credit = False
if high_income and not good_credit:
    print("for loan")
 
"""""""""
"""""""""
 #code 7
 
 #operations
 
temp = 35

if temp > 30:
    print ("its hot day")

else:
    print("its not hot")

#>
#<
#==
#!= not equal
#>=
#<=


#if name is less than 3 character long 
   #name must be at least 3 characters
#otherwise if its more than 50 characters long
   #name can be max of 50 character
#otherwise
   #name looks good
   
naam = input("enter your name")

name= len(naam)

if name < 3:
    print("name must be at least 3 characters")

elif name > 50:
    print("name can be max of 50 character")
    
else:
    print("name looks good")
    
    
#not case sensitive

wt = int(input("enter your weight  "))

unit =input("(L)bs or (K)gs  ")

if unit.upper() == "L":
    convert = wt * 0.45
    print(f"you are {convert} kilos")
else:
    convert = wt / 0.45
    print(f"you are {convert} pounds")

"""""""""
"""""""""
#while loop

i = 1

while i <= 5:
    print(i)
    i=i+1
print ("done")

#gussing the number game
secret_number = 9
j= "you win"
i=0
o = 3
while i < o :
    guess = int(input('guess: '))
    i += 1
    if guess ==secret_number:
        print(j)
        break
else:
    print('sry u didnt win')
    
print('thank you playing')    

    
#car game

command=""

started=False
while True:
    command = input(">  ").lower()
    if command == "start":
         if started:
             print("already started")
         else:
            started=True
            print("car started....")
        
   
    elif command =="stop":
        if not started:
            print("car already stopped")
        else:
         started=False
         
         print('car stoped......')
    
    elif command == "help":
        print(''''''
        start - to start the car
        stop - to stop the car
        quit - to exit
              '''''')

    elif command =="quit":
        break
    
    else:
        print("sorry i don't understand that")

print ('thank you for playing')

"""""""""

#for loop

for item in ['apple', 'banana', 'mango']:
    print(item)
    
for item in range(2,10,3):
    print (item)


price = [10,20,30]

total=0
for number in price:
    total += number

print(f"total {total}")

#nested loops

for x in range(4):
    for y in range(3):
        print(f'({x}, {y})')


numbers=[5,2,5,2,2]
for x_count in numbers:
    print('x' * x_count)

#another way

fu=[8,4,8,4,4]

for xu in fu:
    output =''
    for count in range(xu):
        output += 'x'
    
    print(output)
        
#list
#to find the max no. in a list


numbers=[1,4,6,8,2,9]

max=numbers[0]

for number in numbers:
    if number > max:
        max = number
print(max)


#2d lists



matrix =[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]    
matrix[0][1]=20
print (matrix[0][1])
    
for pp in matrix:
    
    for item in pp:
     print (item)


#append (to add object)
#insert (it adds object wherever u want)
#remove(to remove object)
#pop (end object is remove)
#index(to check the existance of object in list)
#in (same as index but boolean)
#sort
#copy(it will be a different list)


#to remove deplicates

number =[2,2,4,5,3,4,6,1]

unique =[]

for numbers in number:
    if numbers not in unique:
        unique.append(numbers)
    unique.sort()    
print(unique)













