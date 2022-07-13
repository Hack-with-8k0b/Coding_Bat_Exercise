#Mine

def cigar_party(cigars, is_weekend):
    if not is_weekend:
        if cigars >= 40 and cigars <= 60:
            return True
    elif is_weekend:
        if cigars>= 40:
            return True
    return False

"""
~~~~~~Expected~~~~~~

def cigar_party(cigars, is_weekend):
  if is_weekend:
    return (cigars >= 40)
  else:
    return (cigars >= 40 and cigars <= 60)

"""

print(cigar_party(30, False))
print(cigar_party(50, False))
print(cigar_party(70, True))