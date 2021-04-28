from datetime import date, datetime


today=date.today()

print(today)
year = today.year
month= today.month
day=today.day

print("오늘 날짜 : {0}" .format(today))
print("연도 : {0}" .format(year))
print("월 : {0}" .format(month))
print("일 : {0}" .format(day))

print("------------")
now= datetime.now()

year= now.day
hour=now.hour
minute=now.minute
second=now.second
microsecond=now.microsecond

print("guswo s")