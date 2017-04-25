# open a file for reading.
file_handle = open("sdot_collisions_seattle.csv", "r")

# build a histogram of collision types

hist = {}  # collision type => number of collisions
column_of_interest = 36

# get the header row
header = file_handle.readline()
header_list = header.strip().split(',')

for line in file_handle:
    clean_line = line.strip()
    line_parts = clean_line.split(',')

    if line_parts[column_of_interest] == '2':
        print(line_parts)
        print(len(line_parts))
        break

print(header_list)
print(len(header_list))