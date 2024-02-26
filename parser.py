import sqlite3
import sys


print('Please select a date')
day = input('Day: ')
month = input('Month: ')
year = input('Year: ')

if len(day) < 2:
    day = "0" + day
if len(month) < 2:
    month = "0" + month


db = sqlite3.connect('stats.sqlite3')
cur = db.cursor()
try:
    cur.execute(f'SELECT * FROM D{year + month + day}')
except Exception:
    print("No such day in database or date is wrong")
    sys.exit()

marks = cur.fetchall()


breakfast_marks = 0
users = len(marks)
for user in marks:
    try:
        breakfast_marks += int(user[0])
    except Exception:
        users -= 1
if users > 0:
    breakfast_middle_mark = round(breakfast_marks / users, 2)
else:
    breakfast_middle_mark = 0
del breakfast_marks


dinner_marks = 0
users = len(marks)
for user in marks:
    try:
        dinner_marks += int(user[2])
    except Exception:
        users -= 1
if users > 0:
    dinner_middle_mark = round(dinner_marks / users, 2)
else:
    dinner_middle_mark = 0
del dinner_marks


lunch_marks = 0
users = len(marks)
for user in marks:
    try:
        lunch_marks += int(user[1])
    except Exception:
        users -= 1
if users > 0:
    lunch_middle_mark = round(lunch_marks / users, 2)
else:
    lunch_middle_mark = 0
del lunch_marks


n = 3
if breakfast_middle_mark == 0:
    n -= 1
if lunch_middle_mark == 0:
    n -= 1
if dinner_middle_mark == 0:
    n -= 1

all_day_middle_mark = (breakfast_middle_mark + lunch_middle_mark + dinner_middle_mark) / n

print("")
print("")
print("")
print(f'Breakfast middle mark: {breakfast_middle_mark}⭐️')
print(f'Lunch middle mark: {lunch_middle_mark}⭐️')
print(f'Dinner middle mark: {dinner_middle_mark}⭐️')
print('')
print(f'All day middle mark: {all_day_middle_mark}⭐️')
print('')