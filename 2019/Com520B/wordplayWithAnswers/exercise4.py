import scrabble

# You need a word that matches "a*ey" (here "*" means any letter). Are there any words that match?
for word in scrabble.wordlist:
    if word[0] == 'a' and word[2] == 'e' and word[3] == 'y' and len(word) == 4:
        print(word)

# alternate implemetation:
for word in scrabble.wordlist:
    for letter in 'abcdefghijklmnopqrstuvwxyz':
        if 'a' + letter + 'ey' in word:
            print(word)
