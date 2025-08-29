


   
def DICT_email_account_item (LIST_email_account_item):

   # enforce data types on the dict values 
   DICT_email_account_item =  {

            "host":                  LIST_email_account_item[0], 
            "username":              LIST_email_account_item[1],
            "password":              LIST_email_account_item[2], 
            "port"                   LIST_email_account_item[3], 

            "name":                 LIST_email_account_item[4],   
            "dob":              LIST_email_account_item[5],
            "gender"                    LIST_email_account_item[6],
            
            "phone":                LIST_email_account_item[7],   
            "email":                   LIST_email_account_item[8],             
            "country":            LIST_email_account_item[9],                                       
            "address":                  LIST_email_account_item[10], 

            "error_msg":             LIST_email_account_item[11], 
            "sent_failed":                LIST_email_account_item[12],   
            "sent_failed_date":           LIST_email_account_item[13],   
                          
   }
     
   return DICT_email_account_item
   # LIST_email_account_item = []   




