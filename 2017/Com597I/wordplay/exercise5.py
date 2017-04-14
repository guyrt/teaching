import scrabble

print_me = True
for word in scrabble.wordlist:
    if word[0] == 'a' and len(word) > 9:
        if print_me:
            print(word)
        
        
