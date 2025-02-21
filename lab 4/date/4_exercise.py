import datetime
date1=datetime.datetime(2025,2,21,14,30,0)
date2=datetime.datetime(2025,2,20,12,15,0)
diff=date1-date2
diffday=diff.days*24*60*60
sec=diff.seconds
print(diffday+sec)