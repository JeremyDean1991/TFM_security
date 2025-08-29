


def DICT_date_item (LIST_file_item):

   # enforce data types on the dict values 
   DICT_date_item =  {

            "start_year":                    LIST_date_item[0],   
            "end_year":                      LIST_date_item[1],
            
            "start_date":               LIST_date_item[2], # select files by query or by index 
            "end_date":               LIST_date_item[3],
                             
   }
     
   return DICT_date_item
   # LIST_date_item = [start_year, end_year, start_date, end_date]
   
   
   
   
def DICT_datetime_item (LIST_file_item):

   # enforce data types on the dict values 
   DICT_datetime_item =  {

            "start_year":                    LIST_datetime_item[0],   
            "end_year":                      LIST_datetime_item[1],
            
            "start_date":                    LIST_datetime_item[2],   
            "end_date":                      LIST_datetime_item[3],   

           "start_time":                    LIST_datetime_item[4],   
            "end_time":                      LIST_datetime_item[5],   
                       
            "start_date_time":               LIST_datetime_item[6], # select files by query or by index 
            "end_date_time":                 LIST_datetime_item[7],
                             
   }
     
   return DICT_datetime_item
   # LIST_datetime_item = [start_year, end_year, start_date, end_date, start_time, end_time, start_date_time, end_date_time]   