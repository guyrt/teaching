raw_ages = [23, 24, 23, 35, 12, 13, 10, 7, 99, 13, 17, 12, 12, 12, 13]
hist = {}

bad_hist = [0] * (max(raw_ages) + 1)

for age in raw_ages:
    bad_hist[age] = bad_hist[age] + 1

print(bad_hist)

for age in raw_ages:
    if age in hist:
        hist[age] = hist[age] + 1
    else:
        hist[age] = 1
print(hist)