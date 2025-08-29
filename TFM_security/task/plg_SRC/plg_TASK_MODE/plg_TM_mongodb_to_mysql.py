


import sys
sys.path.append('../a0_plg_CUSTOM/') 
sys.path.append('../plg_TFM/') 
sys.path.append('../plg_DICT/') 

from plg_DICT_database import * 


from a0_items import * 
import pymongo 
from pymongo import MongoClient
from pprint import pprint
import bson
from plg_DB_MongoDB_2 import * 

from concurrent.futures import ThreadPoolExecutor, wait
import concurrent.futures
import time 
import datetime




###############################################################
###### do one DATA ITEM - import do_one_DATA_ITEM function from a dedicated doc 
##############################################################
from a0_TM_task_func import do_one_DATA_ITEM 

# may want to log task item after task completed 

### RAW
def get_LIST_ALL_RAW (LIST_mongodb_item_RAW):

   DICT_m_item_RAW = DICT_mongodb_item (LIST_mongodb_item=LIST_mongodb_item_RAW)
   
   conn_str_RAW = DICT_m_item_RAW ['conn_str']
   db_name_RAW = DICT_m_item_RAW ['db_name']
   coll_name_RAW = DICT_m_item_RAW ['coll_name']

   LIST_ALL_doc_RAW = get_ALL_docs_in_collection (conn_str=conn_str_RAW, db_name=db_name_RAW, coll_name=coll_name_RAW)
   
   return LIST_ALL_doc_RAW 
   

 
def get_LIST_SELECTED_RAW (LIST_mongodb_item_RAW):

   DICT_m_item_RAW = DICT_mongodb_item (LIST_mongodb_item=LIST_mongodb_item_RAW)
   
   start_doc_index_RAW = DICT_m_item_RAW ['start_doc_index']
   end_doc_index_RAW = DICT_m_item_RAW ['end_doc_index']  
   doc_select_mode_COOKED = DICT_m_item_RAW ['doc_select_mode_COOKED']
   LIST_doc_to_select_RAW = DICT_m_item_RAW ['LIST_doc_to_select']
   
   
   LIST_ALL_doc_RAW = get_LIST_ALL_RAW (LIST_mongodb_item_RAW= LIST_mongodb_item_RAW)

   LIST_selected_doc_RAW = []
   
   
   # select doc by list item or by index?
   if doc_select_mode_RAW == 'by_title': # item could be number or string 
      print ('select by list item')

      for doc_1 in LIST_doc_to_select_RAW:
          
         for doc_2 in LIST_ALL_doc_RAW:
         
            doc_str = str(doc_2)
         
            if doc_1 in doc_str:
      
               LIST_selected_doc_RAW.append (doc_1)
               print (str(doc_1) + ' => in doc => ' + str(doc_2), flush=True)
         
            else:
      
               print (str(doc_1) + ' => NOT in doc => ' + str(doc_2), flush=True)
               pass
   
     
   if doc_select_mode_RAW == 'by_index':
      print ('select by list index')
   
      for RAW_doc in LIST_ALL_doc_RAW[start_doc_index_RAW : end_doc_index_RAW ]:
   
         LIST_selected_doc_RAW.append(RAW_doc)
                 
   else:
   
      pass
           
  
   return LIST_selected_doc_RAW



# get lines of ONE of the selected docs
def get_DATA_ITEMS_RAW (LIST_mongodb_item_RAW, doc_index, doc_key_value_option, doc_key_RAW ):

   DICT_m_item_RAW = DICT_mongodb_item (LIST_mongodb_item=LIST_mongodb_item_RAW)
   
   conn_str_RAW = DICT_m_item_RAW ['conn_str']
   db_name_RAW = DICT_m_item_RAW ['db_name']
   coll_name_RAW = DICT_m_item_RAW ['coll_name']   
  

   LIST_selected_doc = get_LIST_SELECTED_RAW (LIST_mongodb_item_RAW=LIST_mongodb_item_RAW)
   
   # get all values of a specific doc 
   LIST_doc_item_RAW_1 = LIST_selected_doc[doc_index].items()
       
   LIST_doc_item_RAW_2 = []
   
   
    # get all keys + values from a doc 
   if doc_key_value_option == 'all':
      print ("get ALL doc keys + values")
   
      for doc_key_value in LIST_doc_item_RAW_1:
      
         LIST_doc_item_RAW_2.append(doc_key_value)
         
         
   # get value of a key from a doc 
   if doc_key_value_option == 'key':
      print ("get ALL doc values by 1 key")
      
      try: 
         # must convert doc into dictionary first      
         Dict_1 = dict(LIST_doc_item_RAW_1)
         
         doc_value = get_DICT_value_by_key (my_DICT=Dict_1, my_KEY=doc_key_RAW)
         print (doc_value)
      
         #print (item, flush=True)
         LIST_doc_item_RAW_2.append (doc_value)
                 
      except:
      
         #print ("An error has occured")
         pass 
            
   else:
   
      pass   
            
         
   return LIST_doc_item_RAW_2 



  
