
"""

This was a fun challenge to solve and I managed touse a one line solution which is not completely
necessary but it's definitely nice to see it. One fact I learned while reaing 'Learning Python' is
that for list comprehensions this type of one line solution can run up to twice as fast as a more
'conventional one'. Not that it matters right now but still.

Here's the question: 

In this kata you will create a function that takes a list of non-negative integers and strings and returns a new list with the strings filtered out.

Example
filter_list([1,2,'a','b']) == [1,2]
filter_list([1,'a','b',0,15]) == [1,0,15]
filter_list([1,2,'aasf','1','123',123]) == [1,2,123]

And here's the solution:

"""

def filter_list(l):
  return [x for x in l if type(x) == int]

"""
So I'm returning x which is run through a for loop and checked if the class type of x is an integer.
Pretty cool.


"""