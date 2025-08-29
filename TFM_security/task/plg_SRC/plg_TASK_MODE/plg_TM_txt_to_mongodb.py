

import sys
sys.path.append('../plg_TFM/') 
sys.path.append('../plg_DICT/') 

from plg_DICT_database import * 

from plg_Regex import * 
from plg_Files import * 
from plg_Folders import * 
from plg_TXT import * 
from plg_Dict import * 

from plg_Concurrency_2 import *

import pymongo 
from pymongo import MongoClient
from pprint import pprint
import bson
from plg_DB_MongoDB_2 import * 


###############################################################
###### do one DATA ITEM - import do_one_DATA_ITEM function from a dedicated file 
##############################################################
from a0_TM_task_func import do_one_DATA_ITEM 

# may want to log task item after task completed 



##### Must download & install MongoDB software from --> https://www.mongodb.com/try/download/community #######
# https://www.w3schools.com/python/python_mongodb_getstarted.asp


### RAW
def get_LIST_ALL_RAW (LIST_file_item_RAW):

   # get keys from plg_Dict.py
   DICT_f_item_RAW                             = DICT_file_item (LIST_file_item=LIST_file_item_RAW)
   
   # Func arg values from Dict values       
   folder_path_RAW                            = DICT_f_item_RAW['folder_path']  
   file_extension_RAW                         = DICT_f_item_RAW['file_extension']


   LIST_ALL_RAW = get_ALL_in_folder (folder_path=folder_path_RAW)
   
   LIST_txt_RAW = []
   
   for file in LIST_ALL_RAW:
   
      if file_extension_RAW in file: # file extension must in .txt
      
         LIST_txt_RAW.append(file)
         
      else:
      
         pass
   
   return LIST_txt_RAW
   



# select file by file number (not by index)  
def get_LIST_SELECTED_RAW (LIST_file_item_RAW):

   # get values from plg_Dict.py
   DICT_f_item_RAW                             = DICT_file_item (LIST_file_item=LIST_file_item_RAW)
   
   # Func arg values from Dict values       
   folder_path_RAW                            = DICT_f_item_RAW['folder_path']  
   LIST_file_to_select_RAW                    = DICT_f_item_RAW['LIST_file_to_select'] # create file name list to select from 
   start_file_index_RAW                       = DICT_f_item_RAW['start_file_index'] 
   end_file_index_RAW                         = DICT_f_item_RAW['end_file_index']
   
   file_select_mode_RAW                           = DICT_f_item_RAW['file_select_mode'] 
  
   LIST_file_ALL_RAW = get_LIST_ALL_RAW (LIST_file_item_RAW = LIST_file_item_RAW)

   LIST_selected_RAW = []
   
   
   # select file by list item or by index?
   if file_select_mode_RAW == 'by_title': # item could be number or string   
      print ('select by list item')

      for file_RAW in LIST_file_to_select_RAW:
             
         if file_RAW in LIST_file_ALL_RAW:
      
            LIST_selected_RAW.append (file_RAW)
            #print ('raw file selected => ' + str(item), flush=True)
            
         
         else:
      
            #print ('raw file NOT selected => ' + str(item), flush=True)
            pass
            
   if file_select_mode_RAW == 'by_index':  
      print ('select by list index')
    
      for file in LIST_file_ALL_RAW [start_file_index_RAW:end_file_index_RAW]:
       
         LIST_selected_RAW.append (file)
           
   else:
     
     pass
      
          
   return LIST_selected_RAW 
   
   
 
 
# get data items of the selected files 
def get_data_items_RAW (LIST_file_item_RAW):

   # get values from plg_Dict.py
   DICT_f_item_RAW                             = DICT_file_item (LIST_file_item=LIST_file_item_RAW)
   
   # Func arg values from Dict values       
   folder_path_RAW                            = DICT_f_item_RAW['folder_path']  


   LIST_file_SELECTED =  get_LIST_SELECTED_RAW (LIST_file_item_RAW = LIST_file_item_RAW)
   
   LIST_file_data_items = []
   
   LOLISTS_file_data_item = [] # each list in this list is a file + data items
   
   
   for file in LIST_file_SELECTED:
   
      LIST_file_data_items = File_read_lines (file_path = folder_path_RAW + file) 
      
      LIST_file_data_items.insert(0, file)
     
      LOLISTS_file_data_item.append(LIST_file_data_items)
      
   
   return LOLISTS_file_data_item 
   
   
   
   
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
   
   
   # select file by list item or by index?
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




