import ssadata

# second go at 11
# MODIFICATION: if a name occurs more than 20 times, just
# count it as 'common'
# output dict will have a key 'common'. it will also
# have keys 5, 6, 7, 8, 9, 10, ... 20

names_with_target_occurences = {}  # dict storing number to count
for foobar in ssadata.girls:  # girls is a dict storing name to number of people
    # get the number of people with the given name
    num_people = ssadata.girls[foobar]
    if num_people > 20:
    	num_people = 'common'
    if num_people in names_with_target_occurences:
        names_with_target_occurences[num_people] += 1
    else :
        names_with_target_occurences[num_people] = 1

print(names_with_target_occurences)
