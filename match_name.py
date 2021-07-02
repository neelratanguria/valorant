name =input('please enter your name:')
fruits = ["apple", "orange", "cherry"]

fruits.append('Dragon fruit')

matched = False

for fruit in fruits:
    if name == fruit:
        matched = True

if matched:
    print("Hell yeah")
else:
    print("We didn't get a match")

if matched:
    print("yes")

'''
if name==x[0]:
    print ("prasun khani master")
else :
    print ("bimal is best")
    '''
    