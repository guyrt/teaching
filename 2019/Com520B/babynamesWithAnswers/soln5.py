import ssadata

# count girls and boys names
counter = 0
for name in ssadata.girls:
    counter = counter + 1

print('girls')
print(counter)
print(len(ssadata.girls))

counter = 0
for name in ssadata.boys:
    counter = counter + 1

print('boys')
print(counter)
#print(len(ssadata.boys))

