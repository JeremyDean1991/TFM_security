


import sys
sys.path.append('../plg_CUSTOM/') 
sys.path.append('../plg_TFM/') 

from plg_SSH import * 


#### MariDB Galera ####
cmd_mariadb_install = "yum install -y MariaDB-server MariaDB-client galera"
cmd_mariadb_start = "systemctl start mariadb"
cmd_mariadb_stop = "systemctl stop mariadb"
cmd_mariadb_restart = "systemctl restart mariadb"
cmd_mariadb_enable = "systemctl enable mariadb"
cmd_galera_start = "galera_new_cluster"
cmd_firewalld_add_3306__tcp_port = (
    "firewall-cmd --permanent --zone=public --add-port=3306/tcp"
)
cmd_firewalld_add_4567__tcp_port = (
    "firewall-cmd --permanent --zone=public --add-port=4567/tcp"
)
cmd_firewalld_add_4568__tcp_port = (
    "firewall-cmd --permanent --zone=public --add-port=4568/tcp"
)
cmd_firewalld_add_4444__tcp_port = (
    "firewall-cmd --permanent --zone=public --add-port=4444/tcp"
)
cmd_firewalld_add_4567__udp_port = (
    "firewall-cmd --permanent --zone=public --add-port=4567/udp"
)
cmd_update_galera_node_status = (
    "sed -i 's/safe_to_bootstrap: 0/safe_to_bootstrap: 1/' /var/lib/mysql/grastate.dat"
)





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