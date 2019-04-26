import ssadata

# what is the least common name
least_common_name_occurences = 92929292929292929292292
least_common_name = ''
for name in ssadata.girls:
    current_occurences = ssadata.girls[name]
    if least_common_name_occurences > current_occurences:
        least_common_name = name
        least_common_name_occurences = current_occurences

print(least_common_name)
print(least_common_name_occurences)