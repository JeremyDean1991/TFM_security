

import sys
sys.path.append('../plg_TFM/') 
sys.path.append('../plg_DICT/') 

from plg_DICT_database import * 

from plg_docs import * 
from plg_Folders import * 
from plg_Dict import * 

from plg_Concurrency_2 import *

import pymongo 
from pymongo import MongoClient
from pprint import pprint
import bson
from plg_DB_MongoDB_2 import * 



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

   LIST_selected_DOC_RAW = []
   
   
   # select doc by list item or by index?
   if doc_select_mode_RAW == 'by_title': # item could be number or string 
      print ('select by list item')

      for doc_1 in LIST_doc_to_select_RAW:
          
         for doc_2 in LIST_ALL_doc_RAW:
         
            doc_str = str(doc_2)
         
            if doc_1 in doc_str:
      
               LIST_selected_DOC_RAW.append (doc_1)
               print (str(doc_1) + ' => in doc => ' + str(doc_2), flush=True)
         
            else:
      
               print (str(doc_1) + ' => NOT in doc => ' + str(doc_2), flush=True)
               pass
   
     
   if doc_select_mode_RAW == 'by_index':
      print ('select by list index')
   
      for RAW_doc in LIST_ALL_doc_RAW[start_doc_index_RAW : end_doc_index_RAW ]:
   
         LIST_selected_DOC_RAW.append(RAW_doc)
                 
   else:
   
      pass
           
  
   return LIST_selected_DOC_RAW



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
   
   
   # select doc by list item or by index?
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



# get data items of the selected cooked docs 
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



# TO_BE data items of the selected RAW & COOKED docs 
# TO_BE is a single list NOT list of lists 
def get_data_items_TO_BE (LIST_mongodb_item_RAW, LIST_mongodb_item_COOKED):

   LOLISTS_doc_data_item_RAW = get_data_items_RAW (LIST_mongodb_item_RAW = LIST_mongodb_item_RAW)
   LOLISTS_doc_data_item_COOKED = get_data_items_COOKED (LIST_mongodb_item_COOKED = LIST_mongodb_item_COOKED)
   
   LIST_data_item_TO_BE = []
   

   for LIST_doc_data_item_RAW in LOLISTS_doc_data_item_RAW:
   
      for LIST_doc_data_item_COOKED in LOLISTS_doc_data_item_COOKED:
      
         for doc_data_item_RAW in LIST_doc_data_item_RAW:
         
            if doc_data_item_RAW in LIST_doc_data_item_COOKED:
         
               #print (str(doc_data_item_RAW) + ' in ' + str(LIST_doc_data_item_COOKED))
               pass

            else:
         
               print (str(doc_data_item_RAW) + ' NOT in ' + str(LIST_doc_data_item_COOKED))
               
               LIST_data_item_TO_BE.append (doc_data_item_RAW)
               
                              
   return LIST_data_item_TO_BE

       
       
###############################################################
###### Process data items by loop (LP)
##############################################################
  
def LP_data_item_ALL   (LIST_mongodb_item_RAW, LIST_mongodb_item_COOKED):

   
   DICT_f_item_RAW   = DICT_doc_item (LIST_doc_item=LIST_mongodb_item_RAW)
   
   start_data_list_index_RAW                       = DICT_f_item_RAW['start_data_list_index'] 
   end_data_list_index_RAW                         = DICT_f_item_RAW['end_data_list_index']
  
  
   LIST_data_item_TO_BE =  get_data_items_TO_BE (LIST_mongodb_item_RAW, LIST_mongodb_item_COOKED)
   data_doc_only = LIST_data_item_TO_BE[0]
   print ('data doc only => ' + str(data_doc_only))
   
   
   # Loop through EACH selected to_be data doc 
   for data_item in LIST_data_item_TO_BE[start_data_list_index_RAW:end_data_list_index_RAW] :
          
      # do data item here 
      do_one_DATA_ITEM (data_item) 



#################################################################
###### Process data items by concurrency futures (CF)
###################################################################

def CF_data_chunk_ALL (LIST_mongodb_item_RAW, LIST_mongodb_item_COOKED, LIST_concurrency_item_RAW):

   
   DICT_f_item_RAW   = DICT_doc_item (LIST_doc_item=LIST_mongodb_item_RAW)   
   start_data_list_index_RAW                       = DICT_f_item_RAW['start_data_list_index'] 
   end_data_list_index_RAW                         = DICT_f_item_RAW['end_data_list_index']
   
   
   DICT_c_item_RAW   = DICT_concurrency_item (LIST_concurrency_item = LIST_concurrency_item_RAW)   
   LIST_data_item_split = DICT_c_item_RAW['LIST_data_item_split'] 
   start_index = DICT_c_item_RAW['start_index'] 
   items_per_list = DICT_c_item_RAW['items_per_list'] 
   pause_secs = DICT_c_item_RAW['pause_secs'] 
   
     
   LIST_data_item_TO_BE =  get_data_items_TO_BE (LIST_mongodb_item_RAW, LIST_mongodb_item_COOKED) 
   data_doc_only = LIST_data_item_TO_BE[0]
   print ('data doc only => ' + str(data_doc_only))


   CF_all_data_chunks (LIST_data_item_split=LIST_data_item_split, start_index=start_index, items_per_list=items_per_list, do_one_DATA_ITEM=do_one_DATA_ITEM, pause_secs=pause_secs )



