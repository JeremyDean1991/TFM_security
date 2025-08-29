

import sys
sys.path.append('../plg_CUSTOM/') 
sys.path.append('../plg_TFM/') 

from plg_SSH import * 


#### Joomla ####

cmd_install_wget_unzip = "yum install -y wget unzip"
cmd_download_joomla = "wget -P /tmp/ https://downloads.joomla.org/cms/joomla3/3-9-25/Joomla_3-9-25-Stable-Full_Package.zip"

cmd_unzip_joomla = (
    "unzip -o /tmp/Joomla_3-9-25-Stable-Full_Package.zip -d /var/www/html/"
)

cmd_chown_html_dir = "chown -R apache:apache /var/www/html/*"

cmd_chmod_html_dir = "chmod -R 775 /var/www/html/*"

cmd_unzip_backup = "unzip -o /tmp/joomla.zip -d /var/www/html/"




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