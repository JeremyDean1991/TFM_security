

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

from plg_Files import * 
from plg_Folders import * 

from concurrent.futures import ThreadPoolExecutor, wait
import concurrent.futures
import time 
import datetime

##### Must download & install MongoDB software from --> https://www.mongodb.com/try/download/community #######
# https://www.w3schools.com/python/python_mongodb_getstarted.asp


##### plg_TFM_do_task_1 - MongoDB to MongoDB #########################################

### The following code is to be executed on the TFM server side, not from TFM master #######
############################################################################################
##### RAW, COOKED data files #######


# get a list of raw COLLECTIONS from a MongoDB database 
def get_LIST_raw_ALL (raw_folder_path):

   LIST_raw_ALL = get_ALL_in_folder (folder_path=raw_folder_path)
   
   return LIST_raw_ALL 
   
 
#get_LIST_raw_ALL (folder_path)
 
  
# get selected files by index
def get_LIST_raw_SELECTED (raw_folder_path, raw_raw_start_file_index, raw_raw_end_file_index):

   LIST_raw_ALL = get_LIST_raw_ALL (raw_folder_path=raw_folder_path)

   LIST_raw_selected = []
   
   for raw_file in LIST_raw_ALL(raw_start_file_index=raw_start_file_index, raw_end_file_index=raw_end_file_index):
   
      LIST_raw_selected.append(raw_file)
           
   return LIST_raw_selected  
  
  
  
  
def get_raw_DATA_ITEMS (raw_file_path):
  
   LIST_raw_data_item = File_read_lines (file_path = raw_file_path)
   
   return LIST_raw_data_item 



  
# get ALL DOCS in a collection   
def get_LIST_ALL_COOKED (LIST_mongodb_item_COOKED):

   DICT_m_item_COOKED = DICT_mongodb_item (LIST_mongodb_item=LIST_mongodb_item)
   
   conn_str_COOKED = DICT_m_item_COOKED ['conn_str']
   db_name_COOKED = DICT_m_item_COOKED ['db_name']
   coll_name_COOKED = DICT_m_item_COOKED ['coll_name']

   LIST_ALL_doc_COOKED = get_ALL_docs_in_collection (conn_str=conn_str, db_name=db_name, coll_name=coll_name)
   
   return LIST_ALL_doc_COOKED 
   

'''
conn_str ="mongodb://localhost:27017/"
db_name = "mydatabase"
coll_name = "mycoll"

start_coll_index = 0
end_coll_index = 0
LIST_coll_num_to_select = []

doc_key = ''
start_doc_index = 0
end_doc_index = 0
LIST_doc_num_to_select = []

LIST_mongodb_item_COOKED = [conn_str, db_name, coll_name, start_coll_index, end_coll_index, LIST_coll_num_to_select, doc_key, start_doc_index, end_doc_index, LIST_doc_num_to_select]

cooked_ALL_doc = get_LIST_cooked_ALL (LIST_mongodb_item=LIST_mongodb_item_COOKED)

print (cooked_ALL_doc)
'''



def get_LIST_SELECTED_COOKED (LIST_mongodb_item_COOKED):

   DICT_m_item_COOKED = DICT_mongodb_item (LIST_mongodb_item=LIST_mongodb_item_COOKED)
   
   start_doc_index_COOKED = DICT_m_item_COOKED ['start_doc_index']
   end_doc_index_COOKED = DICT_m_item_COOKED ['end_doc_index']  
   doc_select_mode = DICT_m_item_COOKED ['doc_select_mode']
   LIST_doc_item_to_select_COOKED = DICT_m_item_COOKED ['LIST_doc_item_to_select']
   
   
   LIST_ALL_doc_COOKED = get_LIST_cooked_ALL (LIST_mongodb_item= LIST_mongodb_item_COOKED)

   LIST_selected_DOC_COOKED = []
   
   
   # select file by list item or by index?
   if doc_select_mode == 'by_item': # item could be number or string 

      for item in LIST_doc_item_to_select_COOKED:
          
         for doc in LIST_ALL_doc_COOKED:
         
            doc_str = str(doc)
         
            if item in doc_str:
      
               LIST_selected_DOC_COOKED.append (doc)
               print ('raw doc selected => ' + str(doc), flush=True)
         
            else:
      
               #print ('raw file NOT selected => ' + str(file), flush=True)
               pass
   
     
   if doc_select_mode == 'by_index':
   
      for cooked_doc in LIST_ALL_doc_COOKED[start_doc_index_COOKED : end_doc_index_COOKED ]:
   
         LIST_selected_DOC_COOKED.append(cooked_doc)
                 
   else:
   
      pass
           
  
   return LIST_selected_DOC_COOKED
      

