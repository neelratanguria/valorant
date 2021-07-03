"""
number =input("enter the date:")


sum_of_digits = 0




for digit in str(number):


  sum_of_digits += int(digit)
  
  
  print(sum_of_digits)
  break
  
for digit in str(number[0:2]):


  sum_of_digits += int(digit)
  
  
  print(sum_of_digits)
 





if (int(digit) > 6):
    print("it is past")
    """

"""
from datetime import datetime
start_date = "10/2/2020 "
end_date = "10/2/2021 "

# format of date/time strings; assuming dd/mm/yyyy
date_format = "%d/%m/%Y "

# create datetime objects from the strings
start = datetime.strptime(start_date, date_format)
end = datetime.strptime(end_date, date_format)
now = datetime.now()

if end < now:
  # event in past
  """
  
  """
import array
month=array.array('i',[0,31,28,31,30,31,30,31,31,30,31,30,31])
count=0
d=int(input("Enter a day:"))
months=int(input("Enter a month:"))
year=int(input("Enter a year:"))
days=int(input("Enter number of days:"))
if year%4==0:
    month[2]=28
while count<days:
    d=d+1
    count=count+1
    if d>month[months]:
        d=1
        months=months+1
    if months>12:
        months=1
        year=year+1
        if year%4==0:
            month[2]=29
        else:
            month[2]=28
print("Future date= ", end='')
print(d,end='-')
print(months,end='-')
print(year)
"""

""""
# importing the module
import calendar

d,m,y=map(int,input('Enter the value of date,month and year: ').split())

a=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']

try:
    s=calendar.weekday(y,m,d)
    print('Weekday:',a[s])
except ValueError:
    print('You have entered an invalid date.')
""""


from datetime import date
todays_date = date.today()
year = todays_date.year
date = int(input("enter the year"))

if date == year:
    print("this year")
elif date < year:
    print("not this yr")







