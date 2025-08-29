

import sys
sys.path.append('../plg_CUSTOM/') 
sys.path.append('../plg_TFM/') 

from plg_SSH import * 


######Apache########
cmd_httpd_install = "yum install -y httpd"
cmd_httpd_stop = "systemctl stop httpd"
cmd_httpd_enable = "systemctl enable --now httpd; systemctl start httpd"
cmd_http_firewall = "firewall-cmd --permanent --zone=public --add-service=http"
cmd_https_firewall = "firewall-cmd --permanent --zone=public --add-service=https"
cmd_php_chown = "chown -R root:apache /var/lib/php/*"
cmd_restart_php = "systemctl restart php-fpm.service"
cmd_install_epel = "yum install -y epel-release yum-utils"
cmd_install_remi = (
    "yum -y install https://rpms.remirepo.net/enterprise/remi-release-7.rpm"
)
cmd_remi_disable = "yum-config-manager --disable remi-php54"
cmd_remi_enable = "yum-config-manager --enable remi-php74"
cmd_install_php_tools = "yum -y update && yum -y install php-fpm php-cli php-gd php-opcache php-mysqlnd php-json php-mcrypt php-xml php-curl mod_php"











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