'''
conn_str ="mongodb://localhost:27017/"
db_name = "mydatabase"
coll_name = "mycoll"

start_coll_index = 0
end_coll_index = 0
LIST_coll_num_to_select = []

doc_key = ''
start_doc_index = 1
end_doc_index = 3
LIST_doc_num_to_select = []

LIST_mongodb_item_COOKED = [conn_str, db_name, coll_name, start_coll_index, end_coll_index, LIST_coll_num_to_select, doc_key, start_doc_index, end_doc_index, LIST_doc_num_to_select]

cooked_SELECTED = get_LIST_cooked_SELECTED (LIST_mongodb_item_COOKED=LIST_mongodb_item_COOKED)      

print (cooked_SELECTED)
'''


# get lines of ONE db doc
def get_DATA_ITEMS_COOKED (LIST_mongodb_item_COOKED, LIST_doc):

   DICT_m_item_COOKED = DICT_mongodb_item (LIST_mongodb_item=LIST_mongodb_item_COOKED)
   
   conn_str_COOKED = DICT_m_item_COOKED ['conn_str']
   db_name_COOKED = DICT_m_item_COOKED ['db_name']
   coll_name_COOKED = DICT_m_item_COOKED ['coll_name']   
  
   # get value of a key from a doc 
   doc_key_COOKED =  DICT_m_item_COOKED ['doc_key'] 


   # get all values of a specific doc 
   LIST_doc_item_COOKED_1 = LIST_doc[doc_index].items()
       
   LIST_doc_item_COOKED_2 = []
   
   
    # get all lines from a doc 
   if dict_option == 'all':
   
      for doc_key_value in LIST_doc_item_COOKED_1:
      
         LIST_data_item_COOKED_2.append(doc_key_value)
         
         
   # get value of a key from a doc 
   if dict_option == 'key':
   
      for item in LIST_doc_item_COOKED_1:
   
         try: 
         
            # eg, cooked_doc_key = 'email'
            doc_value = item[doc_key_COOKED]
      
            #print (item, flush=True)
            LIST_data_item_COOKED_2.append (doc_value)
                 
         except:
      
         #print ("An error has occured")
            pass 
            
   else:
   
      pass   
            
         
   return LIST_data_item_COOKED_2 

'''
conn_str ="mongodb://localhost:27017/"
db_name = "mydatabase"
coll_name = "mycoll"

start_coll_index = 0
end_coll_index = 0

LIST_coll_num_to_select = []

doc_key = '' # 'email'
start_doc_index = 0
end_doc_index = 3
LIST_doc_num_to_select = []

LIST_mongodb_item_COOKED = [conn_str, db_name, coll_name, start_coll_index, end_coll_index, LIST_coll_num_to_select, doc_key, start_doc_index, end_doc_index, LIST_doc_num_to_select]

get_cooked_DATA_ITEMS (LIST_mongodb_item_COOKED=LIST_mongodb_item_COOKED)
'''



# TO_BE 
def get_TO_BE_DATA_ITEMS (LIST_list_item, LIST_mongodb_item):

   LIST_raw = get_raw_DATA_ITEMS (raw_file_path = raw_file_path)
   LIST_cooked = get_cooked_DOCS(cooked_conn_str=cooked_conn_str, cooked_db_name=cooked_db_name, cooked_coll=cooked_coll)
   
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
def split_to_be_DATA_ITEMS (raw_file_path, cooked_file_path, start_index, items_per_list):
 
   LIST_to_be_DATA_ITEM = get_TO_BE_DATA_ITEMS (raw_file_path = raw_file_path, cooked_file_path = cooked_file_path)
   
   return list_SPLIT_1 (LIST_to_split = LIST_to_be_DATA_ITEM, start_index = start_index, items_per_list = items_per_list)




   

#####################################################################
##### Selected TO_BE collections with TO_BE documents

#####################################################################
##### Selected TO_BE data files with TO_BE data items 

