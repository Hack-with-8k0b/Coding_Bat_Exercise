#Mine
def missing_char(str, n):
    a = ''
    for i in str:
        if i != str[n]:
            a += i
    return a

"""
Expected 

def missing_char(str, n):
  front = str[:n]   # up to but not including n
  back = str[n+1:]  # n+1 through end of string
  return front + back
  
"""

print(missing_char('kitten', 1))
print(missing_char('kitten', 0))
print(missing_char('kitten', 4))