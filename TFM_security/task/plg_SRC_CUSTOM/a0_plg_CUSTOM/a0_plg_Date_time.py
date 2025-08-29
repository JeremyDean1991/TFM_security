

import sys
sys.path.append('../plg_CUSTOM/') 
sys.path.append('../../plg_SRC/a0_plg_TFM/') 
sys.path.append('../../plg_SRC/plg_DICT/')
sys.path.append('../../plg_SRC/plg_Date_time/') 

from plg_Date_time import * 


def get_LIST_date_for_LOG (start_date, end_date):

   LIST_date = get_date_range(start_date, end_date)

   return LIST_date


'''
LIST_date = get_LIST_date_for_LOG(start_date= date(2024, 1, 1), end_date= date(2024, 12, 31) )

for date in LIST_date:

   print (date)
 ''' 