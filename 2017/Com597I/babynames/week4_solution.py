import ssadata

hist = {}

for key in ssadata.boys:
    first_letter = key[0]
    value = ssadata.boys[key]
    if first_letter not in hist:
        hist[first_letter] = 0
    hist[first_letter] = hist[first_letter] + value

for key in ssadata.girls:
    first_letter = key[0]
    value = ssadata.girls[key]
    if first_letter not in hist:
        hist[first_letter] = 0
    hist[first_letter] = hist[first_letter] + value


print(hist)
