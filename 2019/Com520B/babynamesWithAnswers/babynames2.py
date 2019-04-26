import ssadata

for name in ssadata.boys.keys():
    if name in ssadata.girls:
        print(name)
