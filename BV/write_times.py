import datetime as dt

filestring="""
MYD04_3K.A2016361.1915.061.*
MYD04_3K.A2016362.1955.061.*
MYD04_3K.A2015007.1955.061.*
MYD04_3K.A2015001.2035.061.*
MYD04_3K.A2015003.2020.061.*
MYD04_3K.A2017001.2015.061.*
MYD04_3K.A2016364.1945.061.*
MYD04_3K.A2015005.2010.061.*
MYD04_3K.A2015002.1940.061.*
MYD04_3K.A2016363.2040.061.*
MYD04_3K.A2015006.1915.061.*
MYD04_3K.A2016365.2025.061.*
"""

the_dates=[]
for the_line in filestring.split():
    _,datestring,timestring,_,_=the_line.split('.')
    year=int(datestring[1:5])
    day=int(datestring[5:8])
    daynumber=int(day) - 1
    start_year = dt.date(year,1,1)
    the_date = start_year + dt.timedelta(days=daynumber)
    hour=int(timestring[:2])
    minute=int(timestring[2:4])
    the_dates.append((the_date,hour,minute))
print(the_dates[-1])
