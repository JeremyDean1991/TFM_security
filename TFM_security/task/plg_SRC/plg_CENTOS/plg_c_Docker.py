


import sys
sys.path.append('../plg_CUSTOM/') 
sys.path.append('../plg_TFM/') 

from plg_SSH import * 


cmd_Docker_install_path = 'rpm -q --filesbypkg docker' #this may not work in some situtations 


#Check if docker is installed, if so update it 
cmd_check_install_or_update_docker = ''' if [ -x "$(command -v docker)" ]; then
    echo "Update docker"
    # command
else
    echo "Install docker"
    # command
fi '''


cmd_remove_docker = '''yum remove docker \
                  docker-client \
                  docker-client-latest \
                  docker-common \
                  docker-latest \
                  docker-latest-logrotate \
                  docker-logrotate \
                  docker-engine'''


# Multi-line bash script 
cmd_Docker_running_or_not = '''if curl -s --unix-socket /var/run/docker.sock http/_ping 2>&1 >/dev/null
then
  echo "Running"
else
  echo "NOT running"
fi '''

cmd_Docker_status = 'systemctl status docker' #To check if Docker engine is running 
cmd_start_docker_engine = 'systemctl start docker'
cmd_docker_version = 'docker version'


# ####################### Docker compose ####################################
cmd_docker_compose_version = 'docker-compose version'

cmd_install_docker_compose = ''


cmd_stop_docker_compose ='docker-compose stop'
cmd_start_docker_compose = 'docker-compose up -d'




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