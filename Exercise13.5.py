import random

t = ['a', 'a', 'b']

def hist(x):
    """count the frequency and store in dictionary"""
    hist = {}
    for item in x:
        hist[item] = hist.get(item, 0) + 1
    return hist
    
hist = hist(t)

def choose_from_hist(hist):
    """The reverse of hist function, from dictionary to list, 
    then random choose an element"""
    list_ = []
    for key in hist:
        for i in range(0, hist[key]):
            list_.append(key)
    return random.choice(list_)
    

def stats():
    """Do the experiment for 10000 times"""
    
    a = 0
    b = 0
    for i in range(0, 10000):
        if choose_from_hist(hist) == 'a':
            a += 1
        else:
            b += 1
    print ("a: %.5f" % (a / 10000.0), "b: %.5f" % (b / 10000.0))
    

stats()