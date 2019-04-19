import scrabble

# Print every other word that matches the condition in (1) above.
should_i_print = True
for word in scrabble.wordlist:
    if word[0] == 'a' and len(word) >= 9:
        if should_i_print:
            print(word)
            should_i_print = False
        else:
            should_i_print = True
#        should_i_print = not should_i_print


# alternate:
new_list = []
for word in scrabble.wordlist:
    if word[0] == 'a' and len(word) >= 9:
        new_list.append(word)
print(new_list[::2])