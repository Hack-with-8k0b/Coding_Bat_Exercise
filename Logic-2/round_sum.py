#Mine

def round_sum(a, b, c):
    def round10(num):
        l = int(num/10)
        if (num%10) < 5:
            return l*10
        elif (num%10) >= 5:
            return (l*10)+10
        
    n = [a,b,c]
    m = []
    for i in n:
        m.append(round10(i))
    return sum(m)

"""
~~~~~~Expected~~~~~~

def round_sum(a, b, c):
  return round10(a) + round10(b) + round10(c)
  
def round10(num):
  mod = num % 10
  num -= mod
  if mod >= 5: num += 10
  return num


"""

print(round_sum(16, 17, 18))
print(round_sum(12, 13, 14))
print(round_sum(6, 4, 4))