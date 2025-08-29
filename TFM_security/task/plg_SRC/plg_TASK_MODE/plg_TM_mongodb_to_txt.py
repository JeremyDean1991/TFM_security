

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


##### Must download & install MongoDB software from --> https://www.mongodb.com/try/download/community #######
# https://www.w3schools.com/python/python_mongodb_getstarted.asp



### RAW data items 
# get ALL DOCS in a collection   
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
   
   
   # select file by list item or by index?
   if doc_select_mode_COOKED == 'by_query': # item could be number or string 
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
   
     
   if doc_select_mode_COOKED == 'by_index':
      print ('select by list index')
   
      for RAW_doc in LIST_ALL_doc_RAW[start_doc_index_RAW : end_doc_index_RAW ]:
   
         LIST_selected_DOC_RAW.append(RAW_doc)
                 
   else:
   
      pass
           
  
   return LIST_selected_DOC_RAW



# get lines of ONE of the selected docs
def get_DATA_ITEMS_RAW (LIST_mongodb_item_RAW ):

   DICT_m_item_RAW = DICT_mongodb_item (LIST_mongodb_item=LIST_mongodb_item_RAW)
   
   conn_str_RAW = DICT_m_item_RAW ['conn_str']
   db_name_RAW = DICT_m_item_RAW ['db_name']
   coll_name_RAW = DICT_m_item_RAW ['coll_name'] 
   
   doc_index_RAW = DICT_m_item_RAW ['doc_index']
   doc_key_RAW = DICT_m_item_RAW ['doc_key']
   doc_key_value_option_RAW = DICT_m_item_RAW ['doc_key_value_option']   
  

   LIST_selected_doc = get_LIST_SELECTED_RAW (LIST_mongodb_item_RAW=LIST_mongodb_item_RAW)
   
   # get all values of a specific doc 
   LIST_doc_item_RAW_1 = LIST_selected_doc[doc_index_RAW].items()
       
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
def get_LIST_ALL_COOKED (LIST_file_item_COOKED):

   # get keys from plg_Dict.py
   DICT_f_item_COOKED                             = DICT_file_item (LIST_file_item=LIST_file_item_COOKED)
   
   # Func arg values from Dict values       
   folder_path_COOKED                            = DICT_f_item_COOKED['folder_path']  
   file_extension_COOKED                         = DICT_f_item_COOKED['file_extension']

   # LIST_file_item_COOKED = [folder_path_COOKED, file_path_COOKED, file_select_mode, start_file_index, end_file_index, LIST_file_item_to_select, file_prefix, file_extension_COOKED]
   #folder_path_COOKED = LIST_file_item_COOKED[0]
   #file_extension_COOKED = LIST_file_item_COOKED[7]

   LIST_ALL_COOKED = get_ALL_in_folder (folder_path=folder_path_COOKED)
   
   LIST_txt_COOKED = []
   
   for file in LIST_ALL_COOKED:
   
      if file_extension_COOKED in file:
      
         LIST_txt_COOKED.append(file)
         
      else:
      
         pass
   
   return LIST_txt_COOKED
   


  
# select file by file number (not by index)  
def get_LIST_SELECTED_COOKED (LIST_file_item_COOKED):

   # get values from plg_Dict.py
   DICT_f_item_COOKED                             = DICT_file_item (LIST_file_item=LIST_file_item_COOKED)
   
   # Func arg values from Dict values       
   folder_path_COOKED                            = DICT_f_item_COOKED['folder_path']  
   LIST_file_to_select_COOKED                    = DICT_f_item_COOKED['LIST_file_to_select'] 
   start_file_index_COOKED                       = DICT_f_item_COOKED['start_file_index'] 
   end_file_index_COOKED                         = DICT_f_item_COOKED['end_file_index']
   
   file_select_mode_COOKED                           = DICT_f_item_COOKED['file_select_mode'] 
  
   LIST_file_ALL_COOKED = get_LIST_ALL_COOKED (LIST_file_item_COOKED = LIST_file_item_COOKED)

   LIST_selected_COOKED = []
   
   
   # select file by list item or by index?
   if file_select_mode_COOKED == 'by_query': # item could be number or string   
      print ('select by list item')

      for file_COOKED in LIST_file_to_select_COOKED:
             
         if file_COOKED in LIST_file_ALL_COOKED:
      
            LIST_selected_COOKED.append (file_COOKED)
            #print ('COOKED file selected => ' + str(item), flush=True)
            
         
         else:
      
            #print ('COOKED file NOT selected => ' + str(item), flush=True)
            pass
            
   if file_select_mode_COOKED == 'by_index':  
      print ('select by list index')
    
      for file in LIST_file_ALL_COOKED [start_file_index_COOKED:end_file_index_COOKED]:
       
         LIST_selected_COOKED.append (file)
           
   else:
     
     pass
      
          
   return LIST_selected_COOKED 
   
   
 

 

