

import sys
sys.path.append('../plg_CUSTOM/') 
sys.path.append('../plg_TFM/') 

from plg_SSH import * 


cmd_install_Fail2ban = '''yum -y install fail2ban fail2ban-systemd
yum update -y selinux-policy*
'''
cmd_configure_fail2ban = '''cp -pf /etc/fail2ban/jail.conf /etc/fail2ban/jail.local
sed -i "/#ignoreip =/s/^#//g" /etc/fail2ban/jail.local
sed -i "285i enabled = true" /etc/fail2ban/jail.local
sed -i "286i #action = firewallcmd-ipset" /etc/fail2ban/jail.local
sed -i "287i maxretry = 5" /etc/fail2ban/jail.local
sed -i "288i bantime = 86400" /etc/fail2ban/jail.local
'''
cmd_enable_fail2ban = 'systemctl enable fail2ban && systemctl start fail2ban'
cmd_remove_fail2ban = '''systemctl stop fail2ban && systemctl disable fail2ban
rpm -e --nodeps `rpm -aq | grep -i fail2ban`
'''
fail2ban_restart_cmd = 'systemctl restart fail2ban'