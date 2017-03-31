'''
Created on Mar 30, 2017

@author: leem42

simpleCalculations.py performs a series of simple calculations given two values passed into 
the command line and then displays the results of those calculations

'''


import sys
a,b = int(sys.argv[1]), int(sys.argv[2])
print "a is ", a
print "b is ", b

# Calculations #

# Finding the sum of a and b #
print "Sum of a + b = " + (a + b )

# Finding the parity of a #
parity = (a % 2 == 0)
if parity:
    print "a is even"
else:
    print "a is odd"
    
# Swapping the values of a and b so that a contains the smaller value #
if( a >  b):
    c  = a
    a = b
    b = a

print "a now contains the smaller of the two values " + str(a)
print "b now contains the larger of the two values " + str(b)