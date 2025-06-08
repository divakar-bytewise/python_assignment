import calendar

def finding_day(m, d, y):
    w = calendar.weekday(y, m, d)
    
    if w == 0:
        return "MONDAY"
    elif w == 1:
        return "TUESDAY"
    elif w == 2:
        return "WEDNESDAY"
    elif w == 3:
        return "THURSDAY"
    elif w == 4:
        return "FRIDAY"
    elif w == 5:
        return "SATURDAY"
    else:
        return "SUNDAY"

if __name__ == '__main__':
    m, d, y = map(int, input("Enter month, day, year: ").split())
    result = finding_day(m, d, y)
    print(result)
