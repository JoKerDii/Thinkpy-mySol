"""There is a string method called count that is similar to the function in “Looping and
Counting” on page 89. Read the documentation of this method and write an invocation
that counts the number of a’s in 'banana'."""

mystr = 'banana'
mychar = 'a'
mycount = mystr.count(mychar) 
print(mycount)


def newcount(word, target):
    i = 0
    for letter in word:
        if letter == target:
            i += 1
    return i
# test
# print (newcount(mystr, mychar))