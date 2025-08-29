
from a0_items import * 
from plg_list_SPLIT import * 

import multiprocessing 
from multiprocessing import Process
from concurrent.futures import ThreadPoolExecutor, wait
import concurrent.futures
import time 

### NOTE: Concurrent futures may be sloewr than loop due to Global interpreter lock (GIL)

def test_task_1 (data_item):

   print ( data_item)
   
     
def test_task_2 (data_item):

   print (" do task 2 => " + data_item)



def CF_one_data_chunk (do_one_DATA_ITEM, LIST_data_item):

   with concurrent.futures.ProcessPoolExecutor() as executor:
        
      executor.map(do_one_DATA_ITEM, LIST_data_item)
        
      t2 = time.perf_counter()
      print (f' finished in {t2} seconds')      
      
     

def CF_all_data_chunks (LIST_data_item_split, start_index, items_per_list, do_one_DATA_ITEM, pause_secs ):

   LOL_data_item_chunk = list_SPLIT_1 (LIST_to_split = LIST_data_item_split, start_index = start_index, items_per_list = items_per_list) 

   for data_item_chunk in LOL_data_item_chunk:  
           
      #print (str(data_item_chunk).encode(), flush=True)       
      CF_one_data_chunk(do_one_DATA_ITEM = do_one_DATA_ITEM  ,LIST_data_item = data_item_chunk)
      
      time.sleep(pause_secs)
         

   
'''
#must run concurrency using if __name__ == '__main__'
if __name__ == '__main__':

   LIST_a= ["hello", "yes", "1234", "BRO", "yo", "man"]

   #CF_one_data_chunk (do_one_DATA_ITEM=test_task_1, LIST_data_item=LIST_a)

   CF_all_data_chunks (LIST_data_item_split=LIST_a, start_index=0, items_per_list=2, do_one_DATA_ITEM = test_task_1, pause_secs=0 )
'''