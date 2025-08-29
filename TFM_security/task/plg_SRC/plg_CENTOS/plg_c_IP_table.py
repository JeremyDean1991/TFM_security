

import sys
sys.path.append('../plg_CUSTOM/') 
sys.path.append('../plg_TFM/') 

from plg_SSH import * 


# iptables is a command not service. So, it will not provide the start, stop, status, etc... options.
# We can just enable/disable the firewall by using 'ufw' command

iptables_install="$SUDO $INSTALLER -y install iptables iptables-persistent"
ufw_install_for_centos_1="$SUDO $INSTALLER -y install epel-release"
ufw_install="$SUDO $INSTALLER -y install ufw"


# https://unix.stackexchange.com/questions/591038/how-to-check-iptables-status-in-centos-7-6
def get_IPtables (option):

   match option:

      case "1":
         print ("Iptables - version") 
         
         iptables_version="iptables -V"
         return iptables_version

      case "2":  
         print ("Iptables - status") 
         
         iptables_ufw_iptables_status="$SUDO ufw status"
         return iptables_ufw_iptables_status
   


def Iptables_enable_or_disable (option):   
     
     case "1":  
         print ("Iptables - enable")  
         
         iptables_ufw_iptables_enable="$SUDO ufw --force enable"
         return iptables_ufw_iptables_enable
   
      case "2"  
        print ("Iptables - disable")  
               
         iptables_ufw_iptables_disable="$SUDO ufw disable"
         return iptables_ufw_iptables_disable