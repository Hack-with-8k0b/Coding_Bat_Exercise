#Mine

def centered_average(nums):
    larg = 0
    small = 10000000
    for i in nums:
        small = min(i, small)
        larg = max(larg, i)
    
    nums.pop(nums.index(larg))
    nums.pop(nums.index(small))

    return int(sum(nums)/len(nums))



"""
~~~~~~Expected~~~~~~

"""

print(centered_average([1, 2, 3, 4, 100]))
print(centered_average([1, 1, 5, 5, 10, 8, 7]))
print(centered_average([-10, -4, -2, -4, -2, 0]))
