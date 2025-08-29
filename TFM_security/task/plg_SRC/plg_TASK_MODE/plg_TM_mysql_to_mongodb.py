

import sys
sys.path.append('../a0_plg_CUSTOM/') 
sys.path.append('../plg_TFM/') 
sys.path.append('../plg_DICT/') 

from plg_DICT_database import * 

import pymongo 
from pymongo import MongoClient
from pprint import pprint
import bson
from plg_DB_MongoDB_2 import * 


from concurrent.futures import ThreadPoolExecutor, wait
import concurrent.futures
import time 
import datetime


##### Must download & install MongoDB software from --> https://www.mongodb.com/try/download/community #######
# https://www.w3schools.com/python/python_mongodb_getstarted.asp


### RAW - get ALL tables of a database (NOT get all database)
def get_LIST_raw_ALL (LIST_mysql_item_RAW):

   DICT_mysql_item_RAW = DICT_mysql_item (LIST_mysql_item=LIST_mysql_item_RAW)
   
   mysql_host_RAW = DICT_mysql_item_RAW ['host']  
   mysql_username_RAW = DICT_csv_item_RAW['username']
   mysql_password_RAW= DICT_csv_item_RAW['password']  

   mysql_db_name_RAW= DICT_csv_item_RAW['db_name']  
   
   LIST_raw_ALL = Mysql_get_ALL_tables (My_host=mysql_host_RAW, My_user=mysql_username_RAW, My_pass=mysql_password_RAW, My_db_name=mysql_db_name_RAW)
   
   return LIST_raw_ALL 
   
 
#get_LIST_raw_ALL (raw_My_host, raw_My_user, raw_My_pass)
 
  
  
def get_LIST_raw_SELECTED ( LIST_mysql_item_RAW):

   # get values from plg_Dict.py
   DICT_mysql_item_RAW = DICT_mysql_item (LIST_mysql_item=LIST_mysql_item_RAW)
   
   mysql_host_RAW = DICT_mysql_item_RAW ['host']  
   mysql_username_RAW = DICT_csv_item_RAW['username']
   mysql_password_RAW= DICT_csv_item_RAW['password']  

   mysql_db_name_RAW= DICT_csv_item_RAW['db_name']  
   
   table_select_mode_RAW= DICT_csv_item_RAW['table_select_mode'] 
   LIST_table_to_select_RAW = DICT_csv_item_RAW['LIST_table_to_select'] 
   
  
   LIST_table_all_RAW = get_LIST_raw_ALL (LIST_mysql_item_RAW=LIST_mysql_item_RAW)

   LIST_selected_RAW = []
   
   
   # select table by name or by index?
   if table_select_mode_RAW == 'by_query': # item could be number or string   
      print ('select by list name')

      for table in LIST_table_to_select_RAW:
             
         if table in LIST_table_ALL_RAW:
      
            LIST_selected_RAW.append (table)
            #print ('raw file selected => ' + str(item), flush=True)
            
         
         else:
      
            #print ('raw file NOT selected => ' + str(item), flush=True)
            pass
            
   if table_select_mode_RAW == 'by_index':  
      print ('select by list index')
    
      for table in LIST_table_ALL_RAW [start_table_index_RAW:end_table_index_RAW]:
       
         LIST_selected_RAW.append (table)
           
   else:
     
     pass
      
          
   return LIST_selected_RAW 
   
   

# select data from a particular table 
def get_raw_DATA_ITEMS (LIST_mysql_item_RAW):

   # get values from plg_Dict.py
   DICT_mysql_item_RAW = DICT_mysql_item (LIST_mysql_item=LIST_mysql_item_RAW)
   
   mysql_host_RAW = DICT_mysql_item_RAW ['host']  
   mysql_username_RAW = DICT_csv_item_RAW['username']
   mysql_password_RAW= DICT_csv_item_RAW['password']  

   mysql_db_name_RAW= DICT_csv_item_RAW['db_name'] 
   mysql_querye_RAW= DICT_csv_item_RAW['mysql_query']
   
  
   LIST_raw_data_item = Mysql_select_tb_data (My_host=mysql_host_RAW, My_user=mysql_host_RAW, My_pass=mysql_password_RAW , My_db_name=mysql_db_name_RAW, My_select_query=mysql_query_RAW)
   
   return LIST_raw_data_item  
  
  
  

