#Mine
def near_hundred(n):
    return (abs(n - 100) <= 10) or (abs(n - 200) <= 10)

"""

def near_hundred(n):
  return ((abs(100 - n) <= 10) or (abs(200 - n) <= 10))

"""
print(near_hundred(93))
print(near_hundred(90))
print(near_hundred(89))
print(near_hundred(193))
print(near_hundred(190))
print(near_hundred(189))