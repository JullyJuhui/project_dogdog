from datetime import date, timedelta

print(date.today())
print(date.today()+timedelta(days = 3))
print((date.today()+timedelta(days = 3)).isoformat())
