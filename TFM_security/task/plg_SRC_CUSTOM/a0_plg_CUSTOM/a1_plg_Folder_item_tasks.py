

import sys
sys.path.append('../plg_CUSTOM/') 
sys.path.append('../../plg_SRC/a0_plg_TFM/') 
sys.path.append('../../plg_SRC/plg_DICT/')
sys.path.append('../../plg_SRC/plg_Date_time/') 

from plg_Date_time import * 


def create_folders (LIST_folder_path):

   for folder_path in LIST_folder_path:
   
      create_folder (folder_path)
   
   
     
# item could be a subfolder or a file 
def search_folder_item_by_index (folder_path, start_index, end_index):

   LIST_selected_item = get_folder_item_by_index (folder_path, start_index, end_index)
   
   return LIST_selected_item 
   
   
   
# item could be a subfolder or a file     
def search_folder_item_by_name (folder_path, my_item_name):

   LIST_selected_item = get_folder_item_by_name (folder_path, my_item_name)
   
   return LIST_selected_item 