### COOKED  - all tables of a database
def get_LIST_cooked_ALL (LIST_mysql_item_COOKED):

   DICT_mysql_item_RAW = DICT_mysql_item (LIST_mysql_item=LIST_mongodb_item_COOKED)
   
   host_COOKED = DICT_m_item_RAW ['host']
   username_COOKED = DICT_m_item_RAW ['username']
   password_COOKED = DICT_m_item_RAW ['password']
   db_name_COOKED = DICT_m_item_RAW ['db_name']


   LIST_cooked_ALL = Mysql_get_ALL_tables (My_host=host_COOKED, My_user=username_COOKED, My_pass=password_COOKED, My_db_name=db_name_COOKED)
   
   return LIST_cooked_ALL 
   
 
#get_LIST_raw_ALL (raw_My_host, raw_My_user, raw_My_pass)
   
   

def get_LIST_cooked_SELECTED ( LIST_mysql_item_COOKED):


   DICT_mysql_item_COOKED = DICT_mysql_item (LIST_mysql_item=LIST_mysql_item_COOKED)
   
   start_table_index_COOKED = DICT_m_item_COOKED ['start_table_index']
   end_table_index_COOKED = DICT_m_item_COOKED ['end_table_index']  
   table_select_mode_COOKED = DICT_m_item_COOKED ['table_select_mode']
   LIST_table_to_select_COOKED = DICT_m_item_COOKED ['LIST_table_to_select']


   LIST_cooked_ALL = get_LIST_cooked_ALL (LIST_mysql_item_COOKED)

   LIST_cooked_selected = []
   
   # select table by list item or by index?
   if table_select_mode_RAW == 'by_title': # item could be number or string 
      print ('select by list item')

      for table_1 in LIST_table_to_select_RAW:
          
         for table_2 in LIST_ALL_table_RAW:
         
            table_str = str(table_2)
         
            if table_1 in table_str:
      
               LIST_selected_table_RAW.append (table_1)
               print (str(table_1) + ' => in table => ' + str(table_2), flush=True)
         
            else:
      
               print (str(table_1) + ' => NOT in table => ' + str(table_2), flush=True)
               pass
   
     
   if table_select_mode_RAW == 'by_index':
      print ('select by list index')
   
      for RAW_table in LIST_ALL_table_RAW[start_table_index_RAW : end_table_index_RAW ]:
   
         LIST_selected_table_RAW.append(RAW_table)
                 
   else:
   
      pass
           
  
   return LIST_selected_table_RAW



  
def get_data_item_COOKED (LIST_mysql_item):

   DICT_mysql_item_COOKED = DICT_mysql_item (LIST_mysql_item=LIST_mysql_item_COOKED)
   
   host_COOKED = DICT_m_item_RAW ['host']
   username_COOKED = DICT_m_item_RAW ['username']
   password_COOKED = DICT_m_item_RAW ['password']
   db_name_COOKED = DICT_m_item_RAW ['db_name']   
   table_name_COOKED = DICT_m_item_RAW ['table_name']   
    
   table_column_COOKED = DICT_m_item_COOKED ['table_column']
   table_col_value_option_COOKED = DICT_m_item_COOKED ['table_column_value_option']
   

   LIST_table_item_COOKED_2 = []
   
   LOLISTS_table_items = []


   for table in LIST_table_SELECTED:
   
      LIST_table_item_COOKED_1 =  Mysql_select_ALL_tb_data (My_host=host_COOKED, My_user=username_COOKED, My_pass=password_COOKED , My_db_name=db_name_COOKED, My_table_name=table_name_COOKED)
      
      # get all keys + values from a doc 
      if table_col_value_option_COOKED == 'all':
         print ("get ALL table columns + values")
   
         for table_col_value in LIST_table_item_COOKED_1:
      
            LIST_table_item_COOKED_2.append(table_col_value) 
            
            LIST_table_item_COOKED_2.insert(0, table)   
         
         LOLISTS_table_items.append (LIST_table_item_COOKED_2)
            
         
      # get value of a key from a doc 
      if table_col_value_option_COOKED == 'col':
         print ("get ALL values by 1 column")
                
         col_value = all values of 1 column only
         print (col_value)
      
         #print (item, flush=True)
         LIST_table_item_COOKED_2.append (table_col_value)           
         
         LIST_table_item_COOKED_2.insert(0, table)
            
      LOLISTS_table_items.append (LIST_table_item_COOKED_2)
                 
           
      
   return LOLISTS_table_items   




