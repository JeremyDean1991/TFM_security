

import sys
sys.path.append('../a0_plg_CUSTOM/') 
sys.path.append('../plg_TFM/') 
sys.path.append('../plg_DICT/') 

from plg_DICT_database import * 


from a0_items import * 
from plg_Files import * 
from plg_Folders import * 


##### Must download & install MongoDB software from --> https://www.mongodb.com/try/download/community #######
# https://www.w3schools.com/python/python_mongodb_getstarted.asp


##### plg_TFM_do_task_1 - MongoDB to MongoDB #########################################

### The following code is to be executed on the TFM server side, not from TFM master #######
############################################################################################
##### RAW, COOKED data lists #######


# get a list of raw COLLECTIONS from a MongoDB database 
def get_LIST_raw_ALL (raw_LOLISTS):

   LIST_raw_ALL = raw_LOLISTS 
   
   return LIST_raw_ALL 
   
''' 
raw_LOLISTS = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print (get_LIST_raw_ALL (raw_LOLISTS=raw_LOLISTS))
'''
  
# get selected lists by index
def get_LIST_raw_SELECTED (raw_LOLISTS, raw_start_on_index, raw_end_before_index):

   LIST_raw_ALL = get_LIST_raw_ALL (raw_LOLISTS=raw_LOLISTS)

   LIST_raw_selected = []
   
   for raw_list in LIST_raw_ALL[raw_start_on_index:raw_end_before_index]:
   
      LIST_raw_selected.append(raw_list)
           
   return LIST_raw_selected
   
'''   
raw_LOLISTS = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
start_on_index = 0
end_before_index =  3

print (get_LIST_raw_SELECTED (raw_LOLISTS=raw_LOLISTS, raw_start_on_index=start_on_index, raw_end_before_index=end_before_index) )  
'''     

def get_raw_DATA_ITEMS (raw_list):
  
   LIST_raw_data_item = raw_list
   
   return LIST_raw_data_item


  
def get_LIST_cooked_ALL (cooked_LOLISTS):

   LIST_cooked_ALL = cooked_LOLISTS
   
   return LIST_cooked_ALL 
      
''' 
cooked_LOLISTS = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print (get_LIST_cooked_ALL (cooked_LOLISTS=cooked_LOLISTS))
'''
  
   
# get selected collections by index
def get_LIST_cooked_SELECTED (cooked_LOLISTS, cooked_start_on_index, cooked_end_before_index):

   LIST_cooked_ALL = get_LIST_cooked_ALL (cooked_LOLISTS=cooked_LOLISTS)

   LIST_cooked_selected = []
   
   for cooked_list in LIST_cooked_ALL[cooked_start_on_index: cooked_end_before_index]:
   
      LIST_cooked_selected.append(cooked_list)
           
   return LIST_cooked_selected


'''
cooked_LOLISTS = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
start_on_index = 0
end_before_index =  3

print (get_LIST_cooked_SELECTED (cooked_LOLISTS=cooked_LOLISTS, cooked_start_on_index=start_on_index, cooked_end_before_index=end_before_index) ) 
'''

#### Select data with log status = Completed, In progress, Not completed within allowed task duration
def get_cooked_DATA_ITEMS (cooked_list):

   LIST_cooked_data_item = cooked_list
   
   return LIST_cooked_data_item


#get_cooked_DATA_ITEMS (cooked_list = '')




def get_TO_BE_DATA_ITEMS (raw_list, cooked_list):

   LIST_raw = get_raw_DATA_ITEMS (raw_list = raw_list)
   LIST_cooked = get_cooked_DATA_ITEMS (cooked_list = cooked_list)
   
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
# split data item to get data chunk   
def split_to_be_DATA_ITEMS (raw_list, cooked_list, start_index, items_per_list):
 
   LIST_to_be_DATA_ITEM = get_TO_BE_DATA_ITEMS (raw_list = raw_list, cooked_list = cooked_list)
   
   return list_SPLIT_1 (LIST_to_split = LIST_to_be_DATA_ITEM, start_index = start_index, items_per_list = items_per_list)
