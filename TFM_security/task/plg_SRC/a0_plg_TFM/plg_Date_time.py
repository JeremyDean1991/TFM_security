

from a0_items import *

from datetime import * 
import time  
import datetime
from datetime import datetime, timedelta  
         


def get_date_today ():

   date_today = date.today()
   
   return date_today
   


# https://www.programiz.com/python-programming/datetime/strftime     
def get_date_time_now (dt_format):
   
   # datetime object containing current date and time
   now = datetime.now()
 
   match dt_format:
   
      case "1":
         # dd-mm-YY H:M:S
         dt_string = now.strftime("%d-%m-%Y %H:%M:%S %p")  
         print("date and time =", dt_string)
         
         return dt_string
         
      case "2": 
         # dd_mm_YY_H_M_S
         dt_string = now.strftime("%d #0 %m #1 %Y #2 %H_%M_%S_%p")  
         print("date and time =", dt_string)
         
         return dt_string  

      case "3":
         # dd_mm_YY_H_M_S
         dt_string = now.strftime("%d #0 %b #1 %Y #2 %H %M %S %p")  
         print("date and time =", dt_string)
         
         return dt_string        
         
     
#get_date_time_now (dt_format='3')


#calculate ALL dates between two dates - https://www.tutorjoes.in/Python_example_programs/get_list_of_dates_between_two_dates_in_python
def get_date_range(start_date, end_date):

    LIST_date = []

    for n in range(int ((end_date - start_date).days)+1):
         
        date_value = start_date + timedelta(n)
        #print (date_value.strftime("%d_%b_%Y"))
        
        LIST_date.append (date_value.strftime("%d_%b_#%Y"))
     
    print (LIST_date) 
    return LIST_date
        
#get_date_range(start_date= date(2024, 1, 1), end_date= date(2024, 12, 31) )




def datetime_range(start, end, delta):

    current = start
    
    while current < end:
        yield current
        current += delta




def output_dt_range (start_dt, end_dt, delta):

   dt_format_1 = "%d #0 %m #1 %Y #2 %H_%M_%S_%p"
   dt_format_2 = '%Y-%m-%d T%H:%M Z'
   dt_format_3 = "%d #0 %b #1 %Y #2 %H %M %S %p"
   dt_format_4 = "%d_%b_#%Y"

   LIST_dt = []
  
   LIST_dt_range = datetime_range(start, end, delta) 

   for dt in LIST_dt_range:

      dt_output = dt.strftime(dt_format_4)
      print (dt_output)
   
      LIST_dt.append (dt_output)   
   
      
   #print (LIST_dt)
   print (len(LIST_dt))
   return LIST_dt

'''
start = datetime(2016, 1, 1, 0)
end = datetime(2016, 12, 31, 0)

#delta_secs = timedelta(seconds=60)
#delta_mins = timedelta(minutes=60)
#delta_hrs = timedelta(hours=10)
delta_days = timedelta(days=1)


output_dt_range (start_dt=start, end_dt=end, delta=delta_days )
'''




import pandas as pd

#print (pd.date_range(start="2018-09-09",end="2019-02-02").to_pydatetime().tolist())



def get_24_hour ():

   LIST_hour = []
   
   for x in range (24):
   
      LIST_hour.append(x+1)
            
   return LIST_hour
  
  
#print (get_24_hour ())




def get_dt_every_30m (start_date, end_date):

   LIST_30m_range = ['00', 29, 30, 59] #every 30m

   LIST_date = get_date_range (start_date, end_date)
   LIST_hour = get_24_hour ()
   
   LIST_dt_every_30m = []

   for date in LIST_date: 
   
      for hour in LIST_hour:
            
         dt_name_1 = ('FROM_' + date + '_' + str(hour) + '_' + str(LIST_30m_range[0]) + '_TO_' + str(hour) + '_' + str(LIST_30m_range[1])).replace('-', '_')
         dt_name_2 = ('FROM_' + date + '_' + str(hour) + '_' + str(LIST_30m_range[2]) + '_TO_' + str(hour) + '_' + str(LIST_30m_range[3])).replace('-', '_')
      
         LIST_dt_every_30m.append (dt_name_1 )
         LIST_dt_every_30m.append (dt_name_2 )
         
   return LIST_dt_every_30m
   

