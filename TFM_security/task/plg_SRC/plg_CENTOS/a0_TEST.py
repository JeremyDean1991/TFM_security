

import sys
#sys.path.append('../plg_CUSTOM/') 
sys.path.append('../plg_TFM/') 


from plg_SSH import *



def print_MSG (msg):

   show_msg = "echo " + msg
   
   return show_msg






#https://stackoverflow.com/questions/62656579/why-im-getting-unicodeencodeerror-charmap-codec-cant-encode-character-u2 
def test ():  
 
   #client1 = SSH_into_server (server_ip='107.150.45.226', SSH_username='root', SSH_password='Y4wxyopsvgu2!')  
   client1 = SSH_into_server (server_ip='173.208.150.146', SSH_username='root', SSH_password='Vgd9x0ay6i7p!')  
   #_stdin_1, _stdout_1,_stderr_1 = client1.exec_command(test_print (msg1="man", msg2=" fuck"))
   
   _stdin_1, _stdout_1,_stderr_1 = client1.exec_command(print_MSG(msg="hello how are you man
   
   "))


   #encoding = locale.getpreferredencoding()

   print(_stdout_1.read().decode())
   print ('\n')
   #print(_stdout_2.read().decode(encoding))
   #print(_stdout_2.read().decode('ascii', 'ignore'))

   client1.close()
   
#test()

