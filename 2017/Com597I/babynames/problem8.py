import ssadata

# how many boys names are also girls names?
# implementation details:
#   find all names in the boys data set that are
#   also keys in the girls data set.

num_shared_names = 0
for name in ssadata.boys:
    if name in ssadata.girls:
        num_shared_names = num_shared_names + 1

print(str(num_shared_names) + " names out of " + str(len(ssadata.boys)) + " are shared.")

num_shared_names = 0
for name in ssadata.girls:
    if name in ssadata.boys:
        num_shared_names = num_shared_names + 1

print(str(num_shared_names) + " names out of " + str(len(ssadata.girls)) + " are shared.")
