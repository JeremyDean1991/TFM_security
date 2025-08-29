


#from plg_DB_LOG_task_request import * 


# create do_one_DATA_ITEM in another file, then import it into this file 
def do_one_DATA_ITEM (data_item):

   # do task's data item here 
   print (" This task is to print out => " + str(data_item), flush=True)
   
   # LOG each data item or task item 
   LOG_task_item (data_item)
   
     
   
   
def test_return ():

   return 'NO'
   

def test_again ():

   test = test_return ()
   
   if 'YES' in test:
   
      print ('YES is in ' + test)
      
   else:
   
      print ('NO is in ' + test)
      
      
test_again ()