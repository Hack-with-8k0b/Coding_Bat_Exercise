#Mine

def front_times(str, n):
    if len(str) > 3:
        return str[:3]*n
    else:
        return str*n

"""
~~~~~~Expected~~~~~~

def front_times(str, n):
  front_len = 3
  if front_len > len(str):
    front_len = len(str)
  front = str[:front_len]
  
  result = ""
  for i in range(n):
    result = result + front
  return result 

"""

print(front_times('Chocolate', 2))
print(front_times('Chocolate', 3))
print(front_times('Abc', 3))