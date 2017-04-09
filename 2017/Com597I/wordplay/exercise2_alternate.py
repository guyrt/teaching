# What is the longest word that starts with a 'q'?

# See `exercise2.py` for details. 
# The output differs here. Can you figure out why? Hint: only one character differs!

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
New longest word: qabala
New longest word: qabalah
New longest word: qabalahs
New longest word: qabalism
New longest word: qabalisms
New longest word: qabalistic
New longest word: qinghaosus
New longest word: quackeries
New longest word: quacksalver
New longest word: quacksalvers
New longest word: quacksalving
New longest word: quadragenarian
New longest word: quadragenarians
New longest word: quadringenaries
New longest word: quadripartition
New longest word: quadrisyllables
New longest word: quadrivalencies
New longest word: quadruplicating
New longest word: quadruplication
New longest word: quadruplicities
New longest word: quantifications
New longest word: quarrelsomeness
New longest word: quarterfinalist
New longest word: quartermistress
New longest word: quatercentenary
New longest word: quattrocentisms
New longest word: quattrocentists
New longest word: querulousnesses
New longest word: questionability
New longest word: quicksilverings
New longest word: quincentenaries
New longest word: quincentennials
New longest word: quingentenaries
New longest word: quinquagenarian
New longest word: quinquevalences
New longest word: quintuplicating
New longest word: quintuplication
New longest word: quizzifications
New longest word: quodlibetarians
New longest word: quodlibetically
The longest word is quodlibetically
'''
