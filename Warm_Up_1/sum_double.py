#Mine
def sum_double(a, b):
    if a == b:
        return (a+b)*2
    else:
        return (a+b)

"""
~~~~~~Expected~~~~~~

def sum_double(a, b):
  # Store the sum in a local variable
  sum = a + b
  
  # Double it if a and b are the same
  if a == b:
    sum = sum * 2
  return sum

"""

print(sum_double(1, 2))
print(sum_double(3, 2))
print(sum_double(2, 2))