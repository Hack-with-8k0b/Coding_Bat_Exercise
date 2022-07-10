#Mine
def monkey_trouble(a_smile, b_smile):
    if a_smile == b_smile:
        return True
    else:
        return False

"""
~~~~~~Expected~~~~~~

def monkey_trouble(a_smile, b_smile):
  if a_smile and b_smile:
    return True
  if not a_smile and not b_smile:
    return True
  return False
  ## The above can be shortened to:
  ##   return ((a_smile and b_smile) or (not a_smile and not b_smile))
  ## Or this very short version (think about how this is the same as the above)
  ##   return (a_smile == b_smile)

"""


print(monkey_trouble(True, True))
print(monkey_trouble(False, False))
print(monkey_trouble(True, False))