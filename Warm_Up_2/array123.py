#Mine

def array123(nums):
    a = [1,2,3]
    for i in range(len(nums)-2):
        b = [nums[i],nums[i+1],nums[i+2]]
        if a == b:
            return True
    return False


"""
~~~~~~Expected~~~~~~

def array123(nums):
  # Note: iterate with length-2, so can use i+1 and i+2 in the loop
  for i in range(len(nums)-2):
    if nums[i]==1 and nums[i+1]==2 and nums[i+2]==3:
      return True
  return False 

"""

print(array123([1, 1, 2, 3, 1]))
print(array123([1, 1, 2, 4, 1]))
print(array123([1, 1, 2, 1, 2, 3]))