def TM_mongodb_to_mongodb (LIST_mongodb_item_RAW, LIST_mongodb_item_COOKED, LIST_concurrency_item_RAW, output_option):


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
         COOKED_1 = get_LIST_ALL_COOKED (LIST_mongodb_item_COOKED)
         print ('COOKED_1 => ' + str(COOKED_1))
         
      case 'COOKED_2':
         COOKED_2 = get_LIST_SELECTED_COOKED (LIST_mongodb_item_COOKED)
         print (' COOKED_2 => ' + str(COOKED_2))
         
      case 'COOKED_3':      
         COOKED_3 = get_data_items_COOKED (LIST_mongodb_item_COOKED)
         print ('COOKED_3 => ' + str(COOKED_3))

      case 'TO_BE_1':
         TO_BE_1 = get_data_items_TO_BE (LIST_mongodb_item_RAW, LIST_mongodb_item_COOKED )
         print (' TO_BE_1 => ' + str(TO_BE_1))
       
   
      case 'LP':
         LP =  LP_data_item_ALL (LIST_mongodb_item_RAW, LIST_mongodb_item_COOKED)
         print (' LP => ' + str(LP))
      
      case 'CF':
         CF = CF_data_chunk_ALL (LIST_mongodb_item_RAW, LIST_mongodb_item_COOKED, LIST_concurrency_item_RAW)
         print (' CF => ' + str(CF))


#################################################################
###### TEST OUTPUT 
#################################################################

 ### 1 raw vs 1 cooked doc OR 1 raw vs many cooked docs??


def TEST_OUTPUT (output_option):
   
   # RAW data 
   conn_str_R ="mongodb://localhost:27017/"
   db_name_R = "mydatabase"
   coll_select_mode_R = ''
   coll_name_R = "people"

   start_coll_index_R = 0
   end_coll_index_R = 0
   LIST_coll_to_select_R = [] # list of coll titles to select

   doc_select_mode_R = 'by_index'
   doc_key_R = 'doc_title'
   doc_id_R = ''
   doc_title_R = ''
   
   doc_index_R =0
   start_doc_index_R = 0
   end_doc_index_R = 1
   LIST_doc_to_select_R = ['shane'] # list of doc titles to select
   
   doc_key_value_option_R = 'key'
   start_data_list_index_R = ''
   end_data_list_index_R = ''

   LIST_mongodb_item_RAW = [conn_str_R, db_name_R, coll_select_mode_R, coll_name_R, start_coll_index_R, end_coll_index_R, LIST_coll_to_select_R, doc_select_mode_R, doc_key_R, doc_id_R, doc_title_R, doc_index_R, start_doc_index_R, end_doc_index_R, LIST_doc_to_select_R, doc_key_value_option_R, start_data_list_index_R, end_data_list_index_R]
      
   

   # COOKED data
   conn_str_C ="mongodb://localhost:27017/"
   db_name_C = "mydatabase"
   coll_select_mode_C = ''
   coll_name_C = "people"

   start_coll_index_C = 0
   end_coll_index_C = 0
   LIST_coll_to_select_C = [] # list of coll titles to select

   doc_select_mode_C = 'by_index'
   doc_key_C = 'doc_title'
   doc_id_C = ''
   doc_title_C = ''
   
   doc_index_C =0
   start_doc_index_C = 0
   end_doc_index_C = 1
   LIST_doc_to_select_C = ['shane'] # list of doc titles to select
   
   doc_key_value_option_C = 'key'
   start_data_list_index_C = ''
   end_data_list_index_C = ''

   LIST_mongodb_item_COOKED = [conn_str_C, db_name_C, coll_select_mode_C, coll_name_C, start_coll_index_C, end_coll_index_C, LIST_coll_to_select_C, doc_select_mode_C, doc_key_C, doc_id_C, doc_title_C, doc_index_C, start_doc_index_C, end_doc_index_C, LIST_doc_to_select_C, doc_key_value_option_C, start_data_list_index_C, end_data_list_index_C]
   
   
   # Concurrency futures  
   LIST_data_item_split = get_data_items_TO_BE (LIST_mongodb_item_RAW, LIST_mongodb_item_COOKED)
   start_index = 0
   items_per_list =2 
   do_one_DATA_ITEM = ''
   pause_secs = 2
    
   LIST_concurrency_item_RAW = [LIST_data_item_split, start_index, items_per_list, do_one_DATA_ITEM, pause_secs]
   
   # TASK MODE txt to mongodb
   TM_txt_to_mongodb (LIST_mongodb_item_RAW, LIST_mongodb_item_COOKED, LIST_concurrency_item_RAW, output_option)
         
   
   
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









