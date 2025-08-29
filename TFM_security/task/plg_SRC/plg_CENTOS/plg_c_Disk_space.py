

import sys
sys.path.append('../plg_CUSTOM/') 
sys.path.append('../plg_TFM/') 

from plg_SSH import * 



# https://www.redhat.com/sysadmin/linux-df-command
def get_filesystem_space (option):

   match option: 
   
      case "1":
         print ("Filesystem - disk usage")
      
         get_space_1 = 'df'
         return get_space_1
                  
      case "2":
         print ("Filesystem - short readable format")
      
         get_space_2 = 'df -h'
         return get_space_2
         
      case "3":
         print ("Filesystem - Inodes")
      
         get_space_3 = 'df -ih'   
         return get_space_3






#https://stackoverflow.com/questions/62656579/why-im-getting-unicodeencodeerror-charmap-codec-cant-encode-character-u2 
def test ():  
  
   client1 = SSH_into_server (server_ip='173.208.150.146', SSH_username='root', SSH_password='Vgd9x0ay6i7p!')  
   #_stdin_1, _stdout_1,_stderr_1 = client1.exec_command(test_print (msg1="man", msg2=" fuck"))
   
   _stdin_1, _stdout_1,_stderr_1 = client1.exec_command(get_filesystem_space(option="2"))
   _stdin_2, _stdout_2,_stderr_2 = client1.exec_command("lsblk")

   #encoding = locale.getpreferredencoding()

   print(_stdout_1.read().decode())
   print ('\n')
   #print(_stdout_2.read().decode(encoding))
   print(_stdout_2.read().decode('ascii', 'ignore'))

   client1.close()
   
test()