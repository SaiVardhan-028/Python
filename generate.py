#import random

#coin = random.choice(["heads","trails"])
#print(coin)


# Example : 1 ON FROM 
#from random import choice

#coin = choice(["heads","trails"])
#print(coin)

#Example : 2 ON RANDOM.RANDINT(A,B)
#import random

#num = random.randint(0000,9999)
#print(num)

#Example : 3 ON RANDOM.SHUFFLE(X)
#import random

#cards = ["jack","queen","king","ace"]
#random.shuffle(cards)
#for card in cards:
#    print(card)
    

#Example : 4 ON STATISTICS
#import statistics
#print(statistics.mean([100,95]))


#import sys
#if len(sys.argv) < 2:
#    sys.exit("Too few arguments")
#elif len(sys.argv) > 2:
#    sys.exit("Too many arguments")
#else:
#    print("hello, my name is", sys.argv[1])
    

import sys
if len(sys.argv) < 2:
    sys.exit("Too few arguments")
else:
    sys.exit("Too many arguments")

for arg in sys.argv[1:]:
    print("hello, my name is",arg)   


