

import sys
sys.path.append('../plg_CUSTOM/') 
sys.path.append('../plg_TFM/') 

from plg_SSH import * 




def find_file_by_name (file_name):

   find_file_by_name = 'find . -name ' + '*' + file_name + '*'
   return find_file_by_name   





def find_file_by_path (file_path):

   find_file_by_path = 'find . -path ' + '*' + file_path + '*'
   return find_file_by_path





# https://superuser.com/questions/204564/how-can-i-find-files-that-are-bigger-smaller-than-x-bytes
def find_file_size_bigger_or_smaller_than (option, file_size, measure):


   match option: 
   
      case "1":
         print ("find file size BIGGER than")

         find_file_size = 'find . -size ' + '+' + file_size + measure
         return find_file_size


      case "2":
         print ("find file size SMALLER than")

         find_file_size = 'find . -size ' + '-' + file_size + measure
         return find_file_size




# https://linuxconfig.org/how-to-use-find-command-to-search-for-files-based-on-file-size
def find_file_by_size (file_size, measure):

   find_file_by_size = 'find . -size ' + file_size + measure
   return find_file_by_size  





#https://stackoverflow.com/questions/62656579/why-im-getting-unicodeencodeerror-charmap-codec-cant-encode-character-u2 
def test ():  
 
   client1 = SSH_into_server (server_ip='107.150.45.226', SSH_username='root', SSH_password='Y4wxyopsvgu2!')  
   #client1 = SSH_into_server (server_ip='173.208.150.146', SSH_username='root', SSH_password='Vgd9x0ay6i7p!')  
   #_stdin_1, _stdout_1,_stderr_1 = client1.exec_command(test_print (msg1="man", msg2=" fuck"))
   
   _stdin_1, _stdout_1,_stderr_1 = client1.exec_command(find_file_by_name(file_name = 'ana'))
   #_stdin_2, _stdout_2,_stderr_2 = client1.exec_command(find_file_size_bigger_or_smaller_than (option='1', file_size='1', measure='k'))

   #encoding = locale.getpreferredencoding()

   print(_stdout_1.read().decode())
   print ('\n')
   #print(_stdout_2.read().decode(encoding))
   #print(_stdout_2.read().decode('ascii', 'ignore'))

   client1.close()
   
   
test()