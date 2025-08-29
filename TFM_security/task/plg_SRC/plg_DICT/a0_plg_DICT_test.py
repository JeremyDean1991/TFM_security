


import sys
sys.path.append('../plg_CUSTOM/') 
sys.path.append('../plg_TFM/') 


from plg_DB_MongoDB_2 import * 


## Example on how to use DICT as args 
def DICT_people(LIST_people):

   #encforce data type on the dict values 
   DICT_people =  {

            "name":    str(LIST_people[0]),   
            "age":     int(LIST_people[1]),
            "gender":  str(LIST_people[2]),
            
      }
       
   return DICT_people

# LIST_people = [name, age, gender]



def get_DICT_by_list_people (LIST_people):

   DICT_p = DICT_people(LIST_people=LIST_people)

   person_name = get_DICT_value_by_key (my_DICT=DICT_p, my_KEY='name')
   person_age  = get_DICT_value_by_key (my_DICT=DICT_p, my_KEY='age')
   person_sex = get_DICT_value_by_key (my_DICT=DICT_p, my_KEY='gender')
   
   #print ('person name => ' + str(person_name))
   #print ('person age => ' + str(person_age))
   #print ('person sex => ' + str(person_sex))
   
   #LIST_for_dict_p = [person_name, person_age, person_sex]
   
   #return LIST_for_dict_p
   
'''
# create list of lists for multiple value lists 
LOLISTS_people = [['luke', 12, 'M'], ['pete', 19, 'M'], ['anna', 90, 'F']]

for LIST_p in LOLISTS_people:
   
   output = LIST_for_dict_people (LIST_people= LIST_p )
   print (output)
'''



# LIST_file_item = [folder_path, file_path, start_file_index, end_file_index, LIST_file_num_to_select, file_prefix, file_extension]
def DICT_file_item (LIST_file_item):

   # enforce data types on the dict values 
   DICT_file_item =  {

            "folder_path":                    LIST_file_item[0],   
            "file_path":                      LIST_file_item[1],
            
            "file_select_mode":               LIST_file_item[2]
            "start_file_index":               int(LIST_file_item[3]),
            "end_file_index":                 int(LIST_file_item[4]),
            
            "LIST_file_item_to_select":        list(LIST_file_item[5]),
            "file_prefix":                    LIST_file_item[6],
            "file_extension":                 LIST_file_item[7],                               
   }
     
   return DICT_file_item




# LIST_csv_item = [folder_path, csv_path, start_csv_index, end_csv_index, LIST_csv_num_to_select, csv_prefix, csv_extension, LIST_csv_column]
def DICT_csv_item (LIST_csv_item):

   DICT_csv_item =  {

            "folder_path":                   LIST_csv_item[0],   
            "csv_path":                      LIST_csv_item[1],
            
            "file_select_mode":              LIST_file_item[2]
            "start_csv_index":               int(LIST_csv_item[3]),
            "end_csv_index":                 int(LIST_csv_item[4]),
            
            "LIST_csv_item_to_select":        list(LIST_csv_item[5]),
            "csv_prefix":                    LIST_csv_item[6],
            "csv_extension":                 LIST_csv_item[7],      
            
            "LIST_csv_column":               list(LIST_csv_item[8]), # a list of csv column names     
   }
     
   return DICT_csv_item





# LIST_mongodb_item = [conn_str, db_name, coll_name, start_coll_index, end_coll_index, LIST_coll_item_to_select, csv_prefix, csv_extension, LIST_csv_column]
def DICT_mongodb_item (LIST_mongodb_item):

   # enforce data types on the dict values 
   DICT_mongodb_item =  {

           "conn_str":                  str(LIST_mongodb_item[0]),   
           "db_name":                   LIST_mongodb_item[1],
            
           "coll_select_mode":          LIST_mongodb_item[2]
           "coll_name":                 LIST_mongodb_item[3],
           "start_coll_index":          int(LIST_mongodb_item[4]),
           "end_coll_index":            int(LIST_mongodb_item[5]),
           "LIST_coll_item_to_select":   list(LIST_mongodb_item[6]),
            
            
           "doc_select_mode":           LIST_mongodb_item[7]
           "doc_key":                   LIST_mongodb_item[8], 
           'start_doc_index':           LIST_mongodb_item[9],
           'end_doc_index':             LIST_mongodb_item[10],
           'LIST_doc_item_to_select':    list(LIST_mongodb_item[11]),
                     
                       
   }
     
   return DICT_mongodb_item