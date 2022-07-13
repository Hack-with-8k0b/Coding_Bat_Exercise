#Mine

def sum2(nums):
    if len(nums) > 2:
        return sum(nums[:2])
    else:
        return sum(nums)

"""
~~~~~~Expected~~~~~~



"""

print(sum2([1, 2, 3]))
print(sum2([1, 1]))
print(sum2([1, 1, 1, 1]))