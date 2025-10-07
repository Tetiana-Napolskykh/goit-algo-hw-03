from datetime import datetime, timedelta

current_date=datetime.now()
date_today=datetime.today()
print(current_date)
print(date_today)

print(current_date.date())
print(date_today.time())
print(current_date.year, current_date.month, current_date.day)

interval=timedelta(days=45)
print(current_date+interval) #day off
print(current_date-interval) #day on
count_days=(current_date+interval)-(current_date-interval)
print(count_days.days)


day_zero=datetime.fromtimestamp(0)
print(day_zero)

datetime_string = '1970:01:01 January Jan 02 02 00'
print(datetime.strptime(datetime_string, '%Y:%m:%d %B %b %H %I %M'))
print(current_date.strftime('%Y-%m:%d'), current_date)

current_date="2025-05-30"
requested_day=datetime.strptime(current_date'%Y-%m-%d').date()
print(requested_day)