# get data items of a specific file   
def get_data_items_COOKED (LIST_file_item_COOKED):

   # get values from plg_Dict.py
   DICT_f_item_COOKED                             = DICT_file_item (LIST_file_item=LIST_file_item_COOKED)
   
   # Func arg values from Dict values       
   file_path_COOKED                            = DICT_f_item_COOKED['file_path']  
   
   LIST_data_item_COOKED = File_read_lines (file_path = file_path_COOKED)   
   #print (LIST_data_item_COOKED, flush=True)
   
   return LIST_data_item_COOKED
  
  




### TO_BE data items 
def get_TO_BE_DOCS (raw_conn_str, raw_coll, cooked_coll, raw_doc_key, cooked_doc_key, cooked_file_path):

   LIST_raw_doc = get_raw_DOCS (raw_conn_str=raw_conn_str, raw_db_name=raw_db_name, raw_coll = raw_coll)
   LIST_cooked_data_tiem = get_cooked_DATA_ITEMS (cooked_file_path = cooked_file_path)
   
   LIST_to_be_doc = []
   
   #need to match raw & cooked docs by using doc key = doc title 
        
   for raw_doc in LIST_raw_doc:
    
      for cooked_data_item in LIST_cooked_data_item:
      
         raw_data=raw_doc[raw_doc_key]
       
         if raw_data in cooked_data:
          
            print (raw_data + ' in ' + cooked_data)
            
         else:
         
            print (raw_data + ' NOT in ' + cooked_data)
            LIST_to_be_doc.append(raw_doc)
   
   #print ('LIST to be documents => ' + str(LIST_test_to_be_doc))   
   return LIST_to_be_doc 
   
   
   
# each doc is a list item of a list, split list into separate lists
def split_to_be_DOCS (raw_conn_str, raw_db_name, raw_coll, raw_doc_key, cooked_folder_path,cooked_file_path start_index, docs_per_list):
 
   LIST_to_be_DOC = get_TO_BE_DOCS (raw_conn_str=raw_conn_str, raw_coll=raw_coll, raw_doc_key=raw_doc_key, cooked_file_path)
   
   
   return list_SPLIT_1 (LIST_to_split = LIST_to_be_DOC, start_index = start_index, docs_per_list = docs_per_list)


'''
# do the task on 1 data item, eg send email, post comment   
## this method needs to be created from scratch to be used by CF_data_chunk (LIST_item)
def do_one_DOC (doc):

   #To insert or update docs here
   print (doc)   
'''   
   

#####################################################################
##### Selected TO_BE collections with TO_BE documents

