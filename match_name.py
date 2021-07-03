name =input('please enter your name:')
fruits = ["apple", "orange", "cherry"]

fruits.append('Dragon fruit')
#adding a new element
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

