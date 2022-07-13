#Mine

def rotate_left3(nums):
    b = nums.pop(0)
    nums.append(b)
    return nums


"""
~~~~~~Expected~~~~~~



"""

print(rotate_left3([1, 2, 3]))
print(rotate_left3([5, 11, 9]))
print(rotate_left3([7, 0, 0]))