def get_LIST_to_be_SELECTED_with_doc(LIST_mongodb_item_RAW, LIST_file_item_COOKED):

   LIST_raw_coll_SELECTED =  get_LIST_selected_RAW (conn_str = raw_conn_str, raw_start_coll_index = raw_start_coll_index, raw_end_coll_index = raw_end_coll_index)
   LIST_cooked_coll_SELECTED = get_LIST_cooked_SELECTED (cooked_folder_path=cooked_folder_path, cooked_start_file_index=cooked_start_file_index, cooked_end_file_index=cooked_end_file_index)
   
   #TO_BE lists & data 
   LOLISTS_to_be_data_SELECTED = []
   
   # get_TO_BE_DATA_ITEMS returns LOLISTS_to_be_data_SELECTED
   for raw_list, cooked_list in zip(LIST_raw_list_SELECTED, LIST_cooked_list_SELECTED):

      #LIST_to_be_list_data_SELECTED.append( raw_list + ' #_0 ' + get_TO_BE_DATA_ITEMS (raw_list = raw_LOLISTS + raw_list, cooked_list = cooked_LOLISTS + cooked_list) )
      LIST_TO_BE_item = get_TO_BE_DATA_ITEMS (raw_list=raw_list, cooked_list=cooked_list)
      LIST_TO_BE_item.insert(0, raw_list)
      
      LOLISTS_to_be_data_SELECTED.append(LIST_TO_BE_item)
      

   return LOLISTS_to_be_data_SELECTED


#get_LIST_to_be_SELECTED_with_doc (raw_conn_str, start_collection, end_collection, raw_db_name, cooked_db_name )



###############################################################
###### Process data items by loop (LP)
##############################################################
  
# Process data item by loop
def LP_all_data_items ():

   # LIST TO_BE file & data
   LIST_raw_file_data = get_LIST_selected_RAW_with_data_item (raw_folder_path=raw_folder_path, start_num=start_num, end_num=end_num)
   
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

def CF_doc_chunk (LIST_doc):

   with concurrent.futures.ProcessPoolExecutor() as executor:
        
      executor.map(do_one_DOC, LIST_doc=LIST_doc)
        
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



def TM_mongodb_to_txt (LIST_mongodb_RAW, LIST_file_item_COOKED, do_one_DATA_ITEM, output_option):


   match output_option:

      case 'RAW_1':
         RAW_1 = get_LIST_ALL_RAW (LIST_mongodb_item_RAW)
         print (RAW_1)
         
      case 'RAW_2':       
         RAW_2 = get_LIST_SELECTED_RAW (LIST_mongodb_item_RAW)
         print (RAW_2)
         
      case 'RAW_3':
         RAW_3 = get_data_items_RAW (LIST_mongodb_item_RAW)
         print (RAW_3)

      case 'COOKED_1':
         COOKED_1 = get_LIST_ALL_COOKED (LIST_file_item_COOKED)
         print (COOKED_1)
         
      case 'COOKED_2':
         COOKED_2 = get_LIST_SELECTED_COOKED (LIST_file_item_COOKED)
         print (COOKED_2)
         
      case 'COOKED_3':      
         COOKED_3 = get_DATA_ITEMS_COOKED (LIST_file_item_COOKED)
         print (COOKED_3)

      case 'TO_BE_1':
         TO_BE_1 = get_TO_BE_DATA_ITEMS (LIST_mongodb_RAW, LIST_file_item_COOKED )
         print (TO_BE_1)
         
      case 'TO_BE_2':
         TO_BE_2 = get_LIST_to_be_SELECTED_with_data_items (LIST_mongodb_RAW, LIST_file_item_COOKED  )
         print (TO_BE_2)
   
      case 'LP':
         LP =  LP_all_data_items (LIST_mongodb_RAW, LIST_file_item_COOKED, do_one_DATA_ITEM)
         print (LP)
      
      case 'CF':
         CF = CF_all_data_chunk (LIST_mongodb_RAW, LIST_file_item_COOKED, do_one_DATA_ITEM)




#do_task_DOC --> need write this function to be used by CF_data_chunk (LIST_item)

raw_conn_str = ''
raw_db_name = ''
raw_coll = ''
raw_doc_key = ''
raw_start_coll_index = ''
raw_end_coll_index = ''

cooked_folder_path
cooked_file_path
cooked_start_file_index
cooked_end_file_index

start_index = ''
doc_per_list = ''

do_one_DOC = ''# this is a function to complete 1 data item 
LIST_doc = ''


#CF_all_doc_chunk (raw_conn_str, raw_db_name, raw_coll, raw_start_coll_index, raw_end_coll_index, raw_doc_key, cooked_folder_path, cooked_file_path, start_index, docs_per_list)