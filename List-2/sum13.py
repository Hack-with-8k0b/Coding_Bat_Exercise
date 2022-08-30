#Mine

def sum13(nums):
    sum = 0
    skip = 0
    if nums == []:
        return sum
    for i in nums:
        if skip == 1:
            skip = 0
        elif i != 13:
            sum += i
        elif i == 13:
            skip = 1
    return sum

"""
~~~~~~Expected~~~~~~

"""

print(sum13([1, 2, 2, 1]))
print(sum13([1, 1]) )
print(sum13([1, 2, 2, 1, 13]))
print(sum13([1, 2, 13, 2, 1, 13]))
print(sum13([13, 1, 2, 13, 2, 1, 13]))

