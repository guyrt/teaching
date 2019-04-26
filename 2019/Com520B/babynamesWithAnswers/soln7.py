import ssadata

# count total kids
total_girls = 0
for name in ssadata.girls:
    total_girls = total_girls + ssadata.girls[name]

print(total_girls)


total_boys = 0
for name in ssadata.boys:
    total_boys = total_boys + ssadata.boys[name]

print(total_boys)