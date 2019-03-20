# strip
mystr = "   hello   "
print(mystr.strip())

# replace
a = "abc"
b = a.replace("a", "f")
print (b)

# find(sub[, start[, end]])
print ('Py' in 'Python')

def myfind(mystr, mychar):
    for i in range(len(mystr)):
        if mystr[i] == mychar:
            return i
    print("There is no this char.")

myfind('banana', 'x')




