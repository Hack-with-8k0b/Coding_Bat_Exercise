#Mine

def near_ten(num):
    return ((abs(num%10) <= 2) or abs((num%10)-10)<= 2) 

"""
~~~~~~Expected~~~~~~



"""

print(near_ten(12))
print(near_ten(17))
print(near_ten(19))