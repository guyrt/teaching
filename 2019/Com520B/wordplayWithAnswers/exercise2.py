import scrabble

# comment
longword = ""
for word in scrabble.wordlist:
    if len(word) >= len(longword) and word[0] == "q":
        longword = word
        #print(longword)

length_of_longest_word = len(longword)
print(length_of_longest_word)

# rerun the loop. find q word that are length_of_longest_word long
for word in scrabble.wordlist:
    # find words that are as long as known longest and start with q
    # print them.
    if len(word) == length_of_longest_word and word[0] == 'q':
        print(word)