# get data items of the selected cooked files 
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





# TO_BE data items of the selected RAW & COOKED files 
# TO_BE is a single list NOT list of lists 
def get_data_items_TO_BE (LIST_file_item_RAW, LIST_mongodb_item_COOKED):

   LOLISTS_file_data_item_RAW = get_data_items_RAW (LIST_file_item_RAW = LIST_file_item_RAW)
   LOLISTS_doc_data_item_COOKED = get_data_items_COOKED (LIST_mongodb_item_COOKED = LIST_mongodb_item_COOKED)
   
   LIST_data_item_TO_BE = []
   

   for LIST_file_data_item_RAW in LOLISTS_file_data_item_RAW:
   
      for LIST_doc_data_item_COOKED in LOLISTS_doc_data_item_COOKED:
      
         for file_data_item_RAW in LIST_file_data_item_RAW:
         
            if file_data_item_RAW in LIST_doc_data_item_COOKED:
         
               #print (str(file_data_item_RAW) + ' in ' + str(LIST_doc_data_item_COOKED))
               pass

            else:
         
               print (str(file_data_item_RAW) + ' NOT in ' + str(LIST_doc_data_item_COOKED))
               
               LIST_data_item_TO_BE.append (file_data_item_RAW)
               
                              
   return LIST_data_item_TO_BE

       
###############################################################
###### Process data items by loop (LP)
##############################################################
  
def LP_data_item_ALL   (LIST_file_item_RAW, LIST_mongodb_item_COOKED):

   
   DICT_f_item_RAW   = DICT_file_item (LIST_file_item=LIST_file_item_RAW)
   
   start_data_list_index_RAW                       = DICT_f_item_RAW['start_data_list_index'] 
   end_data_list_index_RAW                         = DICT_f_item_RAW['end_data_list_index']
  
  
   LIST_data_item_TO_BE =  get_data_items_TO_BE (LIST_file_item_RAW, LIST_mongodb_item_COOKED)
   data_file_only = LIST_data_item_TO_BE[0]
   print ('data file only => ' + str(data_file_only))
   
   
   # Loop through EACH selected to_be data file 
   for data_item in LIST_data_item_TO_BE[start_data_list_index_RAW:end_data_list_index_RAW] :
          
      # do data item here 
      do_one_DATA_ITEM (data_item) 



#################################################################
###### Process data items by concurrency futures (CF)
###################################################################

def CF_data_chunk_ALL (LIST_file_item_RAW, LIST_mongodb_item_COOKED, LIST_concurrency_item_RAW):

   
   DICT_f_item_RAW   = DICT_file_item (LIST_file_item=LIST_file_item_RAW)   
   start_data_list_index_RAW                       = DICT_f_item_RAW['start_data_list_index'] 
   end_data_list_index_RAW                         = DICT_f_item_RAW['end_data_list_index']
   
   
   DICT_c_item_RAW   = DICT_concurrency_item (LIST_concurrency_item = LIST_concurrency_item_RAW)   
   LIST_data_item_split = DICT_c_item_RAW['LIST_data_item_split'] 
   start_index = DICT_c_item_RAW['start_index'] 
   items_per_list = DICT_c_item_RAW['items_per_list'] 
   pause_secs = DICT_c_item_RAW['pause_secs'] 
   
     
   LIST_data_item_TO_BE =  get_data_items_TO_BE (LIST_file_item_RAW, LIST_mongodb_item_COOKED) 
   data_file_only = LIST_data_item_TO_BE[0]
   print ('data file only => ' + str(data_file_only))


   CF_all_data_chunks (LIST_data_item_split=LIST_data_item_split, start_index=start_index, items_per_list=items_per_list, do_one_DATA_ITEM=do_one_DATA_ITEM(data_item), pause_secs=pause_secs )



