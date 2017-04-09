# What is the longest word that starts with a 'q'?

# Since more than one word is as long as the longest q word, let's find them all.

import scrabble

longest_word_length_so_far = 0
longest_words = []  # empty list.

for word in scrabble.wordlist:
    if word[0] == 'q':
        # If the current q word is longer than the longest q word we've seen so far, then
        # save it as the longest word.
        current_word_length = len(word)
        if current_word_length == longest_word_length_so_far:
            longest_words.append(word)
        elif current_word_length > longest_word_length_so_far:  # NOTE: I'm comparing length of current word to the stored length.
            longest_word_length_so_far = len(word)
            print("New longest word: " + word)
            longest_words = [word]  # overwrite longest_words with a new list that contains one word.

print("The longest words are: ")
print(longest_words)

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
The longest words are:
['quadragenarians', 'quadringenaries', 'quadripartition', 'quadrisyllables', 'quadrivalencies', 'quadruplicating', 'quadruplication', 'quadruplicities', 'quantifications', 'quarrelsomeness', 'quarterfinalist', 'quartermistress', 'quatercentenary', 'quattrocentisms', 'quattrocentists', 'querulousnesses', 'questionability', 'quicksilverings', 'quincentenaries', 'quincentennials', 'quingentenaries', 'quinquagenarian', 'quinquevalences', 'quintuplicating', 'quintuplication', 'quizzifications', 'quodlibetarians', 'quodlibetically']
'''