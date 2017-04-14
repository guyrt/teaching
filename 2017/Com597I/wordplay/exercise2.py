# What is the longest word that starts with a 'q'?

# This is a simple solution.
# The key idea here is to store information outside the loop. Here, we store
# the longest word we've seen so far. At every iteration in the loop,
# we check whether the current word is longer than the longest word we've seen so far.

import scrabble

longest_word_so_far = ''  # note empty word: any "q" word is longer than this!
for word in scrabble.wordlist:
    if word[0] == 'q':
        # If the current q word is longer than the longest q word we've seen so far, then
        # save it as the longest word.
        if len(word) >= len(longest_word_so_far):
            longest_word_so_far = word
            print("New longest word: " + longest_word_so_far)

print("The longest word is " + longest_word_so_far)

'''
New longest word: qabala
New longest word: qabalah
New longest word: qabalahs
New longest word: qabalisms
New longest word: qabalistic
New longest word: quacksalver
New longest word: quacksalvers
New longest word: quadragenarian
New longest word: quadragenarians
The longest word is quadragenarians
'''
