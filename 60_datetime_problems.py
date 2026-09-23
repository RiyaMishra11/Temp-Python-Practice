# File 60: Date and Time Problems
# 11 practice programs

from datetime import date,datetime,timedelta

# 1 Current date
today=date.today()
print("1.",today)

# 2 Formatted current time
print("2.",datetime.now().strftime("%d-%m-%Y %H:%M:%S"))

# 3 Custom date
d=date(2026,9,23)
print("3.",d)

# 4 Difference between dates
a=date(2026,1,1);b=date(2026,12,31)
print("4.",(b-a).days)

# 5 Add days
print("5.",d+timedelta(days=30))

# 6 Weekday
print("6.",d.strftime("%A"))

# 7 Parse date string
p=datetime.strptime("23-09-2026","%d-%m-%Y")
print("7.",p.date())

# 8 Calculate age
birth=date(2000,5,15)
age=today.year-birth.year-((today.month,today.day)<(birth.month,birth.day))
print("8.",age)

# 9 Leap year
def leap(y):return y%400==0 or (y%4==0 and y%100!=0)
print("9.",leap(2028))

# 10 Count weekdays
def weekdays(s,e):
    c=0
    while s<=e:
        c+=s.weekday()<5
        s+=timedelta(days=1)
    return c
print("10.",weekdays(date(2026,9,1),date(2026,9,30)))

# 11 Next Monday
def next_day(start,weekday):
    gap=(weekday-start.weekday())%7 or 7
    return start+timedelta(days=gap)
print("11.",next_day(d,0))
