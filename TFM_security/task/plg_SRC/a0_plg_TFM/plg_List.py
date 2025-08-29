


# https://www.w3schools.com/python/python_lists_access.asp
my_LIST = ["apple", "banana", "cherry", "orange", "apple", "apple"]



def get_LAST_item (my_LIST):

   last_LIST_item = my_LIST[-1]
   
   print (last_LIST_item)
   return last_LIST_item 
   
#get_LAST_list_item (my_LIST)   



#start after an index, end on an index
def get_START_AFTER_to_END_items (start_after_index, end_index, my_LIST):

   start_after_to_end_items = my_LIST [start_after_index:end_index]
   
   print (start_after_to_end_items)   
   return start_after_to_end_items
  
  
#get_START_AFTER_to_END_items (start_after_index=0, end_index=2, my_LIST=my_LIST)



def get_START_FROM_not_include_END_items (exclude_end_index, my_LIST):

   start_not_include_end = my_LIST [:exclude_end_index]
   
   print (start_not_include_end)
   return start_not_include_end
   
   
   
def get_START_AFTER_to_END_items (start_after_index, my_LIST):

   star_after_to_end = my_LIST [start_after_index:]
   
   print (start_after_to_end)
   return start_after_to_end
   
   
   
   
def insert_LIST_item (insert_item_index, LIST_item, my_LIST):

   LIST_with_inserted_item = my_LIST.insert (insert_item_index, LIST_item)
   
   print (LIST_with_inserted_item)
   return LIST_with_inserted_item
   
   

# https://www.w3schools.com/python/python_lists_change.asp 
def replace_N_values_with_ONE_value (start_value_index, end_value_index, single_value, my_LIST):

   #start_value_index starts from 0, but end_value_index starts count from 1, not from 0
   my_LIST[start_value_index : (end_value_index+1)] = [single_value]
   
   print (my_LIST)
   return my_LIST


#replace_N_values_with_ONE_value (start_value_index=0, end_value_index=2, single_value="shane", my_LIST=my_LIST)


LIST_1 = ["bro", "hello", "hey"]

def add_LIST_1_to_my_LIST (LIST_1, my_LIST):

   my_LIST.extend(LIST_1)
   
   print(my_LIST)
   return my_LIST


#add_LIST_1_to_my_LIST (LIST_1=LIST_1, my_LIST=my_LIST)



def remove_LIST_item_by_value (remove_value, my_LIST):

   my_LIST.remove(remove_value)
   
   print (my_LIST)
   return my_LIST
   
   
   

def remove_LIST_item_by_index (item_index, my_LIST):

  #item_index starts from 0, not 1
   my_LIST.pop(item_index)
   
   print (my_LIST)
   return my_LIST   
   
   
   
def delete_LIST (my_LIST):

   del my_LIST
      
   try: 
   
      my_LIST      
      print (str(my_LIST) + " NOT deleted")
      
   except:
      print ("my_LIST deleted")
   
     
#delete_LIST (my_LIST)   



def clear_LIST (my_LIST):

   my_LIST.clear()
   
   print(my_LIST)
   return my_LIST
   
   
   
   
def sort_LIST_alphanumerically (my_LIST):

   sorted_LIST = my_LIST.sort()
   
   print (sorted_LIST)
   return sorted_LIST
   
   

def sort_LIST_decending (my_LIST):

   sorted_LIST_decend = my_LIST.sort(reverse =True)

   print (sorted_LIST_decend)
   return (sorted_LIST_decend)   



def sort_LIST_case_sensitive (my_LIST):

   LIST_lower_to_upper_case = my_LIST.sort(key =str.lower)
   
   print (LIST_lower_to_upper_case)
   return LIST_lower_to_upper_case
   
   

def sort_LIST_reverse_order (my_LIST):

   LIST_reversed_value = my_LIST.reverse()
   
   print (LIST_reversed_value)
   return (LIST_reversed_value)
   
   
   
   
def copy_LIST_1 (my_LIST):

   my_LIST_COPY = my_LIST.copy()
   
   print (my_LIST_COPY)
   return my_LIST_COPY 
   
   
def copy_LIST_2 (my_LIST):

   my_LIST_COPY = list(my_LIST)
   
   print (my_LIST_COPY)
   return my_LIST_COPY 
   
   
   
def copy_LIST_3 (my_LIST):

   my_LIST_COPY = my_LIST[:]
   
   print (my_LIST_COPY)
   return my_LIST_COPY  



def join_two_LISTS (LIST_1, my_LIST):

   LIST_3 = LIST_1 + my_LIST
   
   print (LIST_3)
   return (LIST_3)
   
   
   
def append_LIST (LIST_1, my_LIST):

   for item in LIST_1:
   
      my_LIST.append(item)
   
   
   print (my_LIST )  
   return my_LIST
   
   
   
   
def extend_LIST (LIST_1, my_LIST):

   LIST_extended = my_LIST.extend(LIST_1)
   
   print (LIST_extended)
   return (LIST_extended)
   
   
   
   
def remove_LIST_duplicate_items_1 (my_LIST):

   my_LIST_unique = list(dict.fromkeys(my_LIST))
   
   print (my_LIST_unique)
   return my_LIST_unique
   
#remove_LIST_duplicate_items_1 (my_LIST) 

 
   
def remove_LIST_duplicate_items_2 (my_LIST):

   my_LIST_unique = list(set(my_LIST))
   
   print (my_LIST_unique)
   return my_LIST_unique
   
   
#remove_LIST_duplicate_items_2 (my_LIST)