def get_LIST_to_be_SELECTED_with_data_items ( raw_folder_path, raw_raw_start_file_index, raw_raw_end_file_index, cooked_conn_str, cooked_db_name, cooked_start_coll_index, cooked_end_coll_index):

   LIST_raw_file_SELECTED =  get_LIST_raw_SELECTED (raw_folder_path=raw_folder_path, raw_raw_start_file_index=raw_start_file_index, raw_raw_end_file_index=raw_end_file_index)
   LIST_cooked_file_SELECTED = get_LIST_cooked_SELECTED (cooked_conn_str=cooked_conn_str, cooked_db_name=cooked_db_name, cooked_start_coll_index=cooked_start_coll_index, cooked_end_coll_index=cooked_end_coll_index)
   
   #TO_BE lists & data 
   LOLISTS_to_be_data_SELECTED = []
   
   # get_TO_BE_DATA_ITEMS returns LOLISTS_to_be_data_SELECTED
   for raw_list, cooked_list in zip(LIST_raw_list_SELECTED, LIST_cooked_list_SELECTED):

      #LIST_to_be_list_data_SELECTED.append( raw_list + ' #_0 ' + get_TO_BE_DATA_ITEMS (raw_list = raw_LOLISTS + raw_list, cooked_list = cooked_LOLISTS + cooked_list) )
      LIST_TO_BE_item = get_TO_BE_DATA_ITEMS (raw_list=raw_list, cooked_list=cooked_list)
      LIST_TO_BE_item.insert(0, raw_list)
      
      LOLISTS_to_be_data_SELECTED.append(LIST_TO_BE_item)
      

   return LOLISTS_to_be_data_SELECTED


#get_LIST_to_be_SELECTED_with_data_items (raw_start_file, raw_end_file, raw_folder_path, cooked_folder_path )


###############################################################
###### Process data items by loop (LP)
##############################################################

# Process data item by loop
def LP_data_item_ALL   (LIST_list_item_RAW, LIST_mongodb_item_COOKED):

   
   DICT_f_item_RAW   = DICT_list_item (LIST_list_item=LIST_list_item_RAW)
   
   start_data_list_index_RAW                       = DICT_f_item_RAW['start_data_list_index'] 
   end_data_list_index_RAW                         = DICT_f_item_RAW['end_data_list_index']
  
  
   LIST_data_item_TO_BE =  get_data_items_TO_BE (LIST_list_item_RAW, LIST_mongodb_item_COOKED)
   data_list_only = LIST_data_item_TO_BE[0]
   print ('data list only => ' + str(data_list_only))
   
   
   # Loop through EACH selected to_be data csv 
   for data_item in LIST_data_item_TO_BE[start_data_list_index_RAW:end_data_list_index_RAW] :
          
      # do data item here 
      do_one_DATA_ITEM (data_item) 




def LP_all_data_items ():

   # LIST TO_BE file & data
   LIST_raw_file_data = get_LIST_raw_selected_with_data_item (raw_folder_path=raw_folder_path, start_num=start_num, end_num=end_num)
   
   LIST_file_name_and_data = []
   
   # Loop through EACH selected to_be data file 
   for LIST_file_data in LIST_raw_file_data[start_num: end_num]:
     
      data_file_only = LIST_file_data[0] # file name is always the first element 
      LIST_data_item_only = LIST_file_data[1:]
      
      #print (str(data_file_only).encode(), flush=True)
      #print (str(LIST_data_item_only).encode(), flush=True)
      
      for data_item in LIST_data_item_only:
      
         print (str(data_item).encode(), flush=True)
         
         #do data item here 
         do_one_DATA_ITEM (data_item)



#################################################################
###### Process data items by concurrency futures (CF)
##################################################################

## do_task_DATA_ITEM --> CF_data_chunk (LIST_item) --> CF_all_data_chunk (raw_start_file, raw_end_file, raw_folder_path, cooked_folder_path, start_index, items_per_list)

# Concurrent using list of list
def CF_all_data_chunk_1 (raw_list, raw_start_list_index, raw_end_list_index, cooked_LOLISTS, cooked_list, cooked_Start_list_index, cooked_end_list_index, start_index, items_per_list, do_one_DATA_ITEM):
  
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



def TM_list_to_mongodb ():

   pass



#do_task_DATA_ITEM --> need write this function to be used by CF_data_chunk (LIST_item)

raw_folder_path = ''
raw_file_path = ''
raw_start_file_index = ''
raw_end_file_index = ''

cooked_conn_str = ''
cooked_db_name = ''
cooked_coll = ''
cooked_doc_key = ''
cooked_start_coll_index = ''
cooked_end_coll_index = ''

start_index = ''
items_per_list = ''


#CF_all_data_chunk (raw_folder_path, raw_file_path, raw_start_file_index, raw_end_file_index, cooked_conn_str, cooked_db_name, cooked_coll, cooked_doc_key, cooked_start_coll_index, cooked_end_coll_iondex, start_index, items_per_list)