'''


# do the task on 1 data item, eg send email, post comment   
## this method needs to be created from scratch to be used by CF_data_chunk (LIST_item)
def do_one_DATA_ITEM (data_item):

   print (data_item) 
  
   

#####################################################################
##### Selected TO_BE data lists with TO_BE data items 

def get_LIST_to_be_SELECTED_with_data_item (raw_LOLISTS, raw_start_on_index, raw_end_before_index, cooked_LOLISTS, cooked_start_on_index, cooked_end_before_index):

   LIST_raw_list_SELECTED =  get_LIST_raw_SELECTED (raw_LOLISTS=raw_LOLISTS, raw_start_on_index=raw_start_on_index, raw_end_before_index=raw_end_before_index)
   LIST_cooked_list_SELECTED = get_LIST_cooked_SELECTED (cooked_LOLISTS=cooked_LOLISTS, cooked_start_on_index=cooked_start_on_index, cooked_end_before_index=cooked_end_before_index)
   
   #TO_BE lists & data 
   LOLISTS_to_be_data_SELECTED = []
   
   # get_TO_BE_DATA_ITEMS returns LOLISTS_to_be_data_SELECTED
   for raw_list, cooked_list in zip(LIST_raw_list_SELECTED, LIST_cooked_list_SELECTED):

      #LIST_to_be_list_data_SELECTED.append( raw_list + ' #_0 ' + get_TO_BE_DATA_ITEMS (raw_list = raw_LOLISTS + raw_list, cooked_list = cooked_LOLISTS + cooked_list) )
      LIST_TO_BE_item = get_TO_BE_DATA_ITEMS (raw_list=raw_list, cooked_list=cooked_list)
      LIST_TO_BE_item.insert(0, raw_list)
      
      LOLISTS_to_be_data_SELECTED.append(LIST_TO_BE_item)
      

   return LOLISTS_to_be_data_SELECTED
   
  
#get_LIST_to_be_SELECTED_with_data_items (raw_LOLISTS, raw_start_on_index, raw_end_before_index, cooked_LOLISTS, cooked_start_on_index, cooked_end_before_index)


###############################################################
###### Process data items by loop (LP)
##############################################################

# Process data item by loop
def LP_all_data_items (start_num, end_num):

   # LIST TO_BE file & data
   LOLISTS_raw_file_data = get_LIST_raw_selected_with_data_item (raw_folder_path=raw_folder_path, start_num=start_num, end_num=end_num)
   
   LIST_file_name_and_data = []
   
   # Loop through EACH selected to_be data file 
   for LIST_file_data in LOLISTS_raw_file_data[start_num: end_num]:
     
      data_file_only = LIST_file_data[0] # file name is always the first element 
      LIST_data_item_only = LIST_file_data[1:]
      
      #print (str(data_file_only).encode(), flush=True)
      #print (str(LIST_data_item_only).encode(), flush=True)
      
      for data_item in LIST_data_item_only:
      
         print (str(data_item).encode(), flush=True)
         
         ### do data item here 
         # do_one_DATA_ITEM_2 (data_item)



#################################################################
###### Process data items by concurrency futures (CF)
###################################################################

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




#do_task_DATA_ITEM --> need write this function to be used by CF_data_chunk (LIST_item)

raw_LOLISTS = ''
raw_list = ''
raw_start_list_index = ''
raw_end_list_index = ''

cooked_LOLISTS = ''
cooked_list = ''
cooked_start_list_index = ''
cooked_end_list_index = ''

start_index = ''
items_per_list = ''

do_one_DATA_ITEM = ''# this is a function to complete 1 data item 
LIST_item = ''


#CF_all_data_chunk (raw_LOLISTS, raw_list, raw_start_list_index, raw_end_list_index, cooked_LOLISTS, cooked_list, cooked_Start_list_index, cooked_end_list_index, start_index, items_per_list)