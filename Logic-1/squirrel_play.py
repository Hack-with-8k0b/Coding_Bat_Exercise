#Mine

from operator import is_


def squirrel_play(temp, is_summer):
    if temp >= 60:
        if is_summer:
            return temp <= 100
        else:
            return temp <= 90
    return False

"""
~~~~~~Expected~~~~~~



"""

print(squirrel_play(70, False))
print(squirrel_play(95, False))
print(squirrel_play(95, True))