

import sys
sys.path.append('../plg_CUSTOM/') 
sys.path.append('../plg_TFM/') 

from plg_SSH import * 



### epel-release 
cmd_install_epel_release = 'yes | sudo yum install epel-release' # yes | will ansewr YES to the prompt. yes no | ansewr NO to the prompt.
cmd_import_epel_gpg_key = 'rpm --import http://download.fedoraproject.org/pub/epel/RPM-GPG-KEY-EPEL-6'

cmd_search_epel_version = 'yum search epel-release'
cmd_epel_install_path = 'rpm -q --filesbypkg epel-release'

#Check installed package versions -- https://www.tecmint.com/install-epel-repository-on-centos/
cmd_info_epel_version = 'yum info epel-release'
cmd_remove_epel_release = 'yes | yum remove epel-release' # yes | will ansewr YES to the prompt. yes no | ansewr NO to the prompt.
cmd_update_after_remove_epel_release = 'yes | yum update' # yes | will ansewr YES to the prompt. yes no | ansewr NO to the prompt.



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