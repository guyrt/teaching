# Example of nested loops.
# TODO:
#   - why did I have to use "str" function below when I printed? (hint: think about each variable's type)
#   - Uncomment the last print statement. How often does it print? Why?
#   - Modify this code to print only if the product is a multiple of 2.

small_numbers = range(5)
multipliers = [1, 2, 3, 4, 5]  # == range(1, 6)

for number in small_numbers:
    for multiplier in multipliers:
        print(str(number) + " * " + str(multiplier) + " == " + str(multiplier * number))
   # print("Done with " + str(number))