'''   
LIST_test = get_dt_every_30m (start_date= date(2024, 1, 1), end_date= date(2024, 12, 31))

for x in LIST_test:

   print (x)
'''


def get_dt_every_60m(start_date, end_date):

   LIST_60m_range = ['00', 59] #every 60m or 1 hour

   LIST_dt_every_60m = []
   
   LIST_date = get_date_range (start_date, end_date)
   LIST_hour = get_24_hour ()
 
   for date in LIST_date: 
   
      for hour in LIST_hour:
            
         dt_name_1 = ('FROM_' + date + '_' + str(hour) + '_' + str(LIST_60m_range[0]) + '_TO_' + str(hour) + '_' + str(LIST_60m_range[1])).replace('-', '_')
      
         LIST_dt_every_60m.append (dt_name_1 )
       
   return LIST_dt_every_60m
   
'''
LIST_test = get_dt_every_60m(start_date=date(2024, 1, 1), end_date= date(2024, 12, 31))
for x in LIST_test:

   print (x)
'''
 
   
def get_dt_every_day(start_date, end_date): 

   LIST_day_1 = []
   LIST_day_2 = []
   
   LIST_date = get_date_range (start_date, end_date)

   for date in LIST_date: 
   
      dt_name_1 = ( 'FROM_TO_' + date ).replace('-', '_')
      
      LIST_day_1.append (date)
      LIST_day_2.append (dt_name_1)
      
       
   return LIST_day_1, LIST_day_2
   
   
'''
LIST_test = get_dt_every_day(start_date=date(2024, 1, 1), end_date= date(2024, 12, 31))[0]
for x in LIST_test:

   print (x)
'''
  
  
  
  
 
   

def add_seconds_to_datetime (add_seconds):

   a= datetime.datetime.now()
   
   b = a + datetime.timedelta(0,add_seconds)
   
   print(a.time())
   
   print(b.time())
   
   return b
   
   
#add_seconds_to_datetime (add_seconds= 300)   




#time spent = date time now - date time started 
#get time spent in seconds, minutes, hours and/or days
def get_time_spent (dt_format, date_time_started, wait_seconds):

   date_time_started 
   
   time.sleep(wait_seconds) #should use 0 in real, non-test cases
   
   # wait a bit 
   date_time_now = datetime.now()

   d = date_time_now - date_time_started # yields a timedelta object

   match dt_format:
   
      case "seconds":
   
         time_spent_in_seconds = d.seconds
   
         print (str(time_spent_in_seconds) + ' seconds')
         return time_spent_in_seconds
         
         
      case "minutes":
      
         time_spent_in_minutes = d.seconds / 60
   
         print (str(time_spent_in_minutes) + ' minutes')
         return time_spent_in_minutes
      
      
      case "hours": 
   
         time_spent_in_hours = d.seconds / 3600
   
         print (str(time_spent_in_hours) + ' hours')
         return time_spent_in_hours
   
   

#get_time_spent ( dt_format = 'hours' , date_time_started=datetime.now(), wait_seconds=5) 



# https://www.tutorialspoint.com/python-program-to-display-date-in-different-country-format
def get_dt_country ():

   pass
   
   
   


#https://www.geeksforgeeks.org/get-current-time-in-different-timezone-using-python/

from datetime import datetime 
import pytz
from pytz import timezone  
  
  
#available time locations 
def get_LIST_all_time_location ():

   LIST_all_time_location = pytz.all_timezones

   print (LIST_all_time_location)   
   return LIST_all_time_location

#get_LIST_all_time_location ()


  
  
