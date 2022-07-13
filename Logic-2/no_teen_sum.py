#Mine

def no_teen_sum(a, b, c):
    def fix_teen(n):
        if (n >= 13) and (n <= 19):
            if n == 15 or n == 16:
                return False    
            return True
        return False

    num = [a,b,c]
    b = []
    for i in num:
        if not fix_teen(i):
            b.append(i)
    return sum(b)

"""
~~~~~~Expected~~~~~~



"""

print(no_teen_sum(1, 2, 3))
print(no_teen_sum(2, 13, 1))
print(no_teen_sum(2, 1, 14))