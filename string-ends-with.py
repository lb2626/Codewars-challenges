
"""
Complete the solution so that it returns true if the first argument(string) passed in ends with the 2nd argument (also a string).

Examples:

solution('abc', 'bc') # returns true
solution('abc', 'd') # returns false

My solution is more of a logical one where you can see the steps taken to check the string, but in fact this can be solved very simply in one line

def solution(string, ending):
    return string.endswith(ending)


"""

def solution(string, ending):
  if ending == '':
    return True
  if string.endswith(ending):
    return True
  else:
    return False