def get_TO_BE_DATA_ITEMS (LIST_mysql_item_COOKED):

   LIST_data_item_RAW = get_data_items_RAW (LIST_mongodb_RAW)
   LIST_data_item_COOKED = get_cooked_DATA_ITEMS (LIST_mysql_COOKED)
   
   LIST_to_be_table = []
   
   #need to match raw & cooked tables by using table key = table title 
        
   for raw_table in LIST_raw_table:
    
      for cooked_data_item in LIST_cooked_data_item:
      
         raw_table=raw_table[raw_table_key=raw_table_key]
            
         if raw_table in cooked_data_item:
          
            print (raw_table + ' in ' + cooked_data_item)
            
         else:
         
            print (raw_table + ' NOT in ' + cooked_data_item)
            LIST_to_be_table.append(raw_table)
   
   #print ('LIST to be tableuments => ' + str(LIST_test_to_be_table))   
   return LIST_to_be_table 
   
   
   
   
###############################################################
###### Process data items by loop (LP)
##############################################################
  
# Process data item by loop
def LP_all_data_items (LIST_mongodb_item_RAW, LIST_mysql_item_COOKED):


   DICT_m_item_RAW   = DICT_mongodb_item (LIST_mongodb_item=LIST_file_item_RAW)
   
   start_data_list_index_RAW                       = DICT_f_item_RAW['start_data_list_index'] 
   end_data_list_index_RAW                         = DICT_f_item_RAW['end_data_list_index']
  
  
   LIST_data_item_TO_BE =  get_data_items_TO_BE (LIST_mongodb_item_RAW, LIST_mysql_item_COOKED)
   data_file_only = LIST_data_item_TO_BE[0]
   print ('data file only => ' + str(data_file_only))
   
   
   # Loop through EACH selected to_be data file 
   for data_item in LIST_data_item_TO_BE[start_data_list_index_RAW:end_data_list_index_RAW] :
          
      # do data item here 
      do_one_DATA_ITEM (data_item) 



#################################################################
###### Process data items by concurrency futures (CF)
###################################################################
      

# Concurrent using list of 
def CF_all_data_chunk (LIST_mongodb_item_RAW, LIST_mysql_item_COOKED):
  
   DICT_f_item_RAW   = DICT_file_item (LIST_file_item=LIST_file_item_RAW)   
   start_data_list_index_RAW                       = DICT_f_item_RAW['start_data_list_index'] 
   end_data_list_index_RAW                         = DICT_f_item_RAW['end_data_list_index']
   
   
   DICT_c_item_RAW   = DICT_concurrency_item (LIST_concurrency_item = LIST_concurrency_item_RAW)   
   LIST_data_item_split = DICT_c_item_RAW['LIST_data_item_split'] 
   start_index = DICT_c_item_RAW['start_index'] 
   items_per_list = DICT_c_item_RAW['items_per_list'] 
   pause_secs = DICT_c_item_RAW['pause_secs'] 
   
     
   LIST_data_item_TO_BE =  get_data_items_TO_BE (LIST_mongodb_item_item_RAW, LIST_mysql_item_COOKED) 
   data_file_only = LIST_data_item_TO_BE[0]
   print ('data file only => ' + str(data_file_only))


   CF_all_data_chunks (LIST_data_item_split=LIST_data_item_split, start_index=start_index, items_per_list=items_per_list, do_one_DATA_ITEM=do_one_DATA_ITEM, pause_secs=pause_secs )




