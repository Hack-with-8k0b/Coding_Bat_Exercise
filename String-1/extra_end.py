#Mine

def extra_end(str):
    return str[-2:]*3

"""
~~~~~~Expected~~~~~~

 def extra_end(str):
  end = str[-2:]
  return end + end + end

"""

print(extra_end('Hello'))
print(extra_end('ab'))
print(extra_end('Hi'))