#Mine

def sum67(nums):
    sum = 0
    skip = 0
    if nums == []:
        return sum
    for i in nums:
        if skip != 1:
            if i == 6:
                skip = 1
            else:
                sum += i
        else:
            if i == 7:
                skip = 0

    return sum

"""
~~~~~~Expected~~~~~~

"""

print(sum67([1, 2, 2]))
print(sum67([1, 2, 2, 6, 99, 99, 7]))
print(sum67([1, 1, 6, 7, 2]))
