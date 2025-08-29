

import sys
sys.path.append('../a0_plg_CUSTOM/') 
sys.path.append('../plg_TFM/') 
sys.path.append('../plg_DICT/') 

from plg_DICT_database import * 

from a0_items import * 
from plg_Str_char import * 
from plg_Regex import * 
from plg_Files import * 
from plg_Folders import * 
from plg_TXT import * 
from plg_list_SPLIT import * 
from plg_Concurrency_2 import * 



# Raw files words --> selected words ---> write selected words to cooked files 

##### Must download & install MongoDB software from --> https://www.mongodb.com/try/download/community #######
# https://www.w3schools.com/python/python_mongodb_getstarted.asp


def get_LIST_raw_ALL (raw_folder_path):

   LIST_raw_ALL = get_ALL_in_folder (folder_path=raw_folder_path)
   
   return LIST_raw_ALL 
   
'''
folder_path = '../../data/raw/RAW_rss_feeds/a2_RSS_topics/a1_RSS_topics_1/'
print (get_LIST_raw_ALL (raw_folder_path=folder_path), flush=True)
'''
  
  
def get_LIST_cooked_ALL (cooked_folder_path):

   LIST_cooked_ALL = get_ALL_in_folder (folder_path=cooked_folder_path)
   
   return LIST_cooked_ALL 
   

'''
folder_path = '../../data/raw/RAW_rss_feeds/a2_RSS_topics/a1_RSS_topics_2/'
print (get_LIST_cooked_ALL (cooked_folder_path=folder_path), flush=True)
'''

      
#################################################################
### select & process data files by file number instead of index 
#################################################################  
   
def create_file_num (start_num, end_num):

   LIST_file_num = []

   for x in range (start_num, end_num):
   
      LIST_file_num.append(str(x))
      
      
   return LIST_file_num

'''
LIST_num = create_file_num (start_num=0, end_num=20)
print (LIST_num)
'''


def get_ONE_raw_SELECTED (raw_folder_path, f_num):

   LIST_raw_ALL = get_LIST_raw_ALL (raw_folder_path=raw_folder_path)
  
   for raw_file in LIST_raw_ALL:
   
      raw_file_num = raw_file.replace('F_', '').replace('.txt', '').strip()

      if f_num == raw_file_num:
      
         return raw_file
         
      else:
      
         #print (raw_file_num + ' NOT in ' + raw_file_num)
         pass

'''         
path_1 = '../../data/raw/RAW_rss_feeds/a2_RSS_topics/a1_RSS_topics_1/'
f_num = '3'
print (get_ONE_raw_SELECTED_2 (raw_folder_path=path_1, f_num=f_num), flush=True)
'''


def get_LIST_raw_SELECTED (raw_folder_path, start_num, end_num):
 
   LIST_file_num = create_file_num (start_num=start_num, end_num=end_num)
   
   LIST_raw_selected = []

   for num in LIST_file_num:
   
      selected_raw_file = get_ONE_raw_SELECTED_2 (raw_folder_path=raw_folder_path, f_num=num)
        
      LIST_raw_selected.append(selected_raw_file)
      #print (selected_raw_file, flush=True)
      
   return LIST_raw_selected 
      
 
'''
folder_path = '../../data/raw/RAW_rss_feeds/a2_RSS_topics/a1_RSS_topics_1/'
start=0
end=20
print (get_LIST_raw_SELECTED_2 (raw_folder_path=folder_path, start_num=start, end_num=end))
'''



# May delete all files before create new 
def delete_ALL_cooked_files (cooked_folder_path):

   LIST_all_cooked_file = get_LIST_cooked_ALL (cooked_folder_path)
   
   for cooked_file in LIST_all_cooked_file:
   
      delete_file (file_path=cooked_folder_path + cooked_file)




# create empty cooked files to save extracted raw data from each raw file    
def create_empty_cooked_files (raw_folder_path, cooked_folder_path):

   #create empyt cooked files if not exist
   
   count_LIST_raw_ALL = len(get_LIST_raw_ALL (raw_folder_path=raw_folder_path))
   
   for num in range (count_LIST_raw_ALL):
   
      #print (x)
      create_TXT_file (path_TXT=cooked_folder_path + 'C_' + str(num) +'.txt')
   
   
