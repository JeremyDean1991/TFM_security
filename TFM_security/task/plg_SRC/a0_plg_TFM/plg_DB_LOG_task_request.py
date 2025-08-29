

from a0_items import * 
from plg_Date_time import * 
import pymongo 
from pymongo import MongoClient
from pprint import pprint
import bson

from plg_DB_MongoDB_2 import * 
from plg_DB_LOG_task_request





def get_LIST_date (start_date, end_date):

   LIST_date = get_dt_every_day(start_date=start_date, end_date=end_date)[0]

   print (LIST_date)
   return LIST_date
   
#get_LIST_date (start_date=date(2024, 1, 1), end_date= date(2024, 12, 31))



########################################################################################################
#### LOG master task request ###########################################################################
#########################################################################################################

def create_DB_MASTER_log_request (conn_str):
 
   create_DB(conn_str =conn_str, db_name = 'LOG_master_task_request',  coll_name='test_1')



# date per collection    
def create_colls_master_log (start_date, end_date, conn_str):

   LIST_date = get_LIST_date (start_date=start_date, end_date=end_date)
   
   for date in LIST_date:
   
      create_collection (conn_str=conn_str, db_name="LOG_master_task_request", coll_name='L_MASTER_' + date)
       
#create_colls_master_log (start_date=date(2024, 1, 1),, end_date= date(2024, 12, 31), conn_str="mongodb://localhost:27017/") 



# 1 server ip per doc 
def create_servers_doc ():

   pass





# 1 server doc can have a list of TFM. Each TFM can have a list of task request urls 
def create_LIST_tfm ():

   pass




def create_LIST_tfm_task_request ():

   pass




def update_LIST_tfm_task_request ():

   pass




######################################################################################################
#### LOG tfm task request ###########################################################################
#######################################################################################################
#### Only 1 tfm task request log database per server 

# create a log request DB for a TFM
def create_DB_TFM_log_request (conn_str ):

     create_DB(conn_str =conn_str, db_name = 'LOG_task_request',  coll_name='test_1')
   


# 1 calender date per collection    
def create_colls_tfm_log (start_date, end_date, conn_str):

   LIST_date = get_LIST_date (start_date=start_date, end_date=end_date)
   
   for date in LIST_date:
   
      create_collection (conn_str=conn_str, db_name="LOG_task_request", coll_name='L_TFM' + date)
       
#create_colls_tfm_log (start_date=date(2024, 1, 1),, end_date= date(2024, 12, 31), conn_str="mongodb://localhost:27017/") 


   
# 1 request url per doc / log     
def create_log_DOC ():

   pass   
   
   
   
    

def DB_get_ALL_log_request ():

   pass
   
   




def DOC_get_log_request_by_task_name ():

   pass

   
   
   
def DOC_get_log_request_by_status ():


   pass




def DOC_insert_log_request ():

   pass
   # get server date time now (start date time)
   # use date time to find the correct collection
   # check rows before insert 
   # insert data into the correct db doc (insert start date time)
   
   
   
# update log task request status (completed, in progress, not completed within allowed duration)   
def DOC_update_LTR_status ():

   pass
   
   
   
   
def DOC_delete_LTR_task ():

   pass   
   
  

##############################################################################################
 
import inspect


# https://stackoverflow.com/questions/5067604/determine-function-name-from-within-that-function
def get_this_func_name():

   this_func_name = inspect.stack()[0][3]
   
   print(this_func_name)
   return this_func_name 
   
   print(inspect.stack()[1][3])  # will give the caller of foos name, if something called foo


#get_this_func_name() 
 
 
 
#################################################################################################
#### LOG task start & end  
################################################################################################# 
 
# log task start date time 
# TFM_name = name of the TFM (eg, TFM_email, TFM_sysadmin)
# TFM_task = name of the TFM task function to call  
# LIST_log_doc_data => a list of data for => DICT_log_doc_1

