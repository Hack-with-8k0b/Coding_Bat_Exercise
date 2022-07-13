#Mine

def in1to10(n, outside_mode):
    if outside_mode:
        return (n >= 10) or (n <= 1)
    return (n <= 10) and (n >= 1)

"""
~~~~~~Expected~~~~~~



"""

print(in1to10(5, False))
print(in1to10(11, False))
print(in1to10(11, True))