'''   
folder_path = '../../data/raw/RAW_rss_feeds/a2_RSS_topics/a1_RSS_topics_1/'
cooked_folder_path = '../../data/raw/RAW_rss_feeds/a2_RSS_topics/a1_RSS_topics_2/'
print (create_empty_cooked_files (raw_folder_path=folder_path, cooked_folder_path=cooked_folder_path))
'''



def get_raw_DATA_ITEMS (raw_file_path):
  
   LIST_raw_data_item = File_read_lines (file_path = raw_file_path)
   
   LIST_data_item = []
   
   for item in LIST_raw_data_item:
   
      try: 
      
         #print (item, flush=True)
         LIST_data_item.append (item)
                 
      except:
      
         #print ("An error has occured")
         pass 
         
   return LIST_data_item 

''' 
path = '../../data/raw/RAW_rss_feeds/a2_RSS_topics/a1_RSS_topics_1/F_1.txt'
print (str(get_raw_DATA_ITEMS_2 (raw_file_path=path)).encode('utf-8'))
''' 


# get all raw files --> get raw files selected --> get selected raw file data --> split raw data into chunks --> CF each chunk, check a-z words --> print a-z words to cooked file 


# only need to get RAW data, no need COOKED and TO_BE data 
def get_LIST_raw_selected_with_data_item (raw_folder_path, start_num, end_num):

   LIST_raw_file_SELECTED =  get_LIST_raw_SELECTED (raw_folder_path=raw_folder_path, start_num=start_num, end_num=end_num)
   
   # RAW files & data 
   LIST_raw_file_data_SELECTED = []
   
   # get_RAW_DATA_ITEMS_2 resturns a list of RAW data 
   for raw_file in LIST_raw_file_SELECTED:
        
      LIST_RAW_item = get_raw_DATA_ITEMS(raw_file_path=raw_folder_path + raw_file)
      #print (str(TO_BE_item).encode(), flush=True)

      #LIST_to_be_file_data_SELECTED.append( raw_file + ' #_0 ' + str(LIST_TO_BE_item) )
      LIST_RAW_item.insert (0, raw_file)
      LIST_raw_file_data_SELECTED.append(LIST_RAW_item)

   return LIST_raw_file_data_SELECTED



F_PATH = '../../data/raw/RAW_rss_feeds/a2_RSS_topics/a1_RSS_topics_2/' 

def do_one_DATA_ITEM (data_item):

   print (str(data_item).encode(), flush=True)

   # remove all numbers from data item 
   # remove leading spaces of data item, but keep nextline 
   # change data item to lower case 
   # get data item starts with a-z 
   # write data item to cooked file with same file number as raw file 
    
   folder_path = F_PATH 
   file_raw = remove_all_after_text (after_text='#0', text_main=data_item)
   file_cooked = file_raw.replace('F_', 'C_')
   #content_1 = str(remove_all_before_text (before_text='#0', text_main=data_item)) + '\n'   
   #content_2 = get_LIST_word_a_to_z (LIST_word=content_1)
   
   #print (content_1)
   #print (content_2)
   #File_write_one (file_path=folder_path + file_cooked, write_mode='a', content=content_2)   
   
    
    
###############################################################
###### Process data items by loop (LP)
##############################################################
  
# Process data item by loop
def LP_all_data_items (raw_folder_path, start_num, end_num):

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
#################################################################
      
# process data item by concurrent futures 
def CF_all_data_chunks_2 (raw_folder_path, start_num, end_num, start_index, items_per_list, do_one_DATA_ITEM, pause_secs):

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
         
         file_name_and_data = data_file_only + " #0 " + file_data
         #print (str(file_name_and_data).encode(), flush=True)
         
         LIST_file_name_and_data.append(file_name_and_data)
         
                       
   CF_all_data_chunks (LIST_data_item_split=LIST_file_name_and_data, start_index=start_index, items_per_list=items_per_list, do_one_DATA_ITEM=do_one_DATA_ITEM, pause_secs=pause_secs )
         
         
         
'''                
raw_folder ='../../data/raw/RAW_rss_feeds/a2_RSS_topics/a1_RSS_topics_1/'
start_num = 0
end_num = 2
start_index = 0
items_per_list = 5
pause_secs = 0

if __name__ == '__main__':

   CF_all_data_chunks_2 (raw_folder_path=raw_folder, start_num=start_num, end_num=end_num, start_index=start_index, items_per_list=items_per_list, do_one_DATA_ITEM = do_one_DATA_ITEM_2, pause_secs=pause_secs)
   
   '''