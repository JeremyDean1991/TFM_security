


import sys 
sys.path.append('../plg_TFM/') 
sys.path.append('../plg_DICT/')

from plg_DICT_database import * 

import pymongo 
from pymongo import MongoClient
from pprint import pprint
import bson

from plg_DB_MongoDB_2 import * 
from a0_plg_DICT_data import * 

from plg_csvs import * 
from plg_Folders import * 

from concurrent.futures import ThreadPoolExecutor, wait
import concurrent.futures
import time 
import datetime

##### Must download & install MongoDB software from --> https://www.mongodb.com/try/download/community #######
# https://www.w3schools.com/python/python_mongodb_getstarted.asp


##### CSV to MongoDB #########################################

### RAW data items 
def get_LIST_raw_ALL (LIST_csv_item):

   DICT_csv_item_RAW = DICT_csv_item (LIST_csv_item=LIST_csv_item_RAW)
   
   folder_path_RAW = DICT_csv_item_RAW ['folder_path']

   LIST_ALL_RAW = get_ALL_in_folder (folder_path=folder_path_RAW)
   
   LIST_csv_RAW = []
   
   for csv in LIST_ALL_RAW:
   
      if '.csv' in csv:
      
         LIST_csv_RAW.append(csv)
         
      else:
      
         pass
   
   return LIST_raw_csv 
   
   
'''
f_path = '../../data/raw/' 
LIST_csv = get_LIST_raw_ALL (raw_folder_path=f_path)
print (LIST_csv) 
''' 
 
 
 
# get selected csvs by index
def get_LIST_raw_SELECTED (LIST_csv_item_RAW):

   DICT_csv_item_RAW = DICT_csv_item (LIST_csv_item=LIST_csv_item_RAW)
   
   folder_path_RAW = DICT_csv_item_RAW ['folder_path']
  
   LIST_csv_to_select_RAW       = DICT_f_item_RAW['LIST_csv_to_select'] 
   
   csv_select_mode_RAW = DICT_csv_item_RAW['csv_select_mode']
   
   start_csv_index_RAW = DICT_csv_item_RAW['start_csv_index']
   end_csv_index_RAW = DICT_csv_item_RAW['end_csv_index']
   
 
   LIST_ALL_RAW = get_LIST_raw_ALL (raw_folder_path=raw_folder_path)

   LIST_raw_selected = []
   
   # select csv by list item or by index?
   if csv_select_mode_RAW == 'by_query': # item could be number or string   
      print ('select by list item')

      for csv_RAW in LIST_csv_to_select_RAW:
             
         if csv_RAW in LIST_csv_ALL_RAW:
      
            LIST_selected_RAW.append (csv_RAW)
            #print ('raw csv selected => ' + str(item), flush=True)
            
         
         else:
      
            #print ('raw csv NOT selected => ' + str(item), flush=True)
            pass
            
   if csv_select_mode_RAW == 'by_index':  
      print ('select by list index')
    
      for csv in LIST_csv_ALL_RAW [start_csv_index_RAW:end_csv_index_RAW]:
       
         LIST_selected_RAW.append (csv)
           
   else:
     
     pass
      
          
   return LIST_selected_RAW 
  

'''  
folder_path = '../../data/raw/' 
csv_path = ' ' 

csv_select_mode = ''
start_csv_index = 0 
end_csv_index = 2

LIST_csv_to_select = []
csv_prefix = 'test_csv_'
csv_extension= '.csv'
LIST_csv_column = []


LIST_csv_item_RAW = [folder_path, csv_path, csv_select_mode, start_csv_index, end_csv_index, LIST_csv_to_select, csv_prefix, csv_extension, LIST_csv_column]
LIST_selected = get_LIST_raw_SELECTED (LIST_csv_item_RAW=LIST_csv_item_RAW)
  
print (LIST_selected)
'''  
  
  
def get_raw_DATA_ITEMS (LIST_csv_item):
   
   DICT_csv_item_RAW = DICT_csv_item (LIST_csv_item=LIST_csv_item_RAW)
   
   # may need to create a different DICT variable list if its a different csv path
   csv_path_RAW = DICT_csv_item_RAW ['csv_path']
  
   LIST_raw_data_item = CSV_dict_reader ( path_CSV=csv_path_RAW)
   
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
   doc_select_mode_COOKED = DICT_m_item_COOKED ['doc_select_mode']
   LIST_doc_to_select_COOKED = DICT_m_item_COOKED ['LIST_doc_to_select']
   
   
   LIST_ALL_doc_COOKED = get_LIST_ALL_COOKED (LIST_mongodb_item_COOKED= LIST_mongodb_item_COOKED)

   LIST_selected_DOC_COOKED = []
   
   
   # select csv by list item or by index?
   if doc_select_mode_COOKED == 'by_title': # item could be number or string 
      print ('select by list item')

      for item in LIST_doc_to_select_COOKED:
          
         for doc in LIST_ALL_doc_COOKED:
         
            doc_str = str(doc)
         
            if item in doc_str:
      
               LIST_selected_DOC_COOKED.append (doc)
               print (str(item) + ' => in doc => ' + str(doc), flush=True)
         
            else:
      
               #print (str(item) + ' => NOT in doc => ' + str(doc), flush=True)
               pass
   
     
   if doc_select_mode_COOKED == 'by_index':
      print ('select by list index')
   
      for cooked_doc in LIST_ALL_doc_COOKED[start_doc_index_COOKED : end_doc_index_COOKED ]:
   
         LIST_selected_DOC_COOKED.append(cooked_doc)
                 
   else:
   
      pass
           
  
   return LIST_selected_DOC_COOKED



