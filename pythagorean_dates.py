from datetime import timedelta, date

def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)

start_date = date(2020, 1, 1)
end_date = date(3000, 12, 31)

for single_date in daterange(start_date, end_date):
    date_str = single_date.strftime("%d-%m-%Y")
    day = single_date.day
    month = single_date.month
    year = int(str(single_date.year)[-2:])

    if day**2 + month**2 == year**2:
        print(date_str)
