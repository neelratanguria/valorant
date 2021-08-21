
"""
#question 1
english = float(input("Please enter English Marks: "))
math = float(input("Please enter Math score: "))
computers = float(input("Please enter Computer Marks: "))
physics = float(input("Please enter Physics Marks: "))
chemistry = float(input("Please enter Chemistry Marks: "))

total = english + math + computers + physics + chemistry
average = total / 5
percentage = (total / 500) * 100

print(f"Total Marks ={total} "  )
print(f"Average Marks = {average}" )
print(f"Marks Percentage = {percentage}"  )

"""


#question 2
nums = list(map(int( input("Input integers: ").split(", "))))
nums.sort()
print(nums)


"""
#question 3

def factorial(n):

    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
n = int(input("enter the number=  "))
print(factorial(n))
"""
"""
#question 4
sum=0

for item in range(1,300,3):
    
    print (item)
    
#question 5

name =input("enter your name=   ")

i = 0

while i <= 5:
    print(name[i :i+1])
    i=i+1
print ("done")

"""
    
      



   







    