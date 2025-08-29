
import sys
sys.path.append('../plg_CUSTOM/') 
sys.path.append('../plg_TFM/') 

from plg_SSH import * 



cmd_install_ClamAV = 'yum -y install clamav-server clamav-data clamav-update clamav-filesystem clamav clamav-scanner-systemd clamav-devel clamav-lib clamav-server-systemd'

cmd_uninstall_ClamAV = '''systemctl stop clamd@scan && systemctl disable clamd@scan
rpm -e --nodeps `rpm -aq | grep -i clamav`
'''

clamav_selinux_config="setsebool -P antivirus_can_scan_system 1 && setsebool -P clamd_use_jit 1"

clamav_config='''sed -i -e 's/^Example/#Example/' /etc/clamd.d/scan.conf
sed -i "/clamd.sock/s/^#//g" /etc/clamd.d/scan.conf
sed -i -e "s/^Example/#Example/" /etc/freshclam.conf
freshclam
'''
clamav_enable_cmd="systemctl start clamd@scan && systemctl enable clamd@scan"

clamav_scan="freshclam && clamscan -r /"

clamav_restart_cmd="systemctl restart clamd@scan"




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