

import sys
sys.path.append('../plg_CUSTOM/') 
sys.path.append('../plg_TFM/') 

from plg_SSH import * 


# SSH Allow Deny
ssh_touch_files = 'touch /etc/hosts.{allow,deny}'
ssh_add_to_allow_list = 'echo "sshd: {}" >> /etc/hosts.allow'
ssh_deny_hosts = 'echo "sshd: ALL" >> /etc/hosts.deny'




#https://stackoverflow.com/questions/62656579/why-im-getting-unicodeencodeerror-charmap-codec-cant-encode-character-u2 
def test ():  
 
   #client1 = SSH_into_server (server_ip='107.150.45.226', SSH_username='root', SSH_password='Y4wxyopsvgu2!')  
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