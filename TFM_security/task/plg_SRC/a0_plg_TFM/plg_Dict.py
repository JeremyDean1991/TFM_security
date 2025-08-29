



### https://www.w3schools.com/python/python_dictionaries_remove.asp

def create_DICT (LIST_key, LIST_value):

   my_dict = {}

   # Populate the dictionary keys + values using a for loop
   for key, value in zip(LIST_key, LIST_value):
      
      my_dict[key] = value

   print(my_dict)
   return my_dict

#create_test_DICT ()  
   

'''
LIST_val_3 = [1,2,3,4]

# Create a list of keys
LIST_key = ['key1', 'key2', 'key3']
LIST_value = ['val_1', 'val_2', LIST_val_3]

create_DICT (LIST_key, LIST_value)
'''



def get_DICT_keys (my_DICT):

   LIST_dict_key = my_DICT.keys()
   
   print (LIST_dict_key)
   return LIST_dict_key 


#show_DICT_keys (my_DICT)




def get_DICT_values (my_DICT):

   LIST_dict_value = my_DICT.values()
   
   print (LIST_dict_value)
   return LIST_dict_value


#get_DICT_values (my_DICT=DICT_test())




# get both key + value 
def get_DICT_items (my_DICT):

   LIST_dict_item = my_DICT.items()
   
   print (LIST_dict_item)
   return LIST_dict_item


#get_DICT_items (my_DICT=DICT_test())




def get_DICT_value_by_key (my_DICT, my_KEY):

   get_value_by_key = my_DICT.get(my_KEY)
   
   #print (get_value_by_key)
   return get_value_by_key
   
'''
output = get_DICT_value_by_key (my_DICT=DICT_test(), my_KEY='LIST color')   
print ('DICT colors => ' + str(output), flush=True)
'''


def change_DICT_value (my_DICT, my_KEY, new_VAL):

   my_DICT[my_KEY] = new_VAL
   
   print (my_DICT)
   return my_DICT
   
   

def update_DICT_value (my_DICT, update_KEY, update_VAL):

   my_DICT_updated = my_DICT.update({update_KEY: update_VAL})
   
   print (my_DICT_updated)
   return (my_DICT_updated)
   
   


def remove_DICT_item_by_key (my_DICT, my_KEY):

   my_DICT_item_removed = my_DICT.pop(my_KEY) 

   print (my_DICT_item_removed)
   return my_DICT_item_removed    
   
   
   
def remove_DICT_last_item (my_DICT):

   my_DICT_last_item_removed = my_DICT.popitem()
   
   print (my_DICT_last_item_removed)
   return my_DICT_last_item_removed 
   
   
   
def delete_DICT_item_by_key (my_DICT, my_KEY):

   del my_DICT [my_KEY]
      
   print (my_DICT)
   return my_DICT
   
   
   
def clear_DICT (my_DICT):

   my_DICT.clear()

   print (my_DICT)
   return (my_DICT)



   
def get_LIST_dict_key (my_DICT):

   LIST_value = []
   
   for value in my_DICT.values():
   
      LIST_value.append (value)
            
   print (LIST_value)
   return LIST_value 


#get_LIST_dict_key (my_DICT)




def get_LIST_dict_value (my_DICT):

   LIST_key = []
   
   for key in my_DICT.keys():
   
      LIST_key.append (key)
            
   print (LIST_key)
   return LIST_key




def LIST_dic_item (my_DICT):

   LIST_key_value = []
   
   for key, value in my_DICT.items():
   
      LIST_key_value.extend([key, value]) #use extend to append 2 values, instead of 1
            
   print (LIST_key_value)
   return LIST_key_value
      
#LIST_dic_item (my_DICT)



def copy_DICT_1 (my_DICT):

   my_DICT_COPY = my_DICT.copy()
   
   print (my_DICT_COPY)
   return my_DICT_COPY
   
   
   
def copy_DICT_2 (my_DICT):

   my_DICT_COPY = dict(my_DICT)
   
   print (my_DICT_COPY)
   return my_DICT_COPY
   
   
   

# Add new dict key and value if not exists    
def add_DICT_key_value (my_DICT, new_key, new_value):

   if new_key not in my_DICT:

      my_DICT[new_key] = new_value

   else:

      print (str(my_DICT[new_key]) + ' already exists')


   return my_DICT       
   
   
 

def add_DICT_value (my_DICT, my_key, new_value):

   if my_key in my_DICT:
   
      my_DICT[my_key].append(new_value)
      
   else:
      
      my_DICT[my_key] = new_value
      
      
   return my_DICT



###########################################################################
### TEST
############################################################################

def DICT_test ():

   my_DICT = {
  "brand": 'ford',
  "model": 'model123',
  "LIST color": ['red', 'blue', 'purple']
   }

   return my_DICT 

   
def TEST_add_key_value ():

   DICT_123 = DICT_test ()
   
   my_DICT = DICT_123
   new_key = 'LIST_part'
   new_value = ['part 1', 'part 2', 'part 3']
   
   output = add_DICT_key_value (my_DICT, new_key, my_LIST_value, new_value)
   
   print (output)
      
#TEST_add_key_value ()



def TEST_add_value ():

   DICT_123 = DICT_test ()
   
   my_DICT = DICT_123
   my_key = 'LIST color'
   new_value = ['shane', 'peter']
   
   output = add_DICT_value (my_DICT, my_key, new_value)
   
   print (output)
      
#TEST_add_value ()


def test_DICT ():

   key_1 ="brand"
   val_1 = "Ford"

   key_2 = "colors"
   val_2 = ["red", "white", "blue"]

   thisdict = {
     key_1: val_1,
     key_2: val_2
   }
   print(thisdict)
   return key_2, val_2

#test_DICT ()

#print (test_DICT ()[1])   


'''
===> TEST Task mode functions with dictionary args

TXT_to_TXT_2

get_LIST_raw_all (raw_folder_path)
get_LIST_cooked_all (cooked_folder_path)

get_LIST_raw_selected (raw_folder_path, LIST_raw_file_num_to_select, raw_file_prefix, raw_file_extension )
get_LIST_cooked_selected (cooked_folder_path, LIST_cooked_file_num_to_select, cooked_file_prefix, cooked_file_extension )

get_raw_DATA_ITEMS
get_cooked_DATA_ITEMS
get_TO_BE_DATA_ITEMS

do_one_DATA_ITEM

get_LIST_to_be_selected_with_data_item (raw_folder_path, LIST_raw_file_num_to_select, raw_file_prefix, raw_file_extension  |||| cooked_folder_path, LIST_cooked_file_num_to_select, cooked_file_prefix, cooked_file_extension)

get_LIST_to_be_selected_with_data_item (LIST_raw_item, LIST_cooked_item)

   DICT_raw_item = 
   
   DICT_cooked_item = 


LP_all_data_items

CF_all_data_item  
'''