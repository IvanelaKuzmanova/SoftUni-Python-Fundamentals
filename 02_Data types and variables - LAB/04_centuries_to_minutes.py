centuries = int(input())

years = centuries * 100

days_per_year = 365.2422

days = years * days_per_year

days = int(days)

hours = days * 24

minutes = hours * 60

print(f"{centuries} centuries = {years} years = {days} days = {hours} hours = {minutes} minutes")