

import sys
sys.path.append('../plg_TFM/') 
sys.path.append('../plg_DICT/') 

from plg_DICT_database import * 

from a0_items import * 
from plg_Regex import * 
from plg_Files import * 
from plg_Folders import * 
from plg_TXT import * 
from plg_list_SPLIT import * 

from plg_Concurrency_2 import *


# number list for testing
def create_LIST_file_num (num):

   LIST_file_num = []

   for i in range (num):
   
      LIST_file_num.append(i)
      
   return LIST_file_num 

'''
num = 3
print (create_LIST_file_num (num), flush=True)
'''


def get_file_num(full_file_path, file_prefix, file_extension):

   file_num = remove_all_before_and_after_texts (before_text=file_prefix, after_text=file_extension, text_main=full_file_path)
   INT_file_num = int(file_num)
   
   return INT_file_num
   

'''
full_file_path = '../../data/raw/a0_TEST_file_num/a_1.txt'
file_prefix = 'a_'
file_extension = '.txt'

file_num = get_file_num(full_file_path, file_prefix, file_extension)   
print (file_num, flush=True)
'''



### RAW
def get_LIST_ALL_RAW (LIST_file_item_RAW):

   # get keys from plg_Dict.py
   DICT_f_item_RAW                             = DICT_file_item (LIST_file_item=LIST_file_item_RAW)
   
   # Func arg values from Dict values       
   folder_path_RAW                            = DICT_f_item_RAW['folder_path']  
   file_extension_RAW                         = DICT_f_item_RAW['file_extension']

   # LIST_file_item_RAW = [folder_path_RAW, file_path_RAW, file_select_mode, start_file_index, end_file_index, LIST_file_item_to_select, file_prefix, file_extension_RAW]
   #folder_path_RAW = LIST_file_item_RAW[0]
   #file_extension_RAW = LIST_file_item_RAW[7]

   LIST_ALL_RAW = get_ALL_in_folder (folder_path=folder_path_RAW)
   
   LIST_txt_RAW = []
   
   for file in LIST_ALL_RAW:
   
      if file_extension_RAW in file:
      
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
   LIST_file_item_to_select_RAW               = DICT_f_item_RAW['LIST_file_item_to_select'] 
   start_file_index_RAW                       = DICT_f_item_RAW['start_file_index'] 
   end_file_index_RAW                         = DICT_f_item_RAW['end_file_index']
   
   file_select_mode_RAW                           = DICT_f_item_RAW['file_select_mode'] 
  
   LIST_file_ALL_RAW = get_LIST_ALL_RAW (LIST_file_item_RAW = LIST_file_item_RAW)

   LIST_selected_RAW = []
   
   
   # select file by list item or by index?
   if file_select_mode_RAW == 'by_item': # item could be number or string 
   
      print ('select by list item')

      for item in LIST_file_item_to_select_RAW:
             
         if item in LIST_file_ALL_RAW:
      
            LIST_selected_RAW.append (item)
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
   
   

# get data items of a specific file   
def get_data_items_RAW (file_path_RAW):

   # do NOT get keys from plg_DICT, the program could get confused. 
   
   LIST_data_item_RAW = File_read_lines (file_path = file_path_RAW)   
   #print (LIST_data_item_RAW, flush=True)
   
   return LIST_data_item_RAW



### COOKED data items  
def get_LIST_ALL_COOKED (LIST_file_item_COOKED):

   # get keys from plg_Dict.py
   DICT_f_item_COOKED                             = DICT_file_item (LIST_file_item=LIST_file_item_COOKED)
   
   # Func arg values from Dict values       
   folder_path_COOKED                            = DICT_f_item_COOKED['folder_path']  
   file_extension_COOKED                         = DICT_f_item_COOKED['file_extension']

   LIST_ALL_COOKED = get_ALL_in_folder (folder_path=folder_path_COOKED)
   
   LIST_txt_COOKED = []
   
   for file in LIST_ALL_COOKED:
   
      if file_extension_COOKED in file:
      
         LIST_txt_COOKED.append(file)
         
      else:
      
         pass
   
   return LIST_txt_COOKED



