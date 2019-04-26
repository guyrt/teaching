import ssadata

# find the most common boy's name
most_common_name_occurences = 0
most_common_name = ''
for name in ssadata.boys:
    current_occurences = ssadata.boys[name]
    if current_occurences > most_common_name_occurences:
        most_common_name = name
        most_common_name_occurences = current_occurences

print(most_common_name)
print(most_common_name_occurences)
