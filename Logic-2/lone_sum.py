#Mine

def lone_sum(a, b, c):
    if a == b == c:
        return 0
    elif a == b:
        return c 
    elif b == c:
        return a 
    elif a == c:
        return b
    return a+b+c 

"""
~~~~~~Expected~~~~~~

def lone_sum(a, b, c):
  sum = 0
  if a != b and a != c: sum += a
  if b != a and b != c: sum += b
  if c != a and c != b: sum += c
  
  return sum

"""

print(lone_sum(1, 2, 3))
print(lone_sum(3, 2, 3))
print(lone_sum(3, 3, 3))
