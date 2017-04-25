import ssadata

all_values = ssadata.values()
least_common = 999999
for value in all_values:
    if value < least_common:
        least_common = value
