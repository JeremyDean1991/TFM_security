

import urllib.parse
import requests 


###################################
##### Uses the Urlib libray #######
####################################

def Url_encode_1(url):

   encoded_url = urllib.parse.quote_plus(url)    
   print (encoded_url)
   
   return encoded_url 

#Encoded_url = Url_encode ( url = 'http://localhost/TEST_CODE/a2_test_API.php/run?LOG_task_request=one_unique&TFM_task_action=func_1#1conn_str=hello1#2db_name=hello2#3raw_db_name=shane2{"name":name,"age":age,"address":address,"country":country,')



def Url_decode_1 (encoded_url):

   decoded_url = urllib.parse.unquote(encoded_url)
   print (decoded_url)
   
   return decoded_url 
   

#Url_decode(encoded_url = Encoded_url)


######################################
##### Uses the Request library #######
#######################################

def Url_encode_2 (url):

   encoded_url = requests.utils.quote(url) 
   print (encoded_url)
   
   return encoded_url
   
#Encoded_url_2 = Url_encode_2 (url = 'http://localhost/TEST_CODE/a2_test_API.php/run?LOG_task_request=one_unique&TFM_task_action=func_1#1conn_str=hello1#2db_name=hello2#3raw_db_name=shane2{"name":name,"age":age,"address":address,"country":country,')   
   
   
def Url_decode_2 (encoded_url):

   decoded_url = requests.utils.unquote(encoded_url) 
   print (decoded_url)
   
   return decoded_url
   
   
#Url_decode_2 (encoded_url=Encoded_url_2)