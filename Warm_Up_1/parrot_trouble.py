#Main
def parrot_trouble(talking, hour):
    if talking:
        if (7 > hour) or (hour > 20):
            return True
        else:
            return False
    return False

"""

Expected 

def parrot_trouble(talking, hour):
  return (talking and (hour < 7 or hour > 20))
  # Need extra parenthesis around the or clause
  # since and binds more tightly than or.
  # and is like arithmetic *, or is like arithmetic +

"""

print(parrot_trouble(True, 6))
print(parrot_trouble(True, 7))
print(parrot_trouble(False, 6))
