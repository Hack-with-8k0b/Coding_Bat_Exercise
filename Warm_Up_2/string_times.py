#Mine

def string_times(str, n):
    return str*n

"""
~~~~~~Expected~~~~~~

def string_times(str, n):
  result = ""
  for i in range(n):  # range(n) is [0, 1, 2, .... n-1]
    result = result + str  # could use += here
  return result

"""

print(string_times('Hi', 2))
print(string_times('Hi', 3))
print(string_times('Hi', 1))