


   
def DICT_smtp_item (LIST_smtp_item):

   # enforce data types on the dict values 
   DICT_smtp_item =  {

            "smtp_host":                  LIST_smtp_item[0], 
            "smtp_username":              LIST_smtp_item[1],
            "smtp_password":              LIST_smtp_item[2], 
            "smtp_port"                   LIST_smtp_item[3], 

            "from_email":                 LIST_smtp_item[4],   
            "LIST_to_email":              LIST_smtp_item[5],
            "LIST_bcc"                    LIST_smtp_item[6],
            
            "msg_subject":                LIST_smtp_item[7],   
            "msg_body":                   LIST_smtp_item[8],             
            "LIST_attachment":            LIST_smtp_item[9],                
                       
            "sent_date":                  LIST_smtp_item[10], 

            "error_msg":             LIST_smtp_item[11], 
            "sent_failed":                LIST_smtp_item[12],   
            "sent_failed_date":           LIST_smtp_item[13],   
                          
   }
     
   return DICT_smtp_item
   # LIST_smtp_item = []   




def DICT_imap_item (LIST_imap_item):

   # enforce data types on the dict values 
   DICT_imap_item =  {

            "imap_host":                  LIST_imap_item[0], 
            "imap_username":              LIST_imap_item[1],
            "imap_password":              LIST_imap_item[2], 
            "imap_port"                   LIST_imap_item[3], 

            "from_email":                 LIST_imap_item[4],   
            "LIST_to_email":              LIST_imap_item[5],
            "LIST_bcc"                    LIST_imap_item[6],
            
            "msg_subject":                LIST_imap_item[7],   
            "msg_body":                   LIST_imap_item[8],             
            "LIST_attachment":            LIST_imap_item[9],  

            "error_msg":             LIST_smtp_item[10], 
                                                
   }
     
   return DICT_imap_item
   # LIST_imap_item = []   