#Mine

def string_match(a, b):

    def split_and_list(a):
        list1 = []
        for i in range(len(a)-1):
            list1.append(a[i]+a[i+1])
        return list1

    c = split_and_list(a)
    d = split_and_list(b)

    num = 0
    count = 0

    if len(c) > len(d):
        num = len(d)
    else:
        num = len(c)

    for i in range(num):
        if c[i] == d[i]:
            count += 1

    return(count)

"""
~~~~~~Expected~~~~~~

 def string_match(a, b):
  # Figure which string is shorter.
  shorter = min(len(a), len(b))
  count = 0
  
  # Loop i over every substring starting spot.
  # Use length-1 here, so can use char str[i+1] in the loop
  for i in range(shorter-1):
    a_sub = a[i:i+2]
    b_sub = b[i:i+2]
    if a_sub == b_sub:
      count = count + 1

  return count

"""

print(string_match('xxcaazz', 'xxbaaz'))
print(string_match('abc', 'abc'))
print(string_match('abc', 'axc'))