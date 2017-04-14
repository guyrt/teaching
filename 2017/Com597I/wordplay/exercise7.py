import scrabble

for character in 'abcdefghijklmnopqrstuvwxyz':
    words_with_most_of_character = []
    max_number_character_so_far = 0

    for word in scrabble.wordlist:
        number_of_character_in_this_word = word.count(character)
        if number_of_character_in_this_word == max_number_character_so_far:
            words_with_most_of_character.append(word)
        if max_number_character_so_far < number_of_character_in_this_word:
            max_number_character_so_far = number_of_character_in_this_word
            words_with_most_of_character = [word]

    print(max_number_character_so_far)
    print(words_with_most_of_character)
