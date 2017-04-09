
# 
# print "short" if the name is 5 or fewer characters
# print "medium" if the name is 6 to 10 characters
# print "long" if the name is 11 characters
# 

# TODO:
#   - what if you change "elif" to "if" below?


my_name = "1234"
if len(my_name) <= 5:
    print("short")
elif len(my_name) <= 10:
    print("medium")
else:
    print("superlong")