# should only select 1, but may select many 
def get_LIST_SELECTED_COOKED (LIST_file_item_COOKED):

   # get values from plg_Dict.py
   DICT_f_item_COOKED                            = DICT_file_item (LIST_file_item=LIST_file_item_COOKED)
   
   # Func arg values from Dict values       
   folder_path_COOKED                            = DICT_f_item_COOKED['folder_path']  
   LIST_file_item_to_select_COOKED              = DICT_f_item_COOKED['LIST_file_item_to_select'] 
   start_file_index_COOKED                       = DICT_f_item_COOKED['start_file_index'] 
   end_file_index_COOKED                         = DICT_f_item_COOKED['end_file_index']
   
   file_select_mode_COOKED                           = DICT_f_item_COOKED['file_select_mode'] 
  
   LIST_file_ALL_COOKED = get_LIST_ALL_COOKED (LIST_file_item_COOKED = LIST_file_item_COOKED)

   LIST_selected_COOKED = []
   
   
   # select file by list item or by index?
   if file_select_mode_COOKED == 'by_item': # item could be number or string 
   
      print ('select by list item')

      for item in LIST_file_item_to_select_COOKED:
             
         if item in LIST_file_ALL_COOKED:
      
            LIST_selected_COOKED.append (item)
            #print ('raw file selected => ' + str(item), flush=True)
            
         
         else:
      
            #print ('raw file NOT selected => ' + str(item), flush=True)
            pass
            
   if file_select_mode_COOKED == 'by_index':
   
      print ('select by list index')
    
      for file in LIST_file_ALL_COOKED [start_file_index_COOKED:end_file_index_COOKED]:
       
         LIST_selected_COOKED.append (file)
           
   else:
     
     pass
      
          
   return LIST_selected_COOKED 
   
   

#### Select data with log status = Completed, In progress, Not completed within allowed task duration
# get data items of a specific file   
def get_data_items_COOKED (file_path_COOKED):

   # do NOT get keys from plg_DICT, the program could get confused. 
   
   LIST_data_item_COOKED = File_read_lines (file_path = file_path_COOKED)
   
   return LIST_data_item_COOKED


'''
file_path_COOKED = '../../data/cooked/people_1a.txt'
               
print (get_data_items_COOKED (file_path_COOKED= file_path_COOKED, flush=True)   
'''



### TO_BE
def get_TO_BE_DATA_ITEMS (file_path_RAW, file_path_COOKED):
   
   # do NOT use plg_DICT here, not to confuse the program 
   
   LIST_item_RAW = get_data_items_RAW (file_path_RAW= file_path_RAW)
   LIST_item_COOKED = get_data_items_COOKED (file_path_COOKED =  file_path_COOKED)
   
   
   LIST_item_TO_BE = []
       
   for item_RAW in LIST_item_RAW:
      #print (item_RAW)
    
      if item_RAW in LIST_item_COOKED:
       
         #rint (item_RAW + ' in cooked')
         pass
          
      else:
          
         #print (item_RAW + ' NOT in cooked')
         LIST_item_TO_BE.append(item_RAW)
   
   #print ('LIST to be => ' + str(LIST_test_to_be))   
   return LIST_item_TO_BE 
   
 
'''
file_path_R = '../../data/raw/people_1.txt'
file_path_C = '../../data/cooked/people_1a.txt'


TO_BE_data123 = get_TO_BE_DATA_ITEMS (file_path_RAW = file_path_R, file_path_COOKED = file_path_C)

#print (TO_BE_data123, flush=True)
'''
 
 
############################################################################################################# 
#### NOTE: this function for testing only must use --> get_LIST_to_be_SELECTED_with_data_items_2 () ###
#############################################################################################################


# do the task on 1 data item, eg send email, post comment   
## this method needs to be created from scratch to be used by CF_data_chunk (LIST_item)
def do_one_DATA_ITEM (data_item):

   print (" HI, FROM do_one_DATA_ITEM => " + str(data_item), flush=True)
   


   
#####################################################################
##### Selected TO_BE data files with TO_BE data items 
######################################################################

def get_LIST_to_be_SELECTED_with_data_items (LIST_file_item_RAW, LIST_file_item_COOKED):

   # get values from plg_Dict.py
   DICT_f_item_RAW                            = DICT_file_item (LIST_file_item=LIST_file_item_RAW)
   DICT_f_item_COOKED                         = DICT_file_item (LIST_file_item=LIST_file_item_COOKED)

   folder_path_RAW                                = DICT_f_item_RAW['folder_path']  
   folder_path_COOKED                            = DICT_f_item_COOKED['folder_path']  


   LIST_raw_file_SELECTED =  get_LIST_SELECTED_RAW (LIST_file_item_RAW=LIST_file_item_RAW)
   LIST_cooked_file_SELECTED = get_LIST_SELECTED_COOKED (LIST_file_item_COOKED=LIST_file_item_COOKED)
   
   #TO_BE files & data 
   LIST_to_be_file_data_SELECTED = []
   
   # get_TO_BE_DATA_ITEMS resturns a list of TO_BE data 
   for raw_file, cooked_file in zip(LIST_raw_file_SELECTED, LIST_cooked_file_SELECTED):
        
      LIST_TO_BE_item = get_TO_BE_DATA_ITEMS(file_path_RAW = folder_path_RAW + raw_file, file_path_COOKED =  folder_path_COOKED + cooked_file)
      #print (str(TO_BE_item).encode(), flush=True)

      # file name is always the first element 
      LIST_TO_BE_item.insert (0, raw_file)
      LIST_to_be_file_data_SELECTED.append(LIST_TO_BE_item)

   return LIST_to_be_file_data_SELECTED


       

