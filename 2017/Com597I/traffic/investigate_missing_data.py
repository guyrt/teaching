#
# print the first row with missing collision type.
#


file_handle = open("sdot_collisions_seattle.txt", "r")

# build a histogram of collision types

hist = {}  # collision type => number of collisions
column_of_interest = 4

for line in file_handle:
    clean_line = line.strip()
    line_parts = clean_line.split('\t')

    # if the row has empty for collision type,
    # print and break
    if line_parts[column_of_interest] == '':
        print(line_parts)
        break