# make a file that prints the 
# number of people who have
# a name that occurs n times in the data set.

# example output:

# 5,23100
# 6,24000
# 7,25000

import ssadata

# how many people have a name that occurs 5 times.
all_girl_values = ssadata.girls.values()

hist = {}  #  number of occurences => number of names

for value in all_girl_values:
    if value not in hist:
        hist[value] = 0
    hist[value] = hist[value] + 1

file_handle = open("challenge_results.csv", "w")
for number_of_occurences in hist:
    number_of_names = hist[number_of_occurences]
    output = str(number_of_occurences) + "," + str(number_of_names * number_of_occurences)
    file_handle.write(output)
    file_handle.write("\n")

file_handle.close()
