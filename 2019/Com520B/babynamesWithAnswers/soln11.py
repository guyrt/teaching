import ssadata

# find a histogram of baby name counts

# to start: count people who have a name that occurs 5 times
for target in [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]:  # equiv to range(5, 21)
    names_with_target_occurences = 0
    for foobar in ssadata.girls:
        num_people = ssadata.girls[foobar]
        if num_people == target:
            names_with_target_occurences = names_with_target_occurences + 1

    print(str(target) + ' ' + str(names_with_target_occurences * target))
