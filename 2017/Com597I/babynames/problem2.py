import ssadata

most_occurences = 0
for girl in ssadata.girls:
    if ssadata.girls[girl] > most_occurences:
        most_occurences = ssadata.girls[girl]
        most_popular_name = girl

print("Most popular name is " + most_popular_name)
