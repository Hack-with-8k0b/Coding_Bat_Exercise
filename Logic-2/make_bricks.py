#Mine

def make_bricks(small, big, goal):
    a = small + big*5
    if not (goal > a):
        if goal == a:
            return True
        elif goal%5 <= small:
            return True
        elif goal == (big*5):
            return True
    return False

"""
~~~~~~Expected~~~~~~



"""

print(make_bricks(3, 1, 8))
print(make_bricks(3, 1, 9))
print(make_bricks(3, 2, 10))
print(make_bricks(1, 4, 11))
print(make_bricks(3, 2, 9))
print(make_bricks(1, 4, 12))
print(make_bricks(2, 1000000, 100003))
print(make_bricks(3, 2, 8))
print(make_bricks(1000000, 1000, 1000100))
