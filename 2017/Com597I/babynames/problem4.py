# how often does least common name occur

import ssadata

least_common_occurrences = 99999999999999999999
for name in ssadata.girls:
    if ssadata.girls[name] < least_common_occurrences:
        least_common_occurrences = ssadata.girls[name]

print(least_common_occurrences)