'''
# get the standard UTC time  
UTC = pytz.utc 
  
# it will get the time zone  
# of the specified location 
IST = pytz.timezone('Asia/Shanghai') 
  
# print the date and time in 
# standard format 
print("UTC in Default Format : ",  
      datetime.now(UTC)) 
  
print("IST in Default Format : ",  
      datetime.now(IST)) 
  
# print the date and time in  
# specified format 
datetime_utc = datetime.now(UTC) 
print("Date & Time in UTC : ", 
      datetime_utc.strftime('%Y:%m:%d %H:%M:%S %Z %z')) 
  
datetime_ist = datetime.now(IST) 
print("Date & Time in IST : ",  
      datetime_ist.strftime('%Y:%m:%d %H:%M:%S %Z %z')) 

'''


# https://stackoverflow.com/questions/46736529/how-to-compute-the-time-difference-between-two-time-zones-in-python
from datetime import datetime
from pytz import timezone
from dateutil.relativedelta import relativedelta
from datetime import datetime, timedelta

def get_location_time_difference(my_location, for_location):

   utcnow = timezone('utc').localize(datetime.utcnow()) # generic time
   my_loc_dt = utcnow.astimezone(timezone(my_location)).replace(tzinfo=None)
   for_loc_dt   = utcnow.astimezone(timezone(for_location)).replace(tzinfo=None)

   print(my_loc_dt)
   print (for_loc_dt)


   offset = relativedelta(my_loc_dt, for_loc_dt) 
   my_loc_dt_LESS_for_loc_dt = offset.hours

   print (my_loc_dt_LESS_for_loc_dt)
   return my_loc_dt_LESS_for_loc_dt
 
''' 
   #### format my location datetime as string
   my_loc_dt1 = datetime.strptime(str(my_loc_dt), '%Y-%m-%d %H:%M:%S.%f')
   print (my_loc_dt1)
   
   ### use time difference to create new My location datetime (equivalent of the for location datetime)
   time_diff_1 = my_loc_dt1 - timedelta(hours=int(my_loc_dt_LESS_for_loc_dt))
   print (time_diff_1)
 '''
 
#get_location_time_difference(my_location='Australia/Queensland', for_location='America/Toronto') 
 
 
# https://www.geeksforgeeks.org/python-datetime-strptime-function/
# https://stackoverflow.com/questions/67686033/adding-hours-and-days-to-the-python-datetime
# https://www.tutorialspoint.com/how-to-compare-time-in-different-time-zones-in-python   
 
 
# convert time difference into a new My location datetime 
def get_converted_My_location_datetime (my_location, for_loation):

   loc_dt_diff = get_location_time_difference(my_location, for_location)

   utcnow = timezone('utc').localize(datetime.utcnow()) # generic time
   my_loc_dt = utcnow.astimezone(timezone(my_location)).replace(tzinfo=None)
     
   #### format my location datetime as string
   my_loc_dt1 = datetime.strptime(str(my_loc_dt), '%Y-%m-%d %H:%M:%S.%f')
   print (my_loc_dt1)
   
   ### use time difference to create new My location datetime (equivalent of the for location datetime)
   time_diff_1 = my_loc_dt1 - timedelta(hours=int(loc_dt_diff))
   print (time_diff_1)
 
 
 
 
 
''' 
time_diff = get_location_time_difference(my_location='Australia/Queensland', for_location='America/Toronto')

utcnow = timezone('utc').localize(datetime.utcnow()) # generic time
my_loc = utcnow.astimezone(timezone('Australia/Queensland')).replace(tzinfo=None)
my_loc_dt = datetime.strptime(str(my_loc), '%Y-%m-%d %H:%M')
'''

'''
dt1 = '2021-05-06 17:30'
dt = datetime.strptime(dt1, '%Y-%m-%d %H:%M')
time_diff_1 = dt - timedelta(hours=14)

print (time_diff_1)
'''   
   
