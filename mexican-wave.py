
L = 'Lukey'
new_L = []

for i, val in enumerate(L[:]):
    upper = L[i].upper()
    B = L[:i] + upper + L[i+1:]
    new_L.append(B)
print(new_L)

"""
So lets look at the solution:
First lets just make a new list that we can append the result to since strings are immutable.
Then we need to be able to access each iteration, so let's slice the string at and before position i with L[:i].
Next, we still need a capital letter as a character so we need to create one at position i. Let's add them together.
This doesn't quite work because as you can see the result looks like this:

['L']
['L', 'LU']
['L', 'LU', 'LuK']
['L', 'LU', 'LuK', 'LukE']
['L', 'LU', 'LuK', 'LukE', 'LukeY']

So how do we get the rest of the string?

Let's try concatenating one step ahead of i and accessing a slice of the string at the same time.
Then print the final result inside of the for loop.
This works because we are only adding ONE upper per iteration.
We're slicing up to i we're adding one upper case character and then we're doing it again until we reach the end
because of the iterations. The first one is added at index 2 and then it continues because it needs to reach the end.


['Lukey', 'LUkey', 'LuKey', 'LukEy', 'LukeY']

"""

