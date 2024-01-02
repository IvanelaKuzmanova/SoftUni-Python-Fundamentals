centuries = int(input())

years = centuries * 100

total_days = 0

for current in range(1, years + 1):

    days_per_year = 365

    if current % 4 == 0:
        days_per_year = 366

    total_days += days_per_year

hours = total_days * 24

minutes = hours * 60

print(minutes)