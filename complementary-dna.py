"""
This challenge was to return the DNA pairs which compliment each other. 
For those of you who remember your biology classes, this means that you need to pair up nucleotides with each other.

Here are the test cases:

DNA_strand ("ATTGC") # return "TAACG"

DNA_strand ("GTAT") # return "CATA"

So in the test cases you can see that G is replaced with C, A is replaced with T and vice versa. 

Here's my solution:
"""


def DNA_strand(dna):

  result = ''
  
  for i in range(0, len(dna), 1):
    if dna[i] == 'A':
      result += 'T'
    elif dna[i] == 'T':
      result += 'A'
    elif dna[i] == 'G':
      result += 'C'
    elif dna[i] == 'C':
      result += 'G' 
return result


""" 
 For this solution I created an empty string because otherwise I would have run into trouble if I had just simply replaced A with T
 because with no empty string to start, this wouldn't pass all of the test cases (just try it).
  
 I ran a standard for loop throughout the length of the string which was passed into the function and then I replaced each instance
 with its corrosponding pair at position [i] and then I added that to the result.
  
Finally we return a full result and the string has of course been added to the result. 

I hope this explained to beginners how you might appoach a problem like this. 
"""