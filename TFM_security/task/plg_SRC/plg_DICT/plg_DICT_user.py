


def DICT_user_item (LIST_user_item):

   # enforce data types on the dict values 
   DICT_user_item =  {

            "first_name":                    LIST_user_item[0],   
            "middle_name":                      LIST_user_item[1],
            "last_name":                      LIST_user_item[2],
            
            "date_of_birth":               LIST_user_item[3], # select files by query or by index 
            "birth_year":               LIST_user_item[4],
            "birth_month":                 LIST_user_item[5],
             "birth_day":                 LIST_user_item[6],
             "birth_time":                 LIST_user_item[7],
             
             "ip_address"               LIST_user_item[8],
             "username":                LIST_user_item[9],
             "password":                   LIST_user_item[10],
             
             "gender":                       LIST_user_item[11],
             "marital_status":                LIST_user_item[12],
                        
            "LIST_phone_landline":       list(LIST_user_item[13]), # file item could be a file number or string
            "LIST_phone_mobile":           list (LIST_user_item[14]),

            "LIST_address":                 list(LIST_user_item[15]), 
            "LIST_country":                   list(LIST_user_item[16], 
            "LIST_language":                  list(LIST_user_item[17], 
   }
     
   return DICT_user_item
   # LIST_user_item = [folder_path, file_path, file_select_mode, start_file_index, end_file_index, LIST_user_item_to_select, file_prefix, file_extension]

