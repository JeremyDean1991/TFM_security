

from a0_items import * 
from plg_Date_time import * 
import pymongo 
from pymongo import MongoClient
from pprint import pprint
import bson

from plg_DB_MongoDB_2 import * 
from plg_DB_LOG_task_request



#################################################################################################
#### LOG task item
################################################################################################# 
 
def LOG_task_item( LIST_mongodb_item, LIST_log_task_item_item):

   # get values from plg_Dict.py
   DICT_mongodb_item = DICT_mongodb_item (LIST_mongodb_item=LIST_mongodb_item)
   DICT_log_task_item_item = DICT_task_item_item (LIST_log_task_item_item)
   
   conn_str = DICT_mongodb_item ['conn_str']
   db_name = DICT_mongodb_item ['db_name']
   coll_name = DICT_mongodb_item ['coll_name']
   
   create_doc_then_return_id = create_ONE_document (conn_str=conn_str, db_name=db_name, coll_name=coll_name, doc_data=DICT_task_request_log_item)
   
   return create_doc_then_return_id
   
   
'''  

Task_item = send_email (email) # assume this function returns the sent email value 

conn_str ="mongodb://localhost:27017/"
db_name = "mydatabase"
coll_name = "mycoll"

Doc_id = ''
Doc_title = Task_item

Date_time_started = datetime.now() # Date_time_started and Date_time_completed should be the same 
Date_time_completed = datetime.now()
Status = 'Logged'
Description = Email sent + str(Task_item)
 

LIST_mongodb_item = [conn_str, db_name, coll_select_mode, coll_name, start_coll_index, end_coll_index, LIST_coll_item_to_select, doct_select_mode, doc_key, doc_id, doc_title, start_doc_index, end_doc_index, LIST_doc_item_to_select]
LIST_log_task_item_item = [doc_id, doc_title, date_time_started, date_time_completed, task_item, decription, status]  

LOG_task_item (LIST_mongodb_item=LIST_mongodb_item, LIST_log_task_item_item=LIST_log_task_item_item)   
'''   