### COOKED   
def get_LIST_ALL_COOKED (LIST_mongodb_item_COOKED):

   DICT_m_item_COOKED = DICT_mongodb_item (LIST_mongodb_item=LIST_mongodb_item_COOKED)
   
   conn_str_COOKED = DICT_m_item_COOKED ['conn_str']
   db_name_COOKED = DICT_m_item_COOKED ['db_name']
   coll_name_COOKED = DICT_m_item_COOKED ['coll_name']

   LIST_ALL_doc_COOKED = get_ALL_docs_in_collection (conn_str=conn_str_COOKED, db_name=db_name_COOKED, coll_name=coll_name_COOKED)
   
   return LIST_ALL_doc_COOKED 
   

 
def get_LIST_SELECTED_COOKED (LIST_mongodb_item_COOKED):

   DICT_m_item_COOKED = DICT_mongodb_item (LIST_mongodb_item=LIST_mongodb_item_COOKED)
   
   start_doc_index_COOKED = DICT_m_item_COOKED ['start_doc_index']
   end_doc_index_COOKED = DICT_m_item_COOKED ['end_doc_index']  
   doc_select_mode = DICT_m_item_COOKED ['doc_select_mode']
   LIST_doc_item_to_select_COOKED = DICT_m_item_COOKED ['LIST_doc_item_to_select']
   
   
   LIST_ALL_doc_COOKED = get_LIST_ALL_COOKED (LIST_mongodb_item_COOKED= LIST_mongodb_item_COOKED)

   LIST_selected_DOC_COOKED = []
   
   
   # select file by list item or by index?
   if doc_select_mode == 'by_query': # item could be number or string 
      print ('select by list item')

      for item in LIST_doc_item_to_select_COOKED:
          
         for doc in LIST_ALL_doc_COOKED:
         
            doc_str = str(doc)
         
            if item in doc_str:
      
               LIST_selected_DOC_COOKED.append (doc)
               print (str(item) + ' => in doc => ' + str(doc), flush=True)
         
            else:
      
               print (str(item) + ' => NOT in doc => ' + str(doc), flush=True)
               pass
   
     
   if doc_select_mode == 'by_index':
      print ('select by list index')
   
      for cooked_doc in LIST_ALL_doc_COOKED[start_doc_index_COOKED : end_doc_index_COOKED ]:
   
         LIST_selected_DOC_COOKED.append(cooked_doc)
                 
   else:
   
      pass
           
  
   return LIST_selected_DOC_COOKED



# get lines of ONE of the selected docs
def get_DATA_ITEMS_COOKED (LIST_mongodb_item_COOKED, doc_index, dict_option ):

   DICT_m_item_COOKED = DICT_mongodb_item (LIST_mongodb_item=LIST_mongodb_item_COOKED)
   
   conn_str_COOKED = DICT_m_item_COOKED ['conn_str']
   db_name_COOKED = DICT_m_item_COOKED ['db_name']
   coll_name_COOKED = DICT_m_item_COOKED ['coll_name']   
  
   # get value of a key from a doc 
   doc_key_COOKED =  DICT_m_item_COOKED ['doc_key'] 

   LIST_selected_doc = get_LIST_SELECTED_COOKED (LIST_mongodb_item_COOKED=LIST_mongodb_item_COOKED)
   
   # get all values of a specific doc 
   LIST_doc_item_COOKED_1 = LIST_selected_doc[doc_index].items()
       
   LIST_doc_item_COOKED_2 = []
   
   
    # get all keys + values from a doc 
   if dict_option == 'all':
      print ("get ALL doc keys + values")
   
      for doc_key_value in LIST_doc_item_COOKED_1:
      
         LIST_doc_item_COOKED_2.append(doc_key_value)
         
         
   # get value of a key from a doc 
   if dict_option == 'key':
      print ("get ALL doc values by 1 key")
      
      try: 
         # must convert doc into dictionary first      
         Dict_1 = dict(LIST_doc_item_COOKED_1)
         
         doc_value = get_DICT_value_by_key (my_DICT=Dict_1, my_KEY=doc_key_COOKED)
         print (doc_value)
      
         #print (item, flush=True)
         LIST_doc_item_COOKED_2.append (doc_value)
                 
      except:
      
         #print ("An error has occured")
         pass 
            
   else:
   
      pass   
            
         
   return LIST_doc_item_COOKED_2 



