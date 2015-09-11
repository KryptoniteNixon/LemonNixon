
# variable
age = 23
print age * 365

#string needs the same "" or ''
print 'hello'
print "hello"
hello = "howdy"
print hello

#variable is not constant changes for most recently assigned
name = "Devin"
print name
name = "Tanner"
print name

#only * works as a type for strings no + or / or -
name1 = "Tanner"
print name * 10


# indexing 0,1,2,3....
s = "Devin"
print s[3]
print (s + s)

# sub sequence, : range between x and y
s = "audacity"
print "U" + s[2:]
print s[:3] + s[3:]
print s + s[0:-1+1]

# .find opertaion -1 when it can't find
quote = 'Hey there whats up'
print quote.find('there')
print quote[4:]
print 'west'.find('test')
print quote.find(quote+'!!!')+1
print quote.find('t',9)

# .find operation with numbers
s = 'dog'
t = 'cat'
i = 'bird'

print s.find(t,i)
print s[i:].find(t)
print s.find(t)[:i]
print s[i:].find(t)+i
