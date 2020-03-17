"""
Write a function that takes an array of numbers (integers for the tests) and a target number. It should find two different items in the array that, when added together, give the target value. The indices of these items should then be returned in a tuple like so: (index1, index2).

For the purposes of this kata, some tests may have multiple answers; any valid solutions will be accepted.

The input will always be valid (numbers will be an array of length 2 or greater, and all of the items will be numbers; target will always be the sum of two different items from that array).

Based on: http://oj.leetcode.com/problems/two-sum/

My solution:

Basially we need to add two integers in a list and check whether or not they add up to a target number.
For this I created a for loop which ran to the total length of the numbers -1. Why? Because we need 
to add a second for loop which starts one AFTER the first integer. We then check if when we add these
indexes if they add u to the target which is passed into the function and then return them.

Since this is a Leetcode question I suppose the most 'optimal' way is to create a hash table,
but I'm practicing the fundamentals here and that's something I can work on later.

"""



def two_sum(numbers, target):
  for i in range(len(numbers)-1):
    for j in range(i+1, len(numbers)):
      if numbers[i] + numbers[j] == target:
        return [i, j]