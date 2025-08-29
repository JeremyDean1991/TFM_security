

import numpy as np

# https://www.geeksforgeeks.org/break-list-chunks-size-n-python/


def list_SPLIT_1 (LIST_to_split, start_index, items_per_list ):

   LIST_of_list = []
        
   end_index = len(LIST_to_split)
     
   for i in range(start_index, end_index, items_per_list):
   
      x = i
      
      LIST_of_list.append(LIST_to_split[x:x+items_per_list])
      
      #print(LIST_to_split[x:x+items_per_list])
      
   return LIST_of_list


'''
LIST = [1, 2, 3, 4, 5,
           6, 7, 8, 9, 934]

print (list_SPLIT_1 (LIST_to_split=LIST, start_index=0, items_per_list=4 ))
'''



###############################################################################################################################
##### 
#################################################################################################################################

def create_LIST_total_output(total_num):

   LIST_total_output = []

   for i in range (total_num):
   
      LIST_total_output.append(i)
      
   return LIST_total_output




def split_LIST_output (total_num, start_index, items_per_list):
 
   LIST_total_output = create_LIST_total_output(total_num=total_num)
   
   # LOL = List of list 
   LOL_output_chunk = list_SPLIT_1 (LIST_to_split = LIST_total_output, start_index = start_index, items_per_list = items_per_list)
   
   return LOL_output_chunk



# The first and last element of each chunk only 
def get_LIST_output_first_last (total_num, start_index, items_per_list):

   LIST_output_chunk = split_LIST_output (total_num=total_num, start_index=start_index, items_per_list=items_per_list)
   
   LIST_output_first_last = []

   for chunk in LIST_output_chunk:
   
      # get only the first and last element of each chunk 
      LIST_output_first_last.append ([chunk[0], chunk[-1]])
      
     
   print (LIST_output_first_last, flush=True)  
   return LIST_output_first_last
   

'''
total_num = 1000
start_index = 0
items_per_list = 10      

get_LIST_output_first_last (total_num, start_index, items_per_list)
'''