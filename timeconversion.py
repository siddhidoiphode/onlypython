
s = input()
def timeConversion(s):
    hour = int(s[:2])
    period = s[8:]
    print(period)
    if period == "AM":  # AM case
        if hour == 12:
            hour = 0
    elif period == "PM":
        if hour < 12:
            hour += 12

    return f"{hour:02}{s[2:8]}"

result = timeConversion(s)
print(result)
