

import sys
sys.path.append('../a0_plg_CUSTOM/') 
sys.path.append('../plg_TFM/') 
sys.path.append('../plg_DICT/') 

from plg_DICT_database import * 


from a0_items import * 
from plg_DB_Mysql import * 

from concurrent.futures import ThreadPoolExecutor, wait
import concurrent.futures
import time 
import datetime



### RAW
def get_LIST_raw_ALL (raw_My_host, raw_My_user, raw_My_pass):

   LIST_raw_ALL = Mysql_get_ALL_DB (My_host=raw_My_host, My_user=raw_My_user, My_pass=raw_My_pass)
   
   return LIST_raw_ALL 
   
  
def get_LIST_raw_SELECTED (raw_start_db_index, raw_end_db_index, raw_My_host, raw_My_user, raw_My_pass):

   LIST_raw_ALL = get_LIST_raw_ALL (raw_My_host=raw_My_host, raw_My_user=raw_My_user, raw_My_pass=raw_My_pass)

   LIST_raw_selected = []
   
   for raw_db in LIST_raw_ALL(raw_start_db_index=raw_start_db_index, raw_end_db_index=raw_end_db_index):
   
      LIST_raw_selected.append(raw_db)
           
   return LIST_raw_selected


def get_raw_DATA_ITEMS (raw_My_host, raw_My_user, raw_My_pass , raw_My_db_name, raw_My_select_query):
  
   LIST_raw_data_item = Mysql_select_tb_data (My_host=raw_My_host, My_user=raw_My_user, My_pass=raw_My_pass , My_db_name=raw_My_db_name, My_select_query=raw_My_select_query)
   
   return LIST_raw_data_item  
  
  
  
  
### COOKED   
def get_LIST_cooked_ALL (cooked_My_host, cooked_My_user, cooked_My_pass):

   LIST_cooked_ALL = Mysql_get_ALL_DB (My_host=cooked_My_host, My_user=cooked_My_user, My_pass=cooked_My_pass)
   
   return LIST_cooked_ALL 
   
  

def get_LIST_cooked_SELECTED (cooked_start_db_index, cooked_end_db_index, cooked_My_host, cooked_My_user, cooked_My_pass):

   LIST_cooked_ALL = get_LIST_cooked_ALL (cooked_My_host=cooked_My_host, cooked_My_user=cooked_My_user, cooked_My_pass=cooked_My_pass)

   LIST_cooked_selected = []
   
   #must use index to select database
   for cooked_db in LIST_cooked_ALL(cooked_start_db_index=cooked_start_db_index, cooked_end_db_index=cooked_end_db_index):
   
      LIST_cooked_selected.append(cooked_db)
           
   return LIST_cooked_selected



#### Select data with log status = Completed, In progress, Not completed within allowed task duration
def get_cooked_DATA_ITEMS (cooked_My_host, cooked_My_user, cooked_My_pass , cooked_My_db_name, cooked_My_select_query):

   LIST_cooked_data_item = Mysql_select_tb_data (My_host=cooked_My_host, My_user=cooked_My_user, My_pass=cooked_My_pass , My_db_name=cooked_My_db_name, My_select_query=cooked_My_select_query)
      
   return LIST_cooked_data_item 



#get_cooked_DATA_ITEMS (cooked_My_host, cooked_My_user, cooked_My_pass , cooked_My_db_name, cooked_My_select_query)


def get_TO_BE_DATA_ITEMS (raw_My_host, raw_My_user, raw_My_pass , raw_My_db_name, raw_My_select_query, cooked_My_host, cooked_My_user, cooked_My_pass , cooked_My_db_name, cooked_My_select_query):

   LIST_raw =  get_raw_DATA_ITEMS (raw_My_host=raw_My_host, raw_My_user=raw_My_user, raw_My_pass = raw_My_pass , raw_My_db_name=raw_My_db_name, raw_My_select_query=raw_My_select_query)
   LIST_cooked = get_cooked_DATA_ITEMS (cooked_My_host=cooked_My_host, cooked_My_user=cooked_My_user, cooked_My_pass=cooked_My_pass , cooked_My_db_name=cooked_My_db_name, cooked_My_select_query=cooked_My_select_query)
   
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
   
   
   
# split data item to get data chunk   
def split_to_be_DATA_ITEMS (raw_My_host, raw_My_user, raw_My_pass , raw_My_db_name, raw_My_select_query, cooked_My_host, cooked_My_user, cooked_My_pass , cooked_My_db_name, cooked_My_select_query, start_index, items_per_list):
 
   LIST_to_be_DATA_ITEM = get_TO_BE_DATA_ITEMS (raw_My_host=raw_My_host, raw_My_user=raw_My_user, raw_My_pass=raw_My_pass , raw_My_db_name=raw_My_db_name, raw_My_select_query=raw_My_select_query, cooked_My_host=cooked_My_host, cooked_My_user=cooked_My_user, cooked_My_pass=cooked_My_pass , cooked_My_db_name=cooked_My_db_name, cooked_My_select_query=cooked_My_select_query)
   
   return list_SPLIT_1 (LIST_to_split = LIST_to_be_DATA_ITEM, start_index = start_index, items_per_list = items_per_list)




# do the task on 1 data item, eg send email, post comment   
## this method needs to be created from scratch to be used by CF_data_chunk (LIST_item)
def do_task_DATA_ITEM (data_item):

   print (data_item)   
   
   

#####################################################################
##### Selected TO_BE data dbs with TO_BE data items 

