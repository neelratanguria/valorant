d = {'UK': 0, 'USA': 1, 'N': 2}
d['Nationality'] = d['Nationality'].map(d)
d = {'YES': 1, 'NO': 0}
d['Go'] = d['Go'].map(d)

print(d)