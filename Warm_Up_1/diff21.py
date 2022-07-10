#Mine
def diff21(n):
    diff = abs(n-21)
    if n > 21:
        return diff*2
    else:
        return diff

"""
~~~~~~Expected~~~~~~

def diff21(n):
  if n <= 21:
    return 21 - n
  else:
    return (n - 21) * 2
"""

print(diff21(19))
print(diff21(10))
print(diff21(21))