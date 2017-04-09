# A very simple example of loops.

# TODO: understand what will be printed if you run this.

days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'satuday', 'sunday']

for i in days:
    if i[0] == 't':
        print(i + " starts with t")
    elif i[0] == 's':
        print("WEEKEND!!!!!!")
        break
    else:
        print("not special")
    print(i)

print("done")