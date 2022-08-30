#Mine

def cat_dog(str):
    cat = 0
    dog = 0
    for i in range(len(str)-2):
        char = str[i:i+3]
#        print(char)
        if char == 'cat':
            cat += 1
        elif char == 'dog':
            dog += 1
    return cat == dog
    
"""
~~~~~~Expected~~~~~~



"""

print(cat_dog('catdog'))
print(cat_dog('catcat'))
print(cat_dog('1cat1cadodog'))