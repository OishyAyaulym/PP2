import datetime
yesterday=datetime.date.today()-datetime.timedelta(days=1)
tomorrow=datetime.date.today()+datetime.timedelta(days=1)
print("yesterday: ", yesterday)
print("today: ", datetime.date.today())
print("tomorrow: ",tomorrow)