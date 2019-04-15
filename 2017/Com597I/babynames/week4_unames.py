# we think that the nubmer of 'u' names
# is too small. let's check them!
# print name and number of children for
# every name that starts with u.

import ssadata

for key in ssadata.girls:
    if key[0] == 'u':
        print(key + " " + str(ssadata.girls[key]))

for key in ssadata.boys:
    if key[0] == 'u':
        print(key + " " + str(ssadata.boys[key]))