def LOG_task_request_start( LIST_mongodb_item, LIST_log_task_request_item):

   # get values from plg_Dict.py
   DICT_mongodb_item = DICT_mongodb_item (LIST_mongodb_item=LIST_mongodb_item)
   DICT_task_rquest_log_item = DICT_log_task_request_item (LIST_log_task_request_item)
   
   conn_str = DICT_mongodb_item ['conn_str']
   db_name = DICT_mongodb_item ['db_name']
   coll_name = DICT_mongodb_item ['coll_name']
   
   create_doc_then_return_id = create_ONE_document (conn_str=conn_str, db_name=db_name, coll_name=coll_name, doc_data=DICT_log_task_request_item)
   
   return create_doc_then_return_id
   
   
'''  
conn_str ="mongodb://localhost:27017/"
db_name = "mydatabase"
coll_name = "mycoll"

Doc_id = ''
Doc_title = ''
TFM_task_request_url = ''
TFM_name = ''
TFM_task = '' # data_item
Visitor_ip = ''

Date_time_started = datetime.now() 
Date_time_completed = ''
Allowed_task_duration = ''
Time_spend = ''
Status = ''
Description = ''
Notes      = ''  


LIST_mongodb_item = [conn_str, db_name, coll_select_mode, coll_name, start_coll_index, end_coll_index, LIST_coll_item_to_select, doct_select_mode, doc_key, doc_id, doc_title, start_doc_index, end_doc_index, LIST_doc_item_to_select]
LIST_log_task_request_item = [Doc_id, Doc_title, TFM_task_request_url, TFM_name, TFM_task, Visitor_ip, Date_time_started, Date_time_completed, Time_spent, Status, Description, Notes   ]   


LOG_task_request_start (LIST_mongodb_item=LIST_mongodb_item, LIST_log_task_request_item=LIST_log_task_request_item)   
'''   
   
   
# log task completed date time 
# TFM_name = name of the TFM (eg, TFM_email, TFM_sysadmin)
# TFM_task = name of the TFM task function to call  
# LIST_log_doc_data => a list of data for => DICT_log_doc_1

