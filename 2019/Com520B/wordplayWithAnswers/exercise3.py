import scrabble

# Finding all words that end in nge
for word in scrabble.wordlist:
    if word[-1] == 'e' and word[-2] == 'g' and word[-3] == 'n':
        print(word)

# alternate using slicing.
for word in scrabble.wordlist:
    if word[-3:] == 'nge':
        print(word)
