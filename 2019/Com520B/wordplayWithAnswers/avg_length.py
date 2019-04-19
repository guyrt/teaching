import scrabble

# Find average number of characters in words
total_word_lengths = 0
total_words = 0
for word in scrabble.wordlist:
    total_word_lengths = total_word_lengths + len(word)
    total_words = total_words + 1

print(total_word_lengths / total_words)
