import scrabble

longest_word_so_far = ''
for word in scrabble.wordlist:
    hist = {}
    for letter in word:
        hist[letter] = True
    unique_chars = len(word) == len(hist)
    if unique_chars:
        if len(word) >= len(longest_word_so_far):
            longest_word_so_far = word

print(longest_word_so_far)