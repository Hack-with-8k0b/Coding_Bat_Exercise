#Mine

def front3(str):
    return str[:3]*3

"""
~~~~~~Expected~~~~~~

def front3(str):
  # Figure the end of the front
  front_end = 3
  if len(str) < front_end:
    front_end = len(str)
  front = str[:front_end]
  return front + front + front 
  
  # Could omit the if logic, and write simply front = str[:3]
  # since the slice is silent about out-of-bounds conditions.

"""

print(front3('Java'))
print(front3('Chocolate'))
print(front3('abc'))