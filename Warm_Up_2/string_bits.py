#Mine

def string_bits(str):
    return str[::2]

"""
~~~~~~Expected~~~~~~

def string_bits(str):
  result = ""
  # Many ways to do this. This uses the standard loop of i on every char,
  # and inside the loop skips the odd index values.
  for i in range(len(str)):
    if i % 2 == 0:
      result = result + str[i]
  return result 

"""

print(string_bits('Hello'))
print(string_bits('Hi'))
print(string_bits('Heeololeo'))