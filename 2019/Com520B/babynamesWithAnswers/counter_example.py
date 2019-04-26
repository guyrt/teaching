letters = ['a', 'b', 'a', 'b', 'a', 'c', 'd']

# count the letters
# should get: {'a': 3, 'b': 2, 'c': 2, 'd': 1}

my_counter = {}
for letter in letters:
    print("My letter is " + letter)
    print("The counter dict is " + str(my_counter))
    if letter in my_counter:
        my_counter[letter] += 1
    else:
        my_counter[letter] = 1
    print("The updated counter dict is " + str(my_counter))
    print()
    print()

print(my_counter)