# get data items of the selected cooked csvs 
def get_data_items_COOKED (LIST_mongodb_item_COOKED):

   DICT_m_item_COOKED = DICT_mongodb_item (LIST_mongodb_item=LIST_mongodb_item_COOKED)
   
   doc_key_COOKED = DICT_m_item_COOKED ['doc_key']
   doc_key_value_option_COOKED = DICT_m_item_COOKED ['doc_key_value_option']


   LIST_doc_SELECTED = get_LIST_SELECTED_COOKED (LIST_mongodb_item_COOKED)
   
   LIST_doc_item_COOKED_2 = []
   
   LOLISTS_doc_items = []


   for doc in LIST_doc_SELECTED:
   
      LIST_doc_item_COOKED_1 =  doc.items()
      
      # get all keys + values from a doc 
      if doc_key_value_option_COOKED == 'all':
         print ("get ALL doc keys + values")
   
         for doc_key_value in LIST_doc_item_COOKED_1:
      
            LIST_doc_item_COOKED_2.append(doc_key_value) 
            
            LIST_doc_item_COOKED_2.insert(0, doc)   
         
         LOLISTS_doc_items.append (LIST_doc_item_COOKED_2)
            
         
      # get value of a key from a doc 
      if doc_key_value_option_COOKED == 'key':
         print ("get ALL doc values by 1 key")

         # must convert doc into dictionary first      
         Dict_1 = dict(LIST_doc_item_COOKED_1)
         
         doc_value = get_DICT_value_by_key (my_DICT=Dict_1, my_KEY=doc_key_COOKED) # get value of a key from a doc
         print (doc_value)
      
         #print (item, flush=True)
         LIST_doc_item_COOKED_2.append (doc_value)           
         
         LIST_doc_item_COOKED_2.insert(0, doc)
            
      LOLISTS_doc_items.append (LIST_doc_item_COOKED_2)
                 
           
      
   return LOLISTS_doc_items



# TO_BE data items of the selected RAW & COOKED csvs 
# TO_BE is a single list NOT list of lists 
def get_data_items_TO_BE (LIST_csv_item_RAW, LIST_mongodb_item_COOKED):

   LOLISTS_csv_data_item_RAW = get_data_items_RAW (LIST_csv_item_RAW = LIST_csv_item_RAW)
   LOLISTS_doc_data_item_COOKED = get_data_items_COOKED (LIST_mongodb_item_COOKED = LIST_mongodb_item_COOKED)
   
   LIST_data_item_TO_BE = []
   

   for LIST_csv_data_item_RAW in LOLISTS_csv_data_item_RAW:
   
      for LIST_doc_data_item_COOKED in LOLISTS_doc_data_item_COOKED:
      
         for csv_data_item_RAW in LIST_csv_data_item_RAW:
         
            if csv_data_item_RAW in LIST_doc_data_item_COOKED:
         
               #print (str(csv_data_item_RAW) + ' in ' + str(LIST_doc_data_item_COOKED))
               pass

            else:
         
               print (str(csv_data_item_RAW) + ' NOT in ' + str(LIST_doc_data_item_COOKED))
               
               LIST_data_item_TO_BE.append (csv_data_item_RAW)
               
                              
   return LIST_data_item_TO_BE

       
###############################################################
###### Process data items by loop (LP)
##############################################################
  
def LP_data_item_ALL   (LIST_csv_item_RAW, LIST_mongodb_item_COOKED):

   
   DICT_f_item_RAW   = DICT_csv_item (LIST_csv_item=LIST_csv_item_RAW)
   
   start_data_list_index_RAW                       = DICT_f_item_RAW['start_data_list_index'] 
   end_data_list_index_RAW                         = DICT_f_item_RAW['end_data_list_index']
  
  
   LIST_data_item_TO_BE =  get_data_items_TO_BE (LIST_csv_item_RAW, LIST_mongodb_item_COOKED)
   data_csv_only = LIST_data_item_TO_BE[0]
   print ('data csv only => ' + str(data_csv_only))
   
   
   # Loop through EACH selected to_be data csv 
   for data_item in LIST_data_item_TO_BE[start_data_list_index_RAW:end_data_list_index_RAW] :
          
      # do data item here 
      do_one_DATA_ITEM (data_item) 



#################################################################
###### Process data items by concurrency futures (CF)
###################################################################

