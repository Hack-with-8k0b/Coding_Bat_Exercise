#Mine

def end_other(a, b):
    x = a.lower()
    y = b.lower()
    a_len = len(x)
    b_len = len(y)

    if a_len > b_len:
        return x[-b_len:] == y
    elif b_len > a_len:
        return y[-a_len:] == x
    elif a_len == b_len:
        return x == y

"""
~~~~~~Expected~~~~~~

def end_other(a, b):
  a = a.lower()
  b = b.lower()
  return (b.endswith(a) or a.endswith(b))

"""

print(end_other('Hiabc', 'abc'))
print(end_other('AbC', 'HiaBc'))
print(end_other('abc', 'abXabc'))