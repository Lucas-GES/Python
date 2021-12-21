import calendar

print("Write the Month, the Day and the Year with spaces: ")
month, day, year = map(int, input().split())

result = calendar.weekday(year, month, day)

print("The day of the week that you have passed was: ", calendar.day_name [result].upper())
    
