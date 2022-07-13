#Mine

def alarm_clock(day, vacation):
    if vacation:
        if day == 0 or day == 6:
            return "off"
        return "10:00"
    if day == 0 or day == 6:
        return "10:00"
    return "7:00"

"""
~~~~~~Expected~~~~~~



"""

print(alarm_clock(1, False))
print(alarm_clock(5, False))
print(alarm_clock(0, False))