### TO_BE data items
def get_TO_BE_DATA_ITEMS (LIST_mysql_item_RAW, LIST_mongodb_item_COOKED, doc_index, dict_option):
  
   LIST_raw = get_raw_DATA_ITEMS (LIST_mysql_item_RAW = LIST_mysql_item_RAW)
   LIST_cooked = get_DATA_ITEMS_COOKED (LIST_mongodb_item_COOKED=LIST_mongodb_item_COOKED, doc_index=doc_index, dict_option=dict_option )
   
   #print (LIST_raw)
   #print (LIST_cooked)
  
   LIST_to_be = []
       
   for raw in LIST_raw:
    
      if raw in LIST_cooked:
       
         #print (raw + ' in cooked')
         pass
          
      else:
          
         #print (raw + ' NOT in cooked')
         LIST_to_be.append(raw)
   
   #print ('LIST to be => ' + str(LIST_test_to_be))   
   return LIST_to_be 
  
   
  
'''
# do the task on 1 data item, eg send email, post comment   
## this method needs to be created from scratch to be used by CF_data_chunk (LIST_item)
def do_one_DATA_ITEM (doc):

   #To insert or update docs here
   print (doc)   
'''   
   

#####################################################################
##### Selected TO_BE collections with TO_BE documents
#####################################################################
##### Selected TO_BE data files with TO_BE data items 

def get_LIST_to_be_SELECTED_with_data_items (LIST_mysql_item_RAW, LIST_mongodb_item_COOKED, doc_index, dict_option ):

   # get values from plg_Dict.py
   DICT_mysql_item_RAW = DICT_mysql_item (LIST_mysql_item=LIST_mysql_item_RAW)


   LIST_table_SELECTED_RAW =  get_LIST_raw_SELECTED ( LIT_mysql_item_RAW)
   LIST_doc_SELECTED_COOKED = get_LIST_SELECTED_COOKED (LIST_mongodb_item_COOKED=LIST_mongodb_item_COOKED)
   
   #TO_BE lists & data 
   LOLISTS_to_be_data_SELECTED = []
   
   # get_TO_BE_DATA_ITEMS returns LOLISTS_to_be_data_SELECTED
   for raw_table, cooked_doc in zip(LIST_mysql_SELECTED_RAW, LIST_doc_SELECTED_COOKED):

      LIST_TO_BE_item = get_TO_BE_DATA_ITEMS (LIST_mysql_item_RAW = raw_table, LIST_mongodb_item_COOKED=LIST_mongodb_item_COOKED, doc_index=doc_index, dict_option=dict_option)    
      LIST_TO_BE_item.insert(0, raw_file)
      
      LOLISTS_to_be_data_SELECTED.append(LIST_TO_BE_item)



###############################################################
###### Process data items by loop (LP)
##############################################################
  
