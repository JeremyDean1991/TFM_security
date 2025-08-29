

import sys
sys.path.append('../plg_CUSTOM/') 
sys.path.append('../plg_TFM/') 

from plg_SSH import * 


cmd_download_RKhunter = '''wget http://downloads.sourceforge.net/project/rkhunter/rkhunter/1.4.6/rkhunter-1.4.6.tar.gz
tar zxvf rkhunter-1.4.6.tar.gz
'''
cmd_install_RKhunter = 'cd rkhunter-1.4.6 && bash installer.sh --layout default --install'
cmd_update_RKhunter = '/usr/local/bin/rkhunter --update && /usr/local/bin/rkhunter --propupd'
cmd_run_RKhunter = 'rkhunter --check --skip-keypress'
cmd_remove_RKhunter = 'rm -rf /usr/local/bin/rkhunter && rm -rf /root/rkhunter-1.4.6*'



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