# Given a string, do some operations
# a string in python can be traited a list that store characters
# however, unlike a list, a string is ummutbale. meaning: it can't be changed

# initialiaze a string
a_string = "This is a strig"

print(a_string)

# given a string, letter = "ABCD"
letter = "ABCD"
# print the second character of the string
print("The second character of the letter string is: ", letter[1])

# print each character of the string
for character in letter:
    print(character)

# iterate over each character using the "for i in range()" style
for i in range(len(letter)):
    print(letter[i])

# let's try something more challeging
# write a fucntion that takes two strings and returns "Ture" 
# if the two strings are reverse of each other