# Process data item by loop
def LP_all_data_items (LIST_mysql_item_RAW, LIST_mongodb_item_COOKED, do_one_DATA_ITEM):

   DICT_mysql_item_RAW = DICT_mysql_item (LIST_mysql_item=LIST_mysql_item_RAW)
   DICT_mongodb_item_COOKED = DICT_mongodb_item (LIST_mongodb_item=LIST_mongodb_item)
     
   # Func arg values from Dict values
   mysql_host_RAW = DICT_mysql_item_RAW ['host']  
   mysql_username_RAW = DICT_csv_item_RAW['username']
   mysql_password_RAW= DICT_csv_item_RAW['password']  

   mysql_db_name_RAW= DICT_csv_item_RAW['db_name'] 
   mysql_querye_RAW= DICT_csv_item_RAW['mysql_query']


   conn_str_COOKED = DICT_mongodb_item_COOKED ['conn_str']
   db_name_COOKED = DICT_mongodb_item_COOKED ['db_name']
   coll_name_COOKED = DICT_mongodb_item_COOKED ['coll_name']   


   # LIST TO_BE file & data
   LOLISTS_to_be_table_data = 
   
   LIST_table_name_and_data = []
   
   # Loop through EACH selected to_be data file 
   for LIST_table_data in LIST_raw_table_data[start_num: end_num]:
     
      data_file_only = LIST_file_data[0] #file name is always the first element 
      LIST_data_item_only = LIST_file_data[1:]
      
      #print (str(data_file_only).encode(), flush=True)
      #print (str(LIST_data_item_only).encode(), flush=True)
      
      for file_data in LIST_file_data:    
         print (str(file_data).encode(), flush=True)
         
         #do data item here 
         do_one_DATA_ITEM (data_item=file_data)



#################################################################
###### Process data items by concurrency futures (CF)
###################################################################

# Concurrent using list of 
def CF_all_data_chunk (LIST_mysql_item_RAW, LIST_mongodb_item_COOKED, do_one_DATA_ITEM):

   # get values from plg_Dict.py
   DICT_mysql_item_RAW = DICT_mysql_item (LIST_mysql_item=LIST_mysql_item_RAW)
   DICT_mongodb_item_COOKED = DICT_mongodb_item (LIST_mongodb_item=LIST_mongodb_item)
   
   # Func arg values from Dict values    
   # Func arg values from Dict values    
   folder_path_RAW                            = DICT_f_item_RAW['folder_path']  
   LIST_file_num_to_select_RAW                = DICT_f_item_RAW['LIST_file_num_to_select'] 
   file_prefix_RAW                            = DICT_f_item_RAW['file_prefix'] 
   file_extension_RAW                         = DICT_f_item_RAW['file_extension'] 

   conn_str_COOKED = DICT_mongodb_item_COOKED ['conn_str']
   db_name_COOKED = DICT_mongodb_item_COOKED ['db_name']
   coll_name_COOKED = DICT_mongodb_item_COOKED ['coll_name']    
  
   # LIST TO_BE list & data
   LOLISTS_to_be_list_data = get_LIST_to_be_SELECTED_with_data_items (LIST_mysql_item_RAW, LIST_mongodb_item_COOKED, doc_index, dict_option )
   
   start_list_index = raw_start_list_index
   end_list_index = raw_end_list_index
   
  
   # Loop through EACH selected to_be data list 
   for LIST_data_item in LOLISTS_to_be_list_data[start_list_index:end_list_index]:

      LIST_data_file_only = LIST_file_data[0] # file name is always the first element 
      LIST_data_item_only = LIST_file_data[1:]
              
      CF_one_data_chunk (do_one_DATA_ITEM=do_one_DATA_ITEM, LIST_data_item=LIST_data_item_only )



