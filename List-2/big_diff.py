#Mine

def big_diff(nums):
    larg = 0
    small = 10000000
    for i in nums:
        small = min(i, small)
        larg = max(larg, i)
    return (larg - small)
  

"""
~~~~~~Expected~~~~~~

"""

print(big_diff([10, 3, 5, 6]))
print(big_diff([2, 10, 7, 2]))
print(big_diff([7, 2, 10, 9]))
