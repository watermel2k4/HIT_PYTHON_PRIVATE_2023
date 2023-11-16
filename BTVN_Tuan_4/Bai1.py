from datetime import datetime, timedelta
n = input()
input_date = datetime.strptime(n, "%d/%m/%Y")
end_year = datetime(input_date.year,12,31)
days = (end_year - input_date).days

print(days)