def TM_mysql_to_mongodb (LIST_file_item_RAW, LIST_mongodb_item_COOKED, do_one_DATA_ITEM, output_option):

   match output_option:

      case 'RAW_1':
         RAW_1 = get_LIST_raw_ALL (LIST_mysql_item_RAW)
         print (RAW_1)
         
      case 'RAW_2':       
         RAW_2 = get_LIST_raw_SELECTED ( LIT_mysql_item_RAW)
         print (RAW_2)
         
      case 'RAW_3':
         RAW_3 = get_raw_DATA_ITEMS (LIST_mysql_item_RAW)
         print (RAW_3)

      case 'COOKED_1':
         COOKED_1 = get_LIST_ALL_COOKED (LIST_mongodb_item_COOKED)
         print (COOKED_1)
         
      case 'COOKED_2':
         COOKED_2 = get_LIST_SELECTED_COOKED (LIST_mongodb_item_COOKED)
         print (COOKED_2)
         
      case 'COOKED_3':      
         COOKED_3 = get_DATA_ITEMS_COOKED (LIST_mongodb_item_COOKED, doc_index, dict_option)
         print (COOKED_3)

      case 'TO_BE_1':
         TO_BE_1 = get_TO_BE_DATA_ITEMS (file_path_RAW, LIST_mongodb_item_COOKED, doc_index, dict_option )
         print (TO_BE_1)
         
      case 'TO_BE_2':
         TO_BE_2 = get_LIST_to_be_SELECTED_with_data_items (LIST_file_item_RAW, LIST_mongodb_item_COOKED, doc_index, dict_option  )
         print (TO_BE_2)
   
      case 'LP':
         LP =  LP_all_data_items (LIST_file_item_RAW, LIST_mongodb_item_COOKED, do_one_DATA_ITEM)
         print (LP)
      
      case 'CF':
         CF = CF_all_data_chunk (LIST_file_item_RAW, LIST_mongodb_item_COOKED, do_one_DATA_ITEM)



#################################################################
###### TEST OUTPUT 
#################################################################

def TEST_OUTPUT (output_option):

   # RAW data 
   host_R ='localhost'
   username_R = 'root'
   password_R = ''

   db_name_R = 'joomla112'
   table_select_mode_R = 'by_index'
   table_name_R = ''
   
   start_table_index_R = 0
   end_table_index_R = 2
   
   LIST_table_to_select_R = []
   mysql_query_R = ''


   LIST_mysql_item_RAW = [host_R, username_R, password_R, db_name_R, table_select_mode_R, table_name_R, start_table_index_R, end_table_index_R, LIST_table_to_select_R, mysql_query_R]

   # COOKED data
   conn_str_C ="mongodb://localhost:27017/"
   db_name_C = "mydatabase"
   coll_select_mode_C = ''
   coll_name_C = "people"

   start_coll_index_C = 0
   end_coll_index_C = 0
   LIST_coll_item_to_select_C = []

   doc_select_mode_C = 'by_query'
   doc_key_C = 'doc_title'
   doc_id_C = ''
   doc_title_C = ''
   
   doc_index_C =0
   start_doc_index_C = 0
   end_doc_index_C = 1
   LIST_doc_item_to_select_C = ['shane', 'peter']

   LIST_mongodb_item_COOKED = [conn_str_C, db_name_C, coll_select_mode, coll_name,  start_coll_index, end_coll_index, LIST_coll_item_to_select, doc_select_mode, doc_key, doc_id, doc_title, doc_index, start_doc_index, end_doc_index, LIST_doc_item_to_select]

   dict_option = 'key'
  
   TM_mysql_to_mongodb (LIST_file_item_RAW, LIST_mongodb_item_COOKED, do_one_DATA_ITEM, output_option)      
   
   
   
   
#must run concurrency using if __name__ == '__main__'
if __name__ == '__main__':
   
   #TEST_OUTPUT (output_option='RAW_1')
   #TEST_OUTPUT (output_option='RAW_2')
   #TEST_OUTPUT (output_option='RAW_3')
   
   #TEST_OUTPUT (output_option='COOKED_1')
   #TEST_OUTPUT (output_option='COOKED_2')
   #TEST_OUTPUT (output_option='COOKED_3')
   
   #TEST_OUTPUT (output_option='TO_BE_1')
   #TEST_OUTPUT (output_option='TO_BE_2')
   
   #TEST_OUTPUT (output_option='LP')
   #TEST_OUTPUT (output_option='CF')