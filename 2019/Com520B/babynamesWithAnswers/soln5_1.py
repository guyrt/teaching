import ssadata

# count girls and boys names that start with a
counter = 0
for name in ssadata.girls:
    if name[0] == 'a':
        counter = counter + 1

print('girls')
print(counter)

boys_counter = 0
for name in ssadata.boys:
    if name[0] == 'a':
        boys_counter = boys_counter + 1

print('boys')
print(boys_counter)

