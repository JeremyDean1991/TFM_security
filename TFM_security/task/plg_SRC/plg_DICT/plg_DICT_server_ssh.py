


def DICT_ssh_item (LIST_ssh_item):

   # enforce data types on the dict values 
   DICT_ssh_item =  {

            "server_name"                LIST_ssh_item[0], 
            "server_ip":                    LIST_ssh_item[1],   
            "ssh_username":                      LIST_ssh_item[2],         
            "ssh_password":               LIST_ssh_item[3],  
            "ssh_port"                    LIST_ssh_item[4], 
   }
     
   return DICT_ssh_item
   # LIST_ssh_item = [server_ip, ssh_username, ssh_password, ssh_port]
   
   
   
def DICT_server_item (LIST_server_item):

   # enforce data types on the dict values 
   DICT_server_item =  {

            "server_name"                LIST_server_item[0],
            "server_ip":                    LIST_server_item[1],   
            "username":                      LIST_server_item[2],         
            "password":                     LIST_ssh_item[3], 
            
            "LIST_operating_system":      LIST_server_item[4], 
            "LIST_browser"                LIST_server_item[5], 
            "LIST_folder":               LIST_server_item[6], 
            "LIST_file":               LIST_server_item[7],            
            
            "LIST_cpu":                      LIST_server_item[8],         
            "LIST_ram":               LIST_server_item[9], 
            "LIST_hdd":                      LIST_server_item[10],         
            "LIST_ssd":               LIST_server_item[11],              
 
              
                             
   }
     
   return DICT_server_item
   # LIST_server_item = [server_ip, username, password, LIST_operating_system, LIST_browser, LIST_folder, LIST_file, LIST_cpu, LIST_ram, LIST_hdd, LIST_ssd]   