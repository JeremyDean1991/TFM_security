
import sys
sys.path.append('../plg_CUSTOM/') 
sys.path.append('../plg_TFM/') 

from plg_SSH import * 


#CPU
def get_specs_CPU (option):
   
   if option== "0":
      print ("CPU - General CPU specs")
      cmd_CPU_0 = 'lscpu' 
      return cmd_CPU_0
                  
   if option== "1":
      print ("CPU - Each individual cpu core specs")
      cmd_CPU_1 ='cat /proc/cpuinfo'
      return cmd_CPU_1



def get_usage_CPU (option):
   
   if option== "0":
      print ("CPU use - General CPU specs")
      cmd_CPU_use_0 = 'top -b -n1' 
      return cmd_CPU_use_0
               
   if option== "1":
      print ("CPU use - Sort CPU use")
      cmd_CPU_use_1 = 'ps -eo %cpu,comm --sort=-%mem | head -n 10'
      return cmd_CPU_use_1



def get_usage_CPU_RAM (option):
   
   if option== "0":
      print ("CPU - CPU and RAM usage")
      cmd_CPU_RAM_use_0 = 'ps -eo %cpu,%mem,comm --sort=-%mem | head -n 10' 
      return cmd_CPU_RAM_use_0
               

          
#RAM
def get_specs_RAM (option):
   
   if option== "0":
      print ("RAM - RAM list summary")
      cmd_RAM_0 = 'sudo lshw -short -C memory'
      return cmd_RAM_0
               
   if option== "1":
      print ("RAM - Full RAM specs")
      cmd_RAM_1 = 'dmidecode --type memory' 
      return cmd_RAM_1

   if option== "2":
      print ("RAM - Total memory")
      cmd_RAM_2 = 'grep MemTotal /proc/meminfo'
      return cmd_RAM_2
               
   if option== "3":
      print ("RAM - Total memory")
      cmd_RAM_3 = 'awk "'"/MemTotal/ {print $2}"'" /proc/meminfo' 
      return cmd_RAM_3



def get_usage_RAM (option):
   
   if option== "0":
      print ("RAM use - Free and used RAM")
      cmd_RAM_use_0 = 'free -h'
      return cmd_RAM_use_0
               
   if option== "1":
      print ("RAM use - TOP 10 MEMORY-CONSUMING PROCESSES")
      cmd_RAM_use_1 = 'ps -eo %mem,comm --sort=-%mem | head -n 10'
      return cmd_RAM_use_1




#Hard disk 
def get_specs_DISK (option):
   
   if option== "0":
      print ("DISK specs - Free and used RAM")
      
      cmd_DISK_0 = 'fdisk -l | grep Disk'
      return cmd_DISK_0
               
   if option== "1":
      print ("DISK specs - Disk specs summary")
      
      cmd_DISK_1 ='lshw -short -C disk'
      return cmd_DISK_1   
   
   

def get_usage_DISK (option):
   
   if option== "0":
      print ("DISK use - Free and used RAM")
      
      cmd_DISK_use_0 = 'df -H --output=source,size,used,avail'
      return cmd_DISK_use_0
               
   if option== "1":
      print ("DISK use - TOP 10 DISK-CONSUMING PROCESSES")
      
      cmd_DISK_use_1 = 'du -a /etc/ | sort -n -r | head -n 10'
      return cmd_DISK_use_1   
   
   if option== "2":
      print ("DISK use - total disk of the root directory")
      
      cmd_DISK_use_2 = 'df -h /' 
      return cmd_DISK_use_2 
   
   
   if option== "3":
      print ("DISK use - Disk specs summary")
      
      cmd_DISK_use_3 = "df -h --output='size','pcent' "
      return cmd_DISK_use_3   
   

   if option== "4":
      print ("DISK use - Disk specs summary")
      
      cmd_DISK_use_4 = 'df -h -t ext4' 
      return cmd_DISK_use_4  

 
  

#Operating system & Software
def get_specs_OS (option):
   
   if option== "0":
      print ("OS specs - Operating system specs")
      
      cmd_OS_0 = 'cat /etc/os-release'
      return cmd_OS_0
      
      
      
#Host machine
def get_specs_HOST (option):
   
   if option== "0":
      print ("HOST specs - host machine info")
      
      cmd_HOST_0 = 'hostnamectl'
      return cmd_HOST_0