def TM_txt_to_mongodb (LIST_file_item_RAW, LIST_mongodb_item_COOKED, LIST_concurrency_item_RAW, output_option):


   match output_option:

      case 'RAW_1':
         RAW_1 = get_LIST_ALL_RAW (LIST_file_item_RAW=LIST_file_item_RAW)
         print ('RAW_1 => ' + str(RAW_1))
         
      case 'RAW_2':       
         RAW_2 = get_LIST_SELECTED_RAW (LIST_file_item_RAW=LIST_file_item_RAW)
         print ('RAW_2 => ' + str(RAW_2))
         
      case 'RAW_3':
         RAW_3 = get_data_items_RAW (LIST_file_item_RAW)
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
         TO_BE_1 = get_data_items_TO_BE (LIST_file_item_RAW, LIST_mongodb_item_COOKED )
         print (' TO_BE_1 => ' + str(TO_BE_1))
       
   
      case 'LP':
         LP =  LP_data_item_ALL (LIST_file_item_RAW, LIST_mongodb_item_COOKED)
         print (' LP => ' + str(LP))
      
      case 'CF':
         CF = CF_data_chunk_ALL (LIST_file_item_RAW, LIST_mongodb_item_COOKED, LIST_concurrency_item_RAW)
         print (' CF => ' + str(CF))


#################################################################
###### TEST OUTPUT 
#################################################################

 ### 1 raw vs 1 cooked file OR 1 raw vs many cooked files??


def TEST_OUTPUT (output_option):
   
   # RAW data 
   folder_path = '../../data/raw/test_only/'
   file_path_RAW = '../../data/raw/test_only/people_1.txt'
   file_select_mode = 'by_index'
   start_file_index = 0
   end_file_index = 1
   
   start_data_list_index = 1
   end_data_list_index = None

   # LIST_raw_file_num_to_select = get_file_num(full_file_path, file_prefix, file_extension)  
   LIST_file_to_select = ['people_1.txt','people_3.txt'] # list of file names to select
   file_prefix= 'people_'
   file_extension = '.txt'
   
   line_start_num = ''
   line_end_num = ''
   
   start_data_list_index = 1
   end_data_list_index = None

   LIST_file_item_RAW = [folder_path, file_path_RAW, file_select_mode, start_file_index, end_file_index, LIST_file_to_select, file_prefix, file_extension, line_start_num, line_end_num, start_data_list_index, end_data_list_index]


   # COOKED data
   conn_str ="mongodb://localhost:27017/"
   db_name = "mydatabase"
   coll_select_mode = ''
   coll_name = "people"

   start_coll_index = 0
   end_coll_index = 0
   LIST_coll_to_select = [] # list of coll titles to select

   doc_select_mode = 'by_index'
   doc_key = 'doc_title'
   doc_id = ''
   doc_title = ''
   
   doc_index =0
   start_doc_index = 0
   end_doc_index = 1
   LIST_doc_to_select = ['shane'] # list of doc titles to select
   
   doc_key_value_option = 'key'
   start_data_list_index = ''
   end_data_list_index = ''

   LIST_mongodb_item_COOKED = [conn_str, db_name, coll_select_mode, coll_name, start_coll_index, end_coll_index, LIST_coll_to_select, doc_select_mode, doc_key, doc_id, doc_title, doc_index, start_doc_index, end_doc_index, LIST_doc_to_select, doc_key_value_option, start_data_list_index, end_data_list_index]
   
   
   # Concurrency futures  
   LIST_data_item_split = get_data_items_TO_BE (LIST_file_item_RAW, LIST_mongodb_item_COOKED)
   start_index = 0
   items_per_list =2 
   do_one_DATA_ITEM = ''
   pause_secs = 2
    
   LIST_concurrency_item_RAW = [LIST_data_item_split, start_index, items_per_list, do_one_DATA_ITEM, pause_secs]
   
   # TASK MODE txt to mongodb
   TM_txt_to_mongodb (LIST_file_item_RAW, LIST_mongodb_item_COOKED, LIST_concurrency_item_RAW, output_option)
         
   
   
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