def TM_mongodb_to_mysql(LIST_mongodb_item_RAW, LIST_mysql_item_COOKED, LIST_concurrency_item_RAW, output_option):

   match output_option:

      case 'RAW_1':
         RAW_1 = get_LIST_ALL_RAW (LIST_mongodb_item_RAW=LIST_mongodb_item_RAW)
         print ('RAW_1 => ' + str(RAW_1))
         
      case 'RAW_2':       
         RAW_2 = get_LIST_SELECTED_RAW (LIST_mongodb_item_RAW=LIST_mongodb_item_RAW)
         print ('RAW_2 => ' + str(RAW_2))
         
      case 'RAW_3':
         RAW_3 = get_data_items_RAW (LIST_mongodb_item_RAW)
         print ('RAW_3 => ' + str(RAW_3))

      case 'COOKED_1':
         COOKED_1 = get_LIST_ALL_COOKED (LIST_mysql_item_COOKED)
         print ('COOKED_1 => ' + str(COOKED_1))
         
      case 'COOKED_2':
         COOKED_2 = get_LIST_SELECTED_COOKED (LIST_mysql_item_COOKED)
         print (' COOKED_2 => ' + str(COOKED_2))
         
      case 'COOKED_3':      
         COOKED_3 = get_data_items_COOKED (LIST_mysql_item_COOKED)
         print ('COOKED_3 => ' + str(COOKED_3))

      case 'TO_BE_1':
         TO_BE_1 = get_data_items_TO_BE (LIST_mongodb_item_RAW, LIST_mysql_item_COOKED )
         print (' TO_BE_1 => ' + str(TO_BE_1))
       
   
      case 'LP':
         LP =  LP_data_item_ALL (LIST_mongodb_item_RAW, LIST_mysql_item_COOKED)
         print (' LP => ' + str(LP))
      
      case 'CF':
         CF = CF_data_chunk_ALL (LIST_mongodb_item_RAW, LIST_mysql_item_COOKED, LIST_concurrency_item_RAW)
         print (' CF => ' + str(CF))


#################################################################
###### TEST OUTPUT 
#################################################################

 ### 1 raw vs 1 cooked table OR 1 raw vs many cooked tables??


def TEST_OUTPUT (output_option):
   
   # RAW data 
   conn_str_R ="mongodb://localhost:27017/"
   db_name_R = "mydatabase"
   coll_select_mode_R = ''
   coll_name_R = "people"

   start_coll_index_R = 0
   end_coll_index_R = 0
   LIST_coll_to_select_R = [] # list of coll titles to select

   table_select_mode_R = 'by_index'
   table_key_R = 'table_title'
   table_id_R = ''
   table_title_R = ''
   
   table_index_R =0
   start_table_index_R = 0
   end_table_index_R = 1
   LIST_table_to_select_R = ['shane'] # list of table titles to select
   
   table_key_value_option_R = 'key'
   start_data_list_index_R = ''
   end_data_list_index_R = ''

   LIST_mongodb_item_RAW = [conn_str_R, db_name_R, coll_select_mode_R, coll_name_R, start_coll_index_R, end_coll_index_R, LIST_coll_to_select_R, table_select_mode_R, table_key_R, table_id_R, table_title_R, table_index_R, start_table_index_R, end_table_index_R, LIST_table_to_select_R, table_key_value_option_R, start_data_list_index_R, end_data_list_index_R]
      
   

   # COOKED data
   host = ''
   username = ''
   password = ''
   db_name = ''
   
   table_select_mode= ''
   table_name = ''
   start_table_index = ''
   end_table_index = ''
   
   LIST_table_to_select = []
   
   mysql_query = ''
   
   table_col_value_option = ''
   column_name = ''
   start_data_list_index = ''
   end_data_list_index = ''

   LIST_mysql_item_COOKED = [conn_str_C, db_name_C, coll_select_mode_C, coll_name_C, start_coll_index_C, end_coll_index_C, LIST_coll_to_select_C, table_select_mode_C, table_key_C, table_id_C, table_title_C, table_index_C, start_table_index_C, end_table_index_C, LIST_table_to_select_C, table_key_value_option_C, start_data_list_index_C, end_data_list_index_C]
   
   
   # Concurrency futures  
   LIST_data_item_split = get_data_items_TO_BE (LIST_mongodb_item_RAW, LIST_mongodb_item_COOKED)
   start_index = 0
   items_per_list =2 
   do_one_DATA_ITEM = ''
   pause_secs = 2
    
   LIST_concurrency_item_RAW = [LIST_data_item_split, start_index, items_per_list, do_one_DATA_ITEM, pause_secs]
   
   # TASK MODE txt to mongodb
   TM_mongodb_to_mysql (LIST_mongodb_item_RAW, LIST_mysql_item_COOKED, LIST_concurrency_item_RAW, output_option)
         
   
   
#must run concurrency using if __name__ == '__main__'
if __name__ == '__main__':
   
   #TEST_OUTPUT (output_option='RAW_1')
   #TEST_OUTPUT (output_option='RAW_2')
   #TEST_OUTPUT (output_option='RAW_3')
   
   #TEST_OUTPUT (output_option='COOKED_1')
   #TEST_OUTPUT (output_option='COOKED_2')
   #TEST_OUTPUT (output_option='COOKED_3')
   
   #TEST_OUTPUT (output_option='TO_BE_1')
  
   #TEST_OUTPUT (output_option='LP')
   #TEST_OUTPUT (output_option='CF')


