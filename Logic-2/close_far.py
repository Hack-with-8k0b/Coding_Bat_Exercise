#Mine

def close_far(a, b, c):
    def close(l,m):
        if abs(l-m) <= 1:
            return True
        return False
    def far(n,o):
        if abs(n-o) >= 2:
            return True
        return False
    
    if close(a,b) and far(b,c) and far(a,c):
        return True
    elif close(a,c) and far(a,b) and far(b,c):
        return True
    return False
"""
~~~~~~Expected~~~~~~



"""

print(close_far(1, 2, 10))
print(close_far(1, 2, 3))
print(close_far(4, 1, 3))