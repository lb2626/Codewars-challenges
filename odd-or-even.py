""" This was one of the first challenges I ever did. I solved in a more 'classical way' when there are
one liner solutions such as the clever one shown undrneath my first solution.

Here is the question:

Task:
Given a list of numbers, determine whether the sum of its elements is odd or even.

Give your answer as a string matching "odd" or "even".

If the input array is empty consider it as: [0] (array with a zero).

Example:
odd_or_even([0])          ==  "even"
odd_or_even([0, 1, 4])    ==  "odd"
odd_or_even([0, -1, -5])  ==  "even"

"""


"""
my solution


Using the modulus remainder which is % in this case, I returned the required input. 
An integer that is divided by a modulus remainer is always even if it equals zero and anything else
is of course, odd.
"""

def odd_or_even(arr):
  if arr == []:
    arr == [0]
  if sum(arr) % 2 == 0:
    return 'even'
  if sum(arr) % 2 == 1:
    return 'odd'


def oddOrEven(arr):
    return 'even' if sum(arr) % 2 == 0 else 'odd'  #'clever' solution

