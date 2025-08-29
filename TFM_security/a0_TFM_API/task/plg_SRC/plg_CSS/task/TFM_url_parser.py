
import sys, os

from plg_DICT_database import * 
from plg_Regex import * 
from a2_test_CORE_TASK import * 
from plg_DB_LOG_task_rquest import * 



#####################################################
##### remove html tags to read it #########
#####################################################

TFM_task_request_url = sys.argv[1] # the full url of the request
LOG_tfm_task_request = sys.argv[2] # call LOG_tfm_task_request function 
TFM_task_action = sys.argv[3] # variables needed to run TFM_task_action functions from TFM_task_router
Visitor_ip = sys.argv[4] # visiter's IP address to be logged 


str_LOG_tfm_task_request = LOG_tfm_task_request.replace('<br>', '').replace("</br>", '')
str_TFM_task_action = TFM_task_action.replace('<br>', '').replace("</br>", '')

# get variable values from the url 

server ip
TFM directory 
LOG tfm requet 
TFM task action 
Visitor info (ip, browser, os, country..etc)


### TFM task action 
# TFM_task_action =create_DB_LOG_country #1 conn_str = mongodb://localhost:27017/ #2 db_name=my_db

# First extract the array from the url string 
LIST_file_item_R = remove_all_after_text (after_text='#1', text_main=str_TFM_task_action).strip()
folder_path_RAW = LIST_file_item_R[0]
file_path_RAW = LIST_file_item_R[1]
file_select_mode_RAW = LIST_file_item_R[2]
start_file_index_RAW = LIST_file_item_R[3]
end_file_index_RAW = LIST_file_item_R[4]
LIST_file_item_to_select_RAW = LIST_file_item_R[5]
file_prefix_RAW = LIST_file_item_R[6]
file_extension_RAW = LIST_file_item_R[7]

LIST_file_item_RAW = [folder_path_RAW, file_path_RAW, file_select_mode_RAW, start_file_index_RAW, end_file_index_RAW, LIST_file_item_to_select_RAW, file_prefix_RAW, file_extension_RAW]


# First extract the array from the url string 
LIST_mongodb_item_C = remove_all_after_text (after_text='#2', text_main=str_TFM_task_action).strip()
conn_str_COOKED = LIST_mongodb_item_C[0]
db_name_COOKED = LIST_mongodb_item_C[1]
coll_select_mode_COOKED = LIST_mongodb_item_C[2]
coll_name_COOKED = LIST_mongodb_item_C[3]
start_coll_index_COOKED = LIST_mongodb_item_C[4]
end_coll_index_COOKED = LIST_mongodb_item_C[5]
LIST_coll_item_to_select_COOKED = LIST_mongodb_item_C[6]
doc_select_mode_COOKED =LIST_mongodb_item_C[7]
doc_key_COOKED = LIST_mongodb_item_C[8]
doc_id_COOKED = LIST_mongodb_item_C[9]
doc_title_COOKED =LIST_mongodb_item_C[10]
start_doc_index_COOKED =LIST_mongodb_item_C[11]
end_doc_index_COOKED =LIST_mongodb_item_C[12]
LIST_doc_item_select_COOKED = LIST_mongodb_item_C[13]

LIST_mongodb_item_COOKED = [conn_str, db_name, coll_select_mode, coll_name, start_coll_index, end_coll_index, LIST_coll_item_to_select, doc_select_mode, doc_key, doc_id, doc_title, start_doc_index, end_doc_index, LIST_doc_item_to_select]






