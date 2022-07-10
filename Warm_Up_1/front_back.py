#Main
def front_back(str):
    if len(str) > 1:
        return str[-1] + str[1:-1] + str[0]
    else:
        return str

"""
Expected

def front_back(str):
  if len(str) <= 1:
    return str
  
  mid = str[1:len(str)-1]  # can be written as str[1:-1]
  
  # last + mid + first
  return str[len(str)-1] + mid + str[0]

"""

print(front_back('code'))
print(front_back('a'))
print(front_back('ab'))
