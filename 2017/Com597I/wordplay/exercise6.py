import scrabble

for word in scrabble.wordlist:
    a_index = word.find('a')
    e_index = word.find('e')
    i_index = word.find('i')
    o_index = word.find('o')
    u_index = word.find('u')
    if a_index >= 0 and a_index < e_index and e_index < i_index and i_index < o_index and o_index < u_index:
        print(word)