def get_LIST_to_be_SELECTED_with_data_items ( raw_My_user, raw_My_pass , raw_My_db_name, raw_start_db_index, raw_end_db_index, raw_My_host, raw_My_select_query, cooked_start_db_index, cooked_end_db_index, cooked_My_host, cooked_My_user, cooked_My_pass , cooked_My_db_name, cooked_My_select_query ):

   LIST_raw_db_SELECTED =  get_LIST_raw_SELECTED (raw_start_db_index=raw_start_db_index, raw_end_db_index=raw_end_db_index, raw_My_host=raw_My_host, raw_My_user=raw_My_user, raw_My_pass=raw_My_pass)
   LIST_cooked_db_SELECTED = get_LIST_cooked_SELECTED (cooked_start_db_index=cooked_start_db_index, cooked_end_db_index=cooked_end_db_index, cooked_My_host=cooked_My_host, cooked_My_user=cooked_My_user, cooked_My_pass=cooked_My_pass)
   
   #TO_BE lists & data 
   LOLISTS_to_be_data_SELECTED = []
   
   # get_TO_BE_DATA_ITEMS returns LOLISTS_to_be_data_SELECTED
   for raw_list, cooked_list in zip(LIST_raw_list_SELECTED, LIST_cooked_list_SELECTED):

      #LIST_to_be_list_data_SELECTED.append( raw_list + ' #_0 ' + get_TO_BE_DATA_ITEMS (raw_list = raw_LOLISTS + raw_list, cooked_list = cooked_LOLISTS + cooked_list) )
      LIST_TO_BE_item = get_TO_BE_DATA_ITEMS (raw_list=raw_list, cooked_list=cooked_list)
      LIST_TO_BE_item.insert(0, raw_list)
      
      LOLISTS_to_be_data_SELECTED.append(LIST_TO_BE_item)


#get_LIST_to_be_SELECTED_with_data_items (start_db, end_db, raw_folder_path, cooked_folder_path, DB_db_name )



###############################################################
###### Process data items by loop (LP)
##############################################################
  
# Process data item by loop
def LP_all_data_items ():

   # LIST TO_BE file & data
   LIST_raw_file_data = get_LIST_raw_selected_with_data_item (raw_folder_path=raw_folder_path, start_num=start_num, end_num=end_num)
   
   LIST_file_name_and_data = []
   
   # Loop through EACH selected to_be data file 
   for LIST_file_data in LIST_raw_file_data[start_num: end_num]:
     
      data_file_only = LIST_file_data[0] #file name is always the first element 
      LIST_data_item_only = LIST_file_data[1:]
      
      #print (str(data_file_only).encode(), flush=True)
      #print (str(LIST_data_item_only).encode(), flush=True)
      
      for file_data in LIST_file_data:
      
         print (str(file_data).encode(), flush=True)
         
         #do data item here 
         #do_one_DATA_ITEM_2 (data_item)





#################################################################
###### Process data items by concurrency futures (CF)
###################################################################

def CF_data_chunk (LIST_item):

   with concurrent.futures.ProcessPoolExecutor() as executor:
        
      executor.map(do_task_DATA_ITEM, LIST_item)
        
      t2 = time.perf_counter()
      print (f' finished in {t2} seconds')      



# Concurrent using list of 
def CF_all_data_chunk (raw_list, raw_start_list_index, raw_end_list_index, cooked_LOLISTS, cooked_list, cooked_Start_list_index, cooked_end_list_index, start_index, items_per_list, do_one_DATA_ITEM):
  
   # LIST TO_BE list & data
   LOLISTS_to_be_list_data = get_LIST_to_be_SELECTED_with_data_items (raw_LOLISTS=raw_LOLISTS, raw_start_list_index=raw_start_list_index, raw_end_list_index=raw_end_list_index, cooked_LOLISTS=cooked_LOLISTS, cooked_start_list_index=cooked_start_list_index, cooked_end_list_index=cooked_end_list_index)
   
   start_list_index = raw_start_list_index
   end_list_index = raw_end_list_index
   
  
   # Loop through EACH selected to_be data list 
   for LIST_data_item in LOLISTS_to_be_list_data[start_list_index:end_list_index]:

      LIST_data_file_only = LIST_file_data[0] # file name is always the first element 
      LIST_data_item_only = LIST_file_data[1:]
              
      LIST_data_item_chunk = split_LIST_data_item  (LIST_to_split=LIST_data_item_only, start_index=start_index, items_per_list=items_per_list)         
            
      for data_item_chunk in LIST_data_item_chunk:    
                  
         CF_data_chunk (do_one_DATA_ITEM = do_one_DATA_ITEM, LIST_item=data_item_chunk) 



def TM_mysql_to_mysql ():

   pass


#do_task_DATA_ITEM --> need write this function to be used by CF_data_chunk (LIST_item)


raw_My_host = ''
raw_My_user = ''
raw_My_pass = ''
raw_My_db_name = ''
raw_My_select_query = ''
raw_My_start_db_index = ''
raw_My_end_db_index = ''


cooked_My_host = ''
cooked_My_user = ''
cooked_My_pass = ''
cooked_My_db_name = ''
cooked_My_select_query = ''
cooked_My_start_db_index = ''
cooked_My_end_db_index = ''

start_index = ''
items_per_list = ''

do_one_DATA_ITEM = ''# this is a function to complete 1 data item 
LIST_item = ''



#CF_all_data_chunk (raw_My_host, raw_My_user, raw_My_pass , raw_My_db_name, raw_My_select_query, cooked_My_host, cooked_My_user, cooked_My_pass , cooked_My_db_name, cooked_My_select_query, start_index, items_per_list)