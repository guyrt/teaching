import scrabble

# Print all words containing 'uu'.
uu_words = []
for word in scrabble.wordlist:
    if 'uu' in word:
        #print(word)
        uu_words.append(word)

      #  print(len(uu_words))