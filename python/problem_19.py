import calendar

sunday = 6
day = 0

print(sum(1 
          for year in range(1901,2000+1)
          for month in range(1,12+1)
          if calendar.monthrange(year, month)[day] == sunday))