def CF_data_chunk_ALL (LIST_csv_item_RAW, LIST_mongodb_item_COOKED, LIST_concurrency_item_RAW):

   
   DICT_f_item_RAW   = DICT_csv_item (LIST_csv_item=LIST_csv_item_RAW)   
   start_data_list_index_RAW                       = DICT_f_item_RAW['start_data_list_index'] 
   end_data_list_index_RAW                         = DICT_f_item_RAW['end_data_list_index']
   
   
   DICT_c_item_RAW   = DICT_concurrency_item (LIST_concurrency_item = LIST_concurrency_item_RAW)   
   LIST_data_item_split = DICT_c_item_RAW['LIST_data_item_split'] 
   start_index = DICT_c_item_RAW['start_index'] 
   items_per_list = DICT_c_item_RAW['items_per_list'] 
   pause_secs = DICT_c_item_RAW['pause_secs'] 
   
     
   LIST_data_item_TO_BE =  get_data_items_TO_BE (LIST_csv_item_RAW, LIST_mongodb_item_COOKED) 
   data_csv_only = LIST_data_item_TO_BE[0]
   print ('data csv only => ' + str(data_csv_only))


   CF_all_data_chunks (LIST_data_item_split=LIST_data_item_split, start_index=start_index, items_per_list=items_per_list, do_one_DATA_ITEM=do_one_DATA_ITEM, pause_secs=pause_secs )

  




def TFM_csv_to_mongodb (LIST_csv_item_RAW, LIST_mongodb_item_COOKED, do_one_DATA_ITEM, output_option):


   match output_option:

      case 'RAW_1':
         RAW_1 = get_LIST_ALL_RAW (LIST_csv_item_RAW=LIST_csv_item_RAW)
         print (RAW_1)
         
      case 'RAW_2':       
         RAW_2 = get_LIST_SELECTED_RAW (LIST_csv_item_RAW=LIST_csv_item_RAW)
         print (RAW_2)
         
      case 'RAW_3':
         RAW_3 = get_data_items_RAW (csv_path_RAW)
         print (RAW_3)

      case 'COOKED_1':
         COOKED_1 = get_LIST_ALL_COOKED (LIST_mongodb_item_COOKED)
         print (COOKED_1)
         
      case 'COOKED_2':
         COOKED_2 = get_LIST_SELECTED_COOKED (LIST_mongodb_item_COOKED)
         print (COOKED_2)
         
      case 'COOKED_3':      
         COOKED_3 = get_DATA_ITEMS_COOKED (LIST_mongodb_item_COOKED)
         print (COOKED_3)

      case 'TO_BE_1':
         TO_BE_1 = get_TO_BE_DATA_ITEMS (csv_path_RAW, LIST_mongodb_item_COOKED )
         print (TO_BE_1)
         
      case 'TO_BE_2':
         TO_BE_2 = get_LIST_to_be_SELECTED_with_data_items (LIST_csv_item_RAW, LIST_mongodb_item_COOKED  )
         print (TO_BE_2)
   
      case 'LP':
         LP =  LP_all_data_items (LIST_csv_item_RAW, LIST_mongodb_item_COOKED, do_one_DATA_ITEM)
         print (LP)
      
      case 'CF':
         CF = CF_all_data_chunk (LIST_csv_item_RAW, LIST_mongodb_item_COOKED, do_one_DATA_ITEM)




#################################################################
###### TEST OUTPUT 
#################################################################

def TEST_OUTPUT (output_option):

   # RAW data 
   folder_path = '../../data/raw/' 
   csv_path = ' ' 

   start_csv_index = 0 
   end_csv_index = 2
   
   start_data_list_index = 0
   end_data_list_index = 1

   LIST_csv_item_to_select = []
   csv_prefix = 'test_csv_'
   csv_extension= '.csv'
   LIST_csv_column = []


   LIST_csv_item_RAW = [folder_path, csv_path, start_csv_index, end_csv_index, LIST_csv_item_to_select, csv_prefix, csv_extension, LIST_csv_column, start_data_list_index, end_data_list_index]


   # COOKED data
   conn_str ="mongodb://localhost:27017/"
   db_name = "mydatabase"
   coll_select_mode = ''
   coll_name = "people"

   start_coll_index = 0
   end_coll_index = 0
   LIST_coll_item_to_select = []

   doc_select_mode = 'by_title'
   doc_key = 'doc_title'
   doc_id = ''
   doc_title = ''
   
   doc_index =0
   start_doc_index = 0
   end_doc_index = 1
   LIST_doc_item_to_select = ['shane', 'peter']

   LIST_mongodb_item_COOKED = [conn_str, db_name, coll_select_mode, coll_name,  start_coll_index, end_coll_index, LIST_coll_item_to_select, doc_select_mode, doc_key, doc_id, doc_title, doc_index, start_doc_index, end_doc_index, LIST_doc_item_to_select]

   doc_key_value_option = 'key'
   

   TFM_csv_to_mongodb (LIST_csv_item_RAW, LIST_mongodb_item_COOKED, do_one_DATA_ITEM, output_option)
         
   
 '''  
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
   
'''