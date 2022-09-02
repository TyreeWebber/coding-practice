# Strings
# A string can contain numbers, letters and symbols
# Declaration examples

# Single line string
string = "This is an example of a string"

# Multi line string
a_world_of_dew = """A world of dew,
And within every dewdrop
A world of struggle."""

# Escaping characters
# Typing "There's a snake in my boot!" will cause problems. 
# Instead type is as follows
correct = 'There\'s a snake in my boot'

# Access by Index
# Each character in a string is assigned a number. This number is called the index, Python is is similar to JavaScript in that it's 0 indexed and so the first value is 0 and the second value is 1.
# Example

r = "tyree"[2]

# When printed, the value of the variable r will be (surprise!) r.

#String methods
# len()
# the len() method stands for length and it works similarly to .length in JavaScript where it returns the number of characters in a string

dog_name = "Kaiser"

# len(dog_name) would return 6 as there are 6 characters in Kaiser's name

# lower()
# lower() works similarly to the .toLowerCase() function in JavaScript where it will turn the string into all lowercase.

