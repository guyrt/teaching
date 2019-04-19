import scrabble

# Find all words that start with 'a' and are 9 or more letters long.

for word in scrabble.wordlist:
    if word[0] == 'a' and len(word) >= 9:
            print(word)

