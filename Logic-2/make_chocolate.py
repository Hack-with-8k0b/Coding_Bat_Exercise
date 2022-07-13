#Mine

def make_chocolate(small, big, goal):
    mod = goal%5
    if ((small + big*5) < goal) or mod > small:
        return -1
    elif big*5 < goal:
        return goal - big*5
    else:
        return mod

"""
~~~~~~Expected~~~~~~



"""

print(make_chocolate(4, 1, 9))
print(make_chocolate(4, 1, 10))
print(make_chocolate(4, 1, 7))
print(make_chocolate(6, 1, 10))
print(make_chocolate(1000, 1000000, 5000006))