# open a file for reading.
file_handle = open("sdot_collisions_seattle.txt", "r")

# build a histogram of collision types

hist = {}  # collision type => number of collisions
column_of_interest = 4

for line in file_handle:
    clean_line = line.strip()
    line_parts = clean_line.split('\t')

    collision_type = line_parts[column_of_interest]
    if collision_type not in hist:
        hist[collision_type] = 0
    hist[collision_type] = hist[collision_type] + 1

print(hist)
