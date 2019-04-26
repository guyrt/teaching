import ssadata

# count the number of girl's names that start with each letter of the alphabet
first_letter_counter = {}
for name in ssadata.girls:
    first_letter = name[0]
    if first_letter in first_letter_counter:
        # increment the number of names by 1 for that key
        first_letter_counter[first_letter] += 1
    else:
        # add the key to the dictionary with value 1
        first_letter_counter[first_letter] = 1

print(first_letter_counter)
