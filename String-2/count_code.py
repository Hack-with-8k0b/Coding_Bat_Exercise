#Mine

def count_code(str):
    c = 0
    for i in range(len(str)-3):
        char = str[i:i+4]
        if char[0] == 'c' and char[1] == 'o' and char[3] == 'e':
            c += 1
    return c

"""
~~~~~~Expected~~~~~~



"""

print(count_code('aaacodebbb'))
print(count_code('codexxcode'))
print(count_code('cozexxcope'))