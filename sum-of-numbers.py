
"""
Codewars doesn't really give a great explanation of what they would like you to do. So here is one...

Given two integers a and b, which can be positive or negative, find the sum of all the numbers in between (including the start and end) 
and return it. If the two numbers are equal return a or b. If a and b are equal, return a or b.

Note: a and b are not ordered!

So if both are equal, I'm just going to return a.

Next, we need to start from the smaller number to be able to loop through the integers and add them together.
I'm using the sum method to add the numbers within the range of +1. And that's it!
You could also do a simpler looking for loop and add the sums to a variable which starts at 0.

For example
n = 0

elif a > b:
    for i in range(b, a +1):
        n += i
"""




def get_sum(a,b):
    if a == b:                               
        return a
    elif a < b:
        return sum(range(a, b +1))
    elif a > b:
        return sum(range(b,a +1))
  


