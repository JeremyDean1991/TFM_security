



def DICT_concurrency_item (LIST_concurrency_item):

   # enforce data types on the dict values 
   DICT_concurrency_item =  {

            "LIST_data_item_split":                      list(LIST_concurrency_item[0]),   
            
            "start_index":               LIST_concurrency_item[1], # select item by query or by index 
            "items_per_list":               int(LIST_concurrency_item[2]),
            "do_one_DATA_ITEM":                 LIST_concurrency_item[3],
            
            "pause_secs":        LIST_concurrency_item[4]
            
                              
   }
     
   return DICT_concurrency_item
   # LIST_concurrency_item = [LIST_data_item_split, start_index, items_per_list, do_one_DATA_ITEM, puase_secs]





def DICT_list_item (LIST_list_item):

   # enforce data types on the dict values 
   DICT_list_item =  {

            "list_body":                      list(LIST_list_item[0]),   
            
            "list_select_mode":               LIST_list_item[1], # select item by query or by index 
            "start_list_index":               int(LIST_list_item[2]),
            "end_list_index":                 int(LIST_list_item[3]),
            
            "LIST_list_to_select":        list(LIST_list_item[4]), # list item could be a item number or string
            
            "start_data_list_index" :          LIST_list_item[5],
            "end_data_list_index"  :           LIST_list_item[6], 
                              
   }
     
   return DICT_list_item
   # LIST_list_item = [list_body, list_select_mode, start_list_index, end_list_index, LIST_item_to_select, start_data_list_index, end_data_list_index]




# text file database
def DICT_file_item (LIST_file_item):

   # enforce data types on the dict values 
   DICT_file_item =  {

            "folder_path":                    LIST_file_item[0],   
            "file_path":                      LIST_file_item[1],
            
            "file_select_mode":               LIST_file_item[2], # select files by title or by index 
            "start_file_index":               LIST_file_item[3],
            "end_file_index":                 LIST_file_item[4],
            
            "LIST_file_to_select":       list(LIST_file_item[5]), # file titles to select
            "file_prefix":                    LIST_file_item[6],
            "file_extension":                 LIST_file_item[7], 

            "line_start_num":                 LIST_file_item[8], 
            "line_end_num":                   LIST_file_item[9], 
            
            "start_data_list_index" :          LIST_file_item[10],
            "end_data_list_index"  :           LIST_file_item[11],
            
   }
     
   return DICT_file_item
   # LIST_file_item = [folder_path, file_path, file_select_mode, start_file_index, end_file_index, LIST_file_item_to_select, file_prefix, file_extension, line_start_num, line_end_num, start_data_list_index, end_data_list_index]




# csv database
def DICT_csv_item (LIST_csv_item):

   DICT_csv_item =  {

            "folder_path":                   LIST_csv_item[0],   
            "csv_path":                      LIST_csv_item[1],
            
            "csv_select_mode":              LIST_csv_item[2], # select csv by title or by index 
            "start_csv_index":               int(LIST_csv_item[3]), # start csv file index
            "end_csv_index":                 int(LIST_csv_item[4]), # end csv file index
            
            "LIST_csv_to_select":        list(LIST_csv_item[5]), # csv could be a file number or string
            "csv_prefix":                    LIST_csv_item[6],
            "csv_extension":                 LIST_csv_item[7],      
            
            "LIST_csv_column":               list(LIST_csv_item[8]), # a list of csv column names  
            
            "start_data_list_index" :          LIST_csv_item[9],
            "end_data_list_index"  :           LIST_csv_item[10],
   }
     
   return DICT_csv_item
   # LIST_csv_item = [folder_path, csv_path, csv_select_mode, start_csv_index, end_csv_index, LIST_csv_to_select, csv_prefix, csv_extension, LIST_csv_column]



