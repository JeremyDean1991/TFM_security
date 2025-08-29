


import sys
sys.path.append('../plg_CUSTOM/') 
sys.path.append('../plg_TFM/') 

from plg_SSH import * 


cmd_lsyncd_install_path = 'rpm -q --filesbypkg lsyncd'
cmd_install_lsyncd = 'yum -y install lsyncd'

cmd_install_sshclients="yum -y install openssh-clients"
cmd_rm_id_rsa='rm -f /root/.ssh/id_rsa'
cmd_ssh_keygen_create_keys='ssh-keygen -b 2048 -t rsa -f /root/.ssh/id_rsa -q -N ""'
open_lsyncd_config_file = 'cat /etc/lsyncd.conf'
open_lsyncd_config_file_1 = 'nl /etc/lsyncd.conf' #file with line numbers 



def Lsyncd_status (option):

   match option: 
   
      case "1":
         print ("Lsyncd - start")

         cmd_start_lsyncd = 'systemctl start lsyncd'
         return cmd_start_lsyncd
   
      case: "2":
         print ("Lsynd - stop")
      
         cmd_stop_lsyncd = 'systemctl stop lsyncd'
         return cmd_stop_lsyncd
         
      case: "3":
         print ("Lsynd - enable")
      
         cmd_enable_lsyncd = 'systemctl enable lsyncd'
         return cmd_enable_lsyncd
         
      
      case: "4":
         print ("Lsynd - remove")
 
         cmd_remove_lsyncd = ''
         return cmd_remove_lsyncd