# Using Dict to create data structure instead of variables 
def LOG_task_request_end (LIST_mongodb_item, LIST_log_task_request_item):
  
   doc_id = LOG_task_start (LIST_mongodb_item=LIST_mongodb_item, LIST_log_task_request_item=LIST_log_task_request_item)   
   Doc_id ={ "_id": ObjectId (doc_id) }
   
   Date_time_completed = datetime.now()
    
   update_ONE_document (conn_str= conn_str, db_name=db_name, coll_name=coll_name, values_OLD=Doc_id, values_NEW ={ "$set": { "Date_time_completed": Date_time_completed})



# LIST_mongodb_item = [conn_str, db_name, coll_select_mode, coll_name, start_coll_index, end_coll_index, LIST_coll_item_to_select, doct_select_mode, doc_key, doc_id, doc_title, start_doc_index, end_doc_index, LIST_doc_item_to_select]
# LIST_log_task_request_item = [Doc_id, Doc_title, TFM_task_request_url, TFM_name, TFM_task, Visitor_ip, Date_time_started, Date_time_completed, Time_spent, Status, Description, Notes   ]   


#LOG_task_request_end (LIST_mongodb_item=LIST_mongodb_item, LIST_log_task_request_item=LIST_log_task_request_item)



#####################################################################################################################################
 
   
##### check to see if ANY task doc in the same collection has status = in progress (only 1 TFM can run on the same server on the same day)   
def get_status_LOG_task_request ():

   # get date time of the task request from db
   # get date time now of the server 

   # Task NOT started – If the task has NO started date time and NO completed date time. 

   # Task completed – If task started date time and completed date time exist for the particular task

   # Task in progress –  If the task has a started date time but NO completed date time. In addition, date time now – date time started ( time spent ) = LESS than allowed task duration (eg, 300 seconds)

   # Task NOT completed within allowed task duration – If the task has a started date time but NO completed date time. In addition, date time now – date time started ( time spent ) = MORE than allowed task duration (eg, 300 seconds)
   pass



# only one task function can run at the time, no other task functions are allowed to run on the same server at the same time     
def check_one_only_LOG_task_request (LIST_mongodb_item):

   DICT_m_item = DICT_mongodb_item (LIST_mongodb_item=LIST_mongodb_item)
   
   conn_str = DICT_m_item ['conn_str']
   db_name = DICT_m_item ['db_name']
   coll_name = DICT_m_item ['coll_name']   
    

   #get all docs from today's collection 
   LIST_all_doc = get_ALL_docs_in_collection (conn_str=conn_str, db_name=db_name, coll_name=coll_name)
   
   doc_key_STATUS = 'status'
      
   for doc in LIST_all_doc:
          
      doc_status = doc[doc_key_STATUS]
   
      if 'In progress' in doc_status:
         
         print ("TFM task NOT run because there are other tasks in progress")
         
         return 'NO'
      
      else:
   
        print ("Start TFM task")

        # call task function of TFM_task_router.py 
        return 'YES'     




# only one task function of the same name can run at the time, task function of other names may run at the same time on the same server 
def check_one_task_LOG_task_request (TFM_task, LIST_mongodb_item, LIST_task_status):

   DICT_m_item = DICT_mongodb_item (LIST_mongodb_item=LIST_mongodb_item)
   
   conn_str = DICT_m_item ['conn_str']
   db_name = DICT_m_item ['db_name']
   coll_name = DICT_m_item ['coll_name']   
    

   #get all docs from today's collection 
   LIST_all_doc = get_ALL_docs_in_collection (conn_str=conn_str, db_name=db_name, coll_name=coll_name)
   
   TFM_task = TFM_task
   doc_key_1 = 'TFM_task'
   doc_key_2 = 'status'
      
   for doc in LIST_all_doc:
   
      for task_status in LIST_task_status:
          
         doc_TFM_task = doc[doc_key_1]
         doc_status = doc[doc_key_2]
   
         if (TFM_task in doc_TFM_task and task_status in doc_status 
      
            print ("NO, task NOT started because its completed, in progress, or not completed within allowed task duration") 
            return 'NO'
      
         else:
   
           print ("YES, start the task")

           return 'YES'       




######  This function should be in plg_CUSTOM  ###################
def check_task_request_before_start (LIST_mongodb_item_RAW, LIST_mongodb_item_COOKED, LIST_task_request_log_item, LIST_concurrency_item_RAW, output_option):

   #LIST_task_status = ['In progress', 'Completed', 'Not completed within allowed task duration']   
   
   check_task_request = check_one_only_LOG_task_request (LIST_mongodb_item=LIST_mongodb_item_COOKED)
   
   if 'YES' not in check_task_request:
   
      print ('NOT start task')
           
   else:
   
      print ('start task')
      
      # log at the start of the task request
      LOG_task_request_start( LIST_mongodb_item=LIST_mongodb_item_COOKED, LIST_task_request_log_item=LIST_task_request_log_item)
             
      TM_mongodb_to_mongodb (LIST_mongodb_item_RAW, LIST_mongodb_item_COOKED, LIST_concurrency_item_RAW=LIST_concurrency_item_RAW, output_option=output_option)
            
      # update LOG after task request is completed 
      LOG_task_request_end (LIST_mongodb_item=LIST_mongodb_item_COOKED, LIST_task_request_log_item)      
      
   
   

####################################################################################
###### TFM task item log - 1 task item log for each TFM 


# create a log request DB for a TFM
def create_DB_TFM_log_task_item (conn_str ):

     create_DB(conn_str =conn_str, db_name = 'LOG_tfm_task_item',  coll_name='test_1')   
     
     
     
     
# 1 calender date per collection    
def create_colls_tfm_task_item (start_date, end_date, conn_str):

   LIST_date = get_LIST_date (start_date=start_date, end_date=end_date)
   
   for date in LIST_date:
   
      create_collection (conn_str=conn_str, db_name="LOG_tfm_task_item", coll_name='LTI_' + date) # LTI stands for Log task item 
       
#create_colls_tfm_item (start_date=date(2024, 1, 1),, end_date= date(2024, 12, 31), conn_str="mongodb://localhost:27017/")      




# 1 log per tfm item doc, eg 1 email sent per item doc 
def create_docs_tfm_task_item ():

   pass