#=======================================================================================
# Match is not supported by python 3.6 version so below code have been commented out  
#=======================================================================================
""" 

def get_specs_CPU (option):

   match option: 
   
      case "0":
         print ("CPU - General CPU specs")
         cmd_CPU_0 = 'lscpu' 
         return cmd_CPU_0
                  
      case "1":
         print ("CPU - Each individual cpu core specs")
         cmd_CPU_1 ='cat /proc/cpuinfo'
         return cmd_CPU_1



def get_usage_CPU (option):

   match option: 
   
      case "0":
         print ("CPU use - General CPU specs")
         cmd_CPU_use_0 = 'top -b -n1' 
         return cmd_CPU_use_0
                  
      case "1":
         print ("CPU use - Sort CPU use")
         cmd_CPU_use_1 = 'ps -eo %cpu,comm --sort=-%mem | head -n 10'
         return cmd_CPU_use_1



def get_usage_CPU_RAM (option):

   match option: 
   
      case "0":
         print ("CPU - CPU and RAM usage")
         cmd_CPU_RAM_use_0 = 'ps -eo %cpu,%mem,comm --sort=-%mem | head -n 10' 
         return cmd_CPU_RAM_use_0
                  

             
#RAM
def get_specs_RAM (option):

   match option: 
   
      case "0":
         print ("RAM - RAM list summary")
         cmd_RAM_0 = 'sudo lshw -short -C memory'
         return cmd_RAM_0
                  
      case "1":
         print ("RAM - Full RAM specs")
         cmd_RAM_1 = 'dmidecode --type memory' 
         return cmd_RAM_1

      case "2":
         print ("RAM - Total memory")
         cmd_RAM_2 = 'grep MemTotal /proc/meminfo'
         return cmd_RAM_2
                  
      case "3":
         print ("RAM - Total memory")
         cmd_RAM_3 = 'awk "'"/MemTotal/ {print $2}"'" /proc/meminfo' 
         return cmd_RAM_3



def get_usage_RAM (option):

   match option: 
   
      case "0":
         print ("RAM use - Free and used RAM")
         cmd_RAM_use_0 = 'free -h'
         return cmd_RAM_use_0
                  
      case "1":
         print ("RAM use - TOP 10 MEMORY-CONSUMING PROCESSES")
         cmd_RAM_use_1 = 'ps -eo %mem,comm --sort=-%mem | head -n 10'
         return cmd_RAM_use_1




#Hard disk 
def get_specs_DISK (option):

   match option: 
   
      case "0":
         print ("DISK specs - Free and used RAM")
         
         cmd_DISK_0 = 'fdisk -l | grep Disk'
         return cmd_DISK_0
                  
      case "1":
         print ("DISK specs - Disk specs summary")
         
         cmd_DISK_1 ='lshw -short -C disk'
         return cmd_DISK_1   
   
   

def get_usage_DISK (option):

   match option: 
   
      case "0":
         print ("DISK use - Free and used RAM")
         
         cmd_DISK_use_0 = 'df -H --output=source,size,used,avail'
         return cmd_DISK_use_0
                  
      case "1":
         print ("DISK use - TOP 10 DISK-CONSUMING PROCESSES")
         
         cmd_DISK_use_1 = 'du -a /etc/ | sort -n -r | head -n 10'
         return cmd_DISK_use_1   
   
      case "2":
         print ("DISK use - total disk of the root directory")
         
         cmd_DISK_use_2 = 'df -h /' 
         return cmd_DISK_use_2 
   
   
      case "3":
         print ("DISK use - Disk specs summary")
         
         cmd_DISK_use_3 = "df -h --output='size','pcent' "
         return cmd_DISK_use_3   
   

      case "4":
         print ("DISK use - Disk specs summary")
         
         cmd_DISK_use_4 = 'df -h -t ext4' 
         return cmd_DISK_use_4  

 
  

#Operating system & Software
def get_specs_OS (option):

   match option: 
   
      case "0":
         print ("OS specs - Operating system specs")
         
         cmd_OS_0 = 'cat /etc/os-release'
         return cmd_OS_0
         
         
         
#Host machine
def get_specs_HOST (option):

   match option: 
   
      case "0":
         print ("HOST specs - host machine info")
         
         cmd_HOST_0 = 'hostnamectl'
         return cmd_HOST_0    
         
         
"""      
         
         
#https://stackoverflow.com/questions/62656579/why-im-getting-unicodeencodeerror-charmap-codec-cant-encode-character-u2 
def test ():  
  
   client1 = SSH_into_server (server_ip='173.208.150.146', SSH_username='root', SSH_password='V999zje4kksp!')  
   #_stdin_1, _stdout_1,_stderr_1 = client1.exec_command(test_print (msg1="man", msg2=" fuck"))
   
   _stdin_1, _stdout_1,_stderr_1 = client1.exec_command(get_filesystem_space(option="2"))
   _stdin_2, _stdout_2,_stderr_2 = client1.exec_command("lsblk")

   #encoding = locale.getpreferredencoding()

   print(_stdout_1.read().decode())
   print ('\n')
   #print(_stdout_2.read().decode(encoding))
   print(_stdout_2.read().decode('ascii', 'ignore'))

   client1.close()
   
#test()         