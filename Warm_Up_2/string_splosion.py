#Mine

def string_splosion(str):
    a = ''
    for i in range(len(str)+1):
        a += str[:i]
    return a

"""
~~~~~~Expected~~~~~~

def string_splosion(str):
  result = ""
  # On each iteration, add the substring of the chars 0..i
  for i in range(len(str)):
    result = result + str[:i+1]
  return result

"""

print(string_splosion('Code'))
print(string_splosion('abc'))
print(string_splosion('ab'))