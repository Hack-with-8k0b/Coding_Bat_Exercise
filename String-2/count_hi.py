#Mine

def count_hi(str):
    c = 0
    for i in range(len(str)):
        char = str[i:i+2]
        if char == 'hi':
            c += 1
    return c
    
"""
~~~~~~Expected~~~~~~

def count_hi(str):
  sum = 0
  ## Loop to length-1 and access index i and i+1
  ## in the loop.
  for i in range(len(str)-1):
    if str[i:i+2] == 'hi':
      sum = sum + 1
  return sum

"""

print(count_hi('abc hi ho'))
print(count_hi('ABChi hi'))
print(count_hi('hihi'))