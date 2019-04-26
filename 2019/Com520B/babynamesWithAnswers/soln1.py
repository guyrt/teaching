import ssadata

# print my own name's count
boys_count = ssadata.boys['tommy']
print("There are " + str(boys_count) + " boys named tommy")

if 'tommy' in ssadata.girls:
    girls_count = ssadata.girls['tommy']
    print("There are " + str(girls_count) + " girls named tommy")
else:
    print("There are no girls named tommy")
