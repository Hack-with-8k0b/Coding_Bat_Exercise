#Mine
def sleep_in(weekday, vacation):
    if not weekday or vacation:
        return True
    else:
        return False

"""
~~~~~~Expected~~~~~~

def sleep_in(weekday, vacation):
  if not weekday or vacation:
    return True
  else:
    return False
  # This can be shortened to: return(not weekday or vacation)

"""


print(sleep_in(False, False))
print(sleep_in(True, False))
print(sleep_in(False, True))