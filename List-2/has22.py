#Mine

def has22(nums):
    temp = 0
    for i in nums:
        if temp == i == 2:
            temp = i
            return True
        else:
            temp = i
    return False

    
"""
~~~~~~Expected~~~~~~

"""

print(has22([1, 2, 2]))
print(has22([1, 2, 1, 2]))
print(has22([2, 1, 2]))