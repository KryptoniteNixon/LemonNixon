# Q2 Hours in 7 weeks
print 7 * 7 * 24
# Q4 speed of light per nano sec
speed_of_light = 299800000. # meters per second
nano_per_sec = 1000000000. # 1 billion
# adding . to number gives it a decimal answer
nanodistance = speed_of_light / nano_per_sec
print nanodistance
#Q6
# Given the variables s and t defined as:
s = 'udacity'
t = 'bodacious'
# write Python code that prints out udacious
# without using any quote characters in
# your code.
print s[0:3] + t[4:]
#Q7
# Assume text is a variable that
# holds a string. Write Python code
# that prints out the position
# of the first occurrence of 'hoo'
# in the value of text, or -1 if
# it does not occur at all.
text = "first hoo"

print text.find("hoo")

#Q8
# Assume text is a variable that
# holds a string. Write Python code
# that prints out the position
# of the second occurrence of 'zip'
# in text, or -1 if it does not occur
# at least twice.


# Here are two example test cases:
#text = 'all zip files are zipped'
# >>> 18
# text = 'all zip files are compressed'
# >>> -1

text = "all zip files are zipped"

first_zip = text.find("zip")
second_zip = text.find('zip',first_zip + 1)
print second_zip
print first_zip


# Given a variable, x, that stores the
# value of any decimal number, write Python
# code that prints out the nearest whole
# number to x.
# If x is exactly half way between two
# whole numbers, round up, so
# 3.5 rounds to 4 and 2.5 rounds to 3.
# You may assume x is not negative.

# Hint: The str function can convert any number into a string.
# eg str(89) converts the number 89 to the string '89'

# Along with the str function, this problem can be solved
# using just the information introduced in unit 1.

# x = 3.14159
# >>> 3 (not 3.0)
# x = 27.63
# >>> 28 (not 28.0)
# x = 3.5
# >>> 4 (not 4.0)

x = 3.14159

print str(x*1)