###############################################################
###### Process data items by loop (LP)
##############################################################

def LP_all_data_items (LIST_file_item_RAW, LIST_file_item_COOKED, start_num, end_num):

   LOLISTS_to_be_file_data = get_LIST_to_be_SELECTED_with_data_items (LIST_file_item_RAW=LIST_file_item_RAW, LIST_file_item_COOKED=LIST_file_item_COOKED)

   for LIST_file_data in LOLISTS_to_be_file_data[start_num: end_num]:   
      #print (str(LIST_file_data).encode(), flush=True) 

      for file_data in LIST_file_data:
         #print (str(file_data).encode(), flush=True) 
         
         # do data item task here             
         do_one_DATA_ITEM (data_item=file_data)



#################################################################
###### Process data items by concurrency futures (CF)
###################################################################

# Concurrent using list of list
def CF_all_data_chunk (LIST_file_item_RAW, LIST_file_item_COOKED, start_list_index, end_list_index):
  
   # LIST TO_BE list & data
   LOLISTS_to_be_file_data = get_LIST_to_be_SELECTED_with_data_items (LIST_file_item_RAW=LIST_file_item_RAW, LIST_file_item_COOKED=LIST_file_item_COOKED)
   
   # Loop through EACH selected to_be data list 
   for LIST_data_item in LOLISTS_to_be_file_data[start_list_index:end_list_index]:

      LIST_data_file_only = LIST_data_item[0] # file name is always the first element 
      LIST_data_item_only = LIST_data_item[1:]
              
      CF_one_data_chunk (do_one_DATA_ITEM=do_one_DATA_ITEM, LIST_data_item=LIST_data_item_only )
     


def TM_txt_to_txt (LIST_file_item_RAW, LIST_file_item_COOKED, start_list_index, end_list_index, output_option):

   match output_option:

      case 'RAW_1':
         RAW_1 = get_LIST_ALL_RAW (LIST_file_item_RAW=LIST_file_item_RAW)
         print (RAW_1)
         
      case 'RAW_2':       
         RAW_2 = get_LIST_SELECTED_RAW (LIST_file_item_RAW=LIST_file_item_RAW)
         print (RAW_2)
         
      case 'RAW_3':
         RAW_3 = get_data_items_RAW (file_path_RAW)
         print (RAW_3)

      case 'COOKED_1':
         COOKED_1 = get_LIST_ALL_COOKED (LIST_file_item_COOKED)
         print (COOKED_1)
         
      case 'COOKED_2':
         COOKED_2 = get_LIST_SELECTED_COOKED (LIST_file_item_COOKED)
         print (COOKED_2)
         
      case 'COOKED_3':      
         COOKED_3 = get_data_items_COOKED (file_path_COOKED)
         print (COOKED_3)

      case 'TO_BE_1':
         TO_BE_1 =  get_TO_BE_DATA_ITEMS (file_path_RAW, file_path_COOKED)
         print (TO_BE_1)
         
      case 'TO_BE_2':
         TO_BE_2 = get_LIST_to_be_SELECTED_with_data_items (LIST_file_item_RAW, LIST_file_item_COOKED)
         print (TO_BE_2)
   
      case 'LP':
         LP =  LP_all_data_items (LIST_file_item_RAW, LIST_file_item_COOKED, start_num, end_num)
         print (LP)
      
      case 'CF':
         CF = CF_all_data_chunk (LIST_file_item_RAW, LIST_file_item_COOKED, start_list_index, end_list_index)



#################################################################
###### TEST OUTPUT 
#################################################################

def TEST_OUTPUT (output_option):

   folder_path_R ='../../data/raw/'
   file_path_R = '../../data/raw/people_1.txt'
   file_select_mode_R = 'by_index'
   start_file_index_R = 1
   end_file_index_R = 2
   LIST_file_item_to_select_R = []
   file_prefix_R= 'people_'
   file_extension_R = '.txt'

   folder_path_C = '../../data/cooked/'
   file_path_C = '../../data/cooked/people_1a.txt'
   file_select_mode_C = 'by_index'
   start_file_index_C = 1
   end_file_index_C = 2
   LIST_file_item_to_select_C = []
   file_prefix_C= 'people_'
   file_extension_C = '.txt'

   start_list_index = 0
   end_list_index = 5

   LIST_file_item_R = [folder_path_R, file_path_R, file_select_mode_R, start_file_index_R, end_file_index_R, LIST_file_item_to_select_R, file_prefix_R, file_extension_R]
   LIST_file_item_C = [folder_path_C, file_path_C, file_select_mode_C, start_file_index_C, end_file_index_C, LIST_file_item_to_select_C, file_prefix_C, file_extension_C]


   TM_txt_to_txt (LIST_file_item_RAW, LIST_file_item_COOKED, start_list_index, end_list_index, output_option)



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
 
 

     
   
