import scrabble

# Find at least one word that uses all five vowels in order.
for word in scrabble.wordlist:
    if 'a' in word:
        if word.find('a') < word.find('e') < word.find('i') < word.find('o') < word.find('u'):
            print(word)
