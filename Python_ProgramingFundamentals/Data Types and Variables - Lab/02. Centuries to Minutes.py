century = int(input())
years = century * 100
days = years * 365.2422
hours = int(days) * 24
minutes = hours * 60


print(f"{century} centuries = {years} years = {int(days)} days = {hours} hours = {minutes} minutes")
