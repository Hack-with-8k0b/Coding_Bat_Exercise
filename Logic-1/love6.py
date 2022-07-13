#Mine

def love6(a, b):
    if 6 in (a,b):
        return True
    elif a+b == 6:
        return True 
    elif abs(a-b) == 6:
        return True
    else:
        return False

"""
~~~~~~Expected~~~~~~



"""

print(love6(6, 4))
print(love6(4, 5))
print(love6(1, 5))