def DICT_mongodb_item (LIST_mongodb_item):

   # enforce data types on the dict values 
   DICT_mongodb_item =  {

           "conn_str":                  str(LIST_mongodb_item[0]),   
           "db_name":                   LIST_mongodb_item[1],
            
           "coll_select_mode":          LIST_mongodb_item[2], # by index or by title
           "coll_name":                 LIST_mongodb_item[3],
           "start_coll_index":          int(LIST_mongodb_item[4]),
           "end_coll_index":            int(LIST_mongodb_item[5]),
           "LIST_coll_to_select":   list(LIST_mongodb_item[6]),
            
            
           "doc_select_mode":           LIST_mongodb_item[7],  # by index or by title
           "doc_key":                   LIST_mongodb_item[8], 
           "doc_id":                    LIST_mongodb_item[9], # can use doc_id or doc_title to find unique doc values 
           "doc_title":                 LIST_mongodb_item[10], 
                      
           'doc_index':                  int(LIST_mongodb_item[11]), 
           'start_doc_index':           int(LIST_mongodb_item[12]),
           'end_doc_index':             int(LIST_mongodb_item[13]),
           'LIST_doc_to_select':    list(LIST_mongodb_item[14]), # list of doc titles to select
           
           'doc_key_value_option':   LIST_mongodb_item[15], # get ALL doc key & values, or get ALL docs values by 1 key 
           
           "start_data_list_index" :          LIST_mongodb_item[16],
            "end_data_list_index"  :           LIST_mongodb_item[17],
                     
                       
   }
     
   return DICT_mongodb_item
   # LIST_mongodb_item = [conn_str, db_name, coll_select_mode, coll_name, start_coll_index, end_coll_index, LIST_coll_to_select, doc_select_mode, doc_key, doc_id, doc_title, doc_index, start_doc_index, end_doc_index, LIST_doc_to_select, doc_key_value_option, start_data_list_index, end_data_list_index]



# mysql database
def DICT_mysql_item (LIST_mysql_item):

   # enforce data types on the dict values 
   DICT_mysql_item =  {

           "host":                       str(LIST_mysql_item[0]),   
           "username":                   LIST_mysql_item[1],
           "password":                   LIST_mysql_item[2],
           "db_name":                    LIST_mysql_item[3],
           
           "table_select_mode":           LIST_mysql_item[4], # select by title or by index 
           "table_name":                  LIST_mysql_item[5],
           'start_table_index':           int(LIST_mysql_item[6]),
           'end_table_index':             int(LIST_mysql_item[7]),
           
           'LIST_table_to_select':        list(LIST_mysql_item[8]), # table name or titles to select 
           'mysql_query':                 LIST_mysql_item[9], 
           
          
           'table_col_value_option':           LIST_mysql_item[10],
           'column_name':                       LIST_mysql_item[11],
           
            "start_data_list_index" :          LIST_mysql_item[12],
            "end_data_list_index"  :           LIST_mysql_item[13],          
                                                    
   }
     
   return DICT_mysql_item
   # LIST_mysql_item = [host, username, password, db_name, table_select_mode, table_name, start_table_index, end_table_index, LIST_table_to_select, mysql_query, table_col_value_option, column_name, start_data_list_index, end_data_list_index]



# sqlite database
def DICT_sqlite_item (LIST_sqlite_item):

   # enforce data types on the dict values 
   DICT_sqlite_item =  {

           "db_file_path":                 str(LIST_sqlite_item[0]),
           "table_name":                   LIST_sqlite_item[1],
           
           "table_select_mode":             LIST_sqlite_item[4], # select by title or by index 
           "table_name":                  LIST_sqlite_item[5],
           'start_table_index':           int(LIST_sqlite_item[6]),
           'end_table_index':             int(LIST_sqlite_item[7]),
           
           'LIST_table_to_select':        list(LIST_sqlite_item[8]), # list of table titles or names to select
           'sqlite_query':                 LIST_sqlite_item[9], 
           
            "start_data_list_index" :          LIST_sqlite_item[10],
            "end_data_list_index"  :           LIST_sqlite_item[11],           
           
           
   }
     
   return DICT_sqlite_item



