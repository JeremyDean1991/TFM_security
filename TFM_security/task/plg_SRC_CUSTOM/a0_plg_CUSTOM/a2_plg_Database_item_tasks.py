


import sys
sys.path.append('../plg_CUSTOM/') 
sys.path.append('../../plg_SRC/a0_plg_TFM/') 
sys.path.append('plg_SRC/plg_DICT/') 
sys.path.append('plg_SRC_CUSTOM/plg_TASK_MODE/') 

from plg_Folders import * 
from plg_TXT import * 
from plg_DB_MongoDB_2 import * 

from a0_plg_Country_section_topic import *
from a0_plg_Date_time import * 


########################################
### get collection names 
########################################


# for MOD database collections - eg, img_country_topic, rss_topic 
def get_LIST_coll_name_a1 (file_path_X):

   LIST_section_prefix =  get_LIST_section (file_path_X=file_path_X)
   LIST_postfix = ['country', 'topic', 'country_topic', 'url']
   LIST_coll_name = []
   
   for section_prefix in LIST_section_prefix:
   
      #print (section_prefix.strip())
   
      for postfix in LIST_postfix:
      
         coll_name = section_prefix.strip() + '_' + postfix 
      
         print (coll_name)
         
         LIST_coll_name.append(coll_name)
         
   return LIST_coll_name 


'''
path_X = '../../../data/raw/RAW_data_input/a2_start_data/section/section_prefix.txt'
get_LIST_coll_name_a1 (file_path_X=path_X)
'''


# country + #section 
def get_LIST_coll_name_a2 (file_path_X, file_path_Y, col_name):

   LIST_country_name = get_LIST_country (file_path_Y, col_name)   
   LIST_section_full = get_LIST_section (file_path_X=file_path_X)  
   LIST_coll_name = []
     
   for country_name in LIST_country_name:
   
      for section_full in LIST_section_full:
      
         coll_name = country_name.strip() + '_#' + section_full.strip()
         
         print (coll_name)
         
         LIST_coll_name.append(coll_name)
         
   return LIST_coll_name 
   
 
'''
file_path_X = '../../../data/raw/RAW_data_input/a2_start_data/section/section_full.txt'
file_path_Y = '../../../data/raw/RAW_data_input/a2_start_data/country/country_only.csv'
col_name = 'Name'

get_LIST_coll_name_a2 (file_path_X, file_path_Y, col_name)
'''


# for LOG database collections 
def get_LIST_coll_name_b1 (start_date, end_date):

   LIST_log_date = get_LIST_date_for_LOG(start_date= start_date, end_date= end_date )
   
   return LIST_log_date
   

#get_LIST_coll_name_b1 (start_date=date(2024, 1, 1), end_date= date(2024, 12, 31))




########################################
### create database items 
########################################

''' Databases to create

TFM_search_query
LOG_search_query

TFM_domain_section_query_url 
LOG_domain_section_query_url

TFM_master_search_query_url 
LOG_master_search_query_url

TFM_user_search_query_url 
LOG_user_search_request

LOG_task_request_url 

'''

def create_DBS (conn_str, LIST_db_name ):

   coll_name = 'demo_1'
   
   for db_name in LIST_db_name: 

      create_DB (conn_str=conn_str, db_name=db_name, coll_name=coll_name) 


# eg, LIST_coll_name = get_LIST_coll_name_a1
def create_COLLS(conn_str, db_name, LIST_coll_name):

   for coll_name in LIST_coll_name:
   
      create_collection (conn_str=conn_str, db_name=db_name, coll_name=coll_name)



def search_db_by_name (conn_str, my_db_name):

   LIST_db_selected = get_db_by_name (conn_str, my_db_name)
   
   return LIST_db_selected 
   
   

def search_db_by_index (conn_str, db_Start_index, db_end_index):

   LIST_db_selected = get_db_by_index (conn_str, db_start_index, db_end_index)
   
   return LIST_db_selected
   
   

def search_coll_by_name (conn_str, db_name, my_coll_name):

   LIST_coll_selected = get_collection_by_name (conn_str, db_name, my_coll_name)
   
   return LIST_coll_selected 
   
   
   
def search_coll_by_index (conn_str, db_name, coll_start_index, coll_end_index):

   LIST_coll_selected = get_collection_by_index (conn_str, db_name, coll_start_index, coll_end_index)
   
   return LIST_coll_selected 
   
   
  
def search_doc_by_index (conn_str, db_name, coll_name, doc_start_index, doc_end_index):

   LIST_doc_selected =get_doc_by_index (conn_str, db_name, coll_name, doc_start_index, doc_end_index)
   
   return LIST_doc_selected 

  
  
def search_doc_by_name (conn_str, db_name, coll_name, my_doc_name):

   LIST_doc_selected =get_doc_by_name (conn_str, db_name, coll_name, my_doc_name)
   
   return LIST_doc_selected 
   
  
  
