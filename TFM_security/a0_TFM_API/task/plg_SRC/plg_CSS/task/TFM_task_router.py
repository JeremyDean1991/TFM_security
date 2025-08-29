

#####################################################
##### remove html tags to read it #########
#####################################################
'''
LOG_tfm_task_request = sys.argv[1]
TFM_task_action = sys.argv[2]

str_LOG_tfm_task_request = LOG_tfm_task_request.replace('<br>', '').replace("</br>", '')
str_TFM_task_action = TFM_task_action.replace('<br>', '').replace("</br>", '')
'''


def LOG_task_request ():

   #str_val =  extract_from_TFM_task_action ()[1]
   #print ("<br>" + str(str_val) + "</br>")


   #only 1 request url can run at a time, the url must not be in progress, completed or not complete within allowed duration 
   if 'one_unique' in str_LOG_tfm_task_request:
   
      check_LOG_1 ()
      TFM_task_action ()#must call this inside the LOG_task_request function, not outside it
      
   else:
   
      print ("<br> NOT one_unique </br>", flush=True)
      TFM_task_action ()#must call this inside the LOG_task_request function, not outside it
   
   
   #only 1 same request url without status = 'in progress', 'completed', 'Not completed withitn allowed duration' can run at a time, but other different request urls can run at the same time
   if 'many_unique' in LOG_tfm_task_request:
   
      pass
   
   
   #many request urls can run at the same time regardless of their statuses 
   if 'many' in LOG_tfm_task_request:
   
      pass
   
   


def TFM_task_action ():

   core_task_func = remove_all_after_text (after_text='#1', text_main=str_TFM_task_action).strip()
   conn_str = remove_all_before_and_after_texts (before_text='=', after_text='#2', text_main=str_TFM_task_action)
   db_name = remove_all_before_text (before_text='db_name=', text_main=str_TFM_task_action)
  
   
   match TFM_task: # TFM task name = includes name of the payment system  
   
      case "F_1": # create folders 
      FIT = Folder_item_tasks ()
      FIT.create_folder (folder_path)
      
      case "F_2": # create files
      FIT = Folder_item_tasks ()
      FIT.create_files (folder_path, LIST_file_name)
      
      case"F_3": # search folder item by index
      FIT = Folder_item_tasks ()
      FIT.search_folder_item_by_index (folder_path, start_index, end_index)
      
      case"F_4": # search folder item by name 
      FIT = Folder_item_tasks ()
      FIT.search_folder_item_by_name (folder_path, my_item_name)
      
      case "DB_1": # create databases 
      DBIT = Database_item_tasks ()
      DBIT.create_DBS (conn_str, LIST_db_name)
      
      case "DB_2": # create db collections 
      DBIT = Database_item_tasks ()
      DBIT.create_COLLS (conn_str, db_name, LIST_coll_name)      
      
      case"DB_3": # search db by index 
      DBIT = Database_item_tasks ()
      DBIT.search_db_by_index (conn_str, db_Start_index, db_end_index)  
      
      case"DB_4": # search db by name 
      DBIT = Database_item_tasks ()
      DBIT.search_db_by_name (conn_str, my_db_name)
      
      case"DB_5": # search coll by index
      DBIT = Database_item_tasks ()
      DBIT.search_coll_by_index (conn_str, db_name, coll_start_index, coll_end_index)
      
      case"DB_6": # search coll by name 
      DBIT = Database_item_tasks ()
      DBIT.search_coll_by_name (conn_str, db_name, my_coll_name)
      
      case"DB_7": # search doc by index
      DBIT = Database_item_tasks ()
      DBIT.search_doc_by_index (conn_str, db_name, coll_name, doc_start_index, doc_end_index)
      
           
      case"DB_8": # search doc by name 
      DBIT = Database_item_tasks ()  
      DBIT.search_doc_by_name (conn_str, db_name, coll_name, my_doc_name)
      
            
      case "DB_7": # sharding collections
      sharding??   


      case "LP_crawler_scraper_1": # TM_txt_to_mongodb - RAW txt url --> COOKED db start_url 
      DIT = Data_item_tasks ()
      DIT.LP_crawler_scraper_1 ()
      
      case "CF_crawler_scraper_1": # TM_txt_to_mongodb - RAW txt url --> COOKED db start_url
      DIT = Data_item_tasks ()
      DIT.CF_crawler_scraper_1 ()
      
      case "LP_crawler_scraper_2": # TM_mongodb_to_mongodb - RAW txt url --> COOKED db start_url 
      DIT = Data_item_tasks ()
      DIT.LP_crawler_scraper_2()
      
      case "CF_crawler_scraper_2": # TM_mongodb_to_mongodb - RAW url data --> COOKED db url data
      DIT = Data_item_tasks ()
      DIT.CF_crawler_scraper_2 ()


      case "LP_search_query_1": # TM_txt_to_mongodb - RAW txt search query --> COOKED db search query 
      DIT = Data_item_tasks ()
      DIT.LP_search_query_1 ()
      
      case "CF_search_query_1": # TM_txt_to_mongodb - RAW txt search query --> COOKED db search query 
      DIT = Data_item_tasks ()
      DIT.CF_search_query_1 ()
      
      case "LP_search_query_2": # TM_mongodb_to_mongodb - RAW db search query --> COOKED db search query 
      DIT = Data_item_tasks ()
      DIT.LP_search_query_2 ()
      
      case "CF_search_query_2": # TM_mongodb_to_mongodb - RAW db search query --> COOKED db search query 
      DIT = Data_item_tasks ()
      DIT.CF_search_query_2 ()     
                  
    
      case "LP_dsqu_1": # TM_txt_to_mongodb - RAW txt dsqu --> COOKED db dsqu
      DIT = Data_item_tasks ()
      DIT.LP_domain_section_query_url_1()
      
      case "CF_dsqu_1": # TM_txt_to_mongodb - RAW txt dsqu --> COOKED db dsqu
      DIT = Data_item_tasks ()
      DIT.CF_domain_section_query_url_1 ()
      
      case "LP_dsqu_2": # TM_mongodb_to_mongodb - RAW db dsqu --> COOKED db dsqu
      DIT = Data_item_tasks ()
      DIT.LP_domain_section_query_url_2 ()
      
      case "CF_dsqu_2": # TM_mongodb_to_mongodb - RAW db dsqu --> COOKED db dsqu 
      DIT = Data_item_tasks ()
      DIT.CF_domain_section_query_url_2 ()       
         
      case "LP_msqu_1": # TM_mongodb_to_mongodb - RAW db msqu  --> COOKED db usqu 
      DIT = Data_item_tasks ()
      DIT.LP_master_search_query_url_1 ()
      
      case "CF_msqu_1": # TM_mongodb_to_mongodb - RAW db msqu --> COOKED db dsqu 
      DIT = Data_item_tasks ()
      DIT.CF_domain_section_query_url_1 ()
              
      case "LP_log_usr_1": # TM_mongodb_to_mongodb - RAW db msqu  --> COOKED db usqu 
      DIT = Data_item_tasks ()
      DIT.LP_log_usr_1()
      
      case "CF_log_usr_1": # TM_mongodb_to_mongodb - RAW db msqu --> COOKED db dsqu 
      DIT = Data_item_tasks ()
      DIT.CF_log_usr_1()    


      
   
#LOG_task_request ()

core_task_func =''
TFM_task_action ()