import datetime
future=input("What is your 'future' date (in DD/MM/YYYY) ?")
futuredate=datetime.datetime.strptime(future,"%d/%m/%Y").date()
today=datetime.date.today();
days=futuredate-today;
print(days.days, 'days left');