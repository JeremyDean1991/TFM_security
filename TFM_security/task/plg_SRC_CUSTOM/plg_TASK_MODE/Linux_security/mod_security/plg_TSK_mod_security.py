import sys
import os

# Add paths for imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../../plg_SRC/a0_plg_TFM')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../../plg_SRC_CUSTOM/a0_plg_CUSTOM')))

from plg_SSH import *
from plg_CSV import *
from plg_String import *
from plg_Date_time import *

class ModSecurity_TaskExecutor:
    """
    Task Executor for ModSecurity operations
    Contains the single function that performs ModSecurity tasks
    """
    
    def __init__(self):
        pass
    
    def setup_and_configure_modsecurity(self, LIST_file_path):
        """
        Main function to setup and configure ModSecurity
        """
        log2('info', 'Setting up and configuring ModSecurity')
        try:
            results = []
            for server in merge_and_read_csv(LIST_file_path):
                server_ip, ssh_username, ssh_password = server_details(server)
                if server_ip:
                    try:
                        ssh_client = Ssh_into_server(server_ip, ssh_username, ssh_password)
                        if ssh_client:
                            # Install ModSecurity
                            ssh_exec(ssh_client, "yum install -y mod_security")
                            
                            # Configure ModSecurity
                            ssh_exec(ssh_client, "cp /etc/httpd/conf.d/mod_security.conf /etc/httpd/conf.d/mod_security.conf.backup")
                            ssh_exec(ssh_client, "echo 'SecRuleEngine On' > /etc/httpd/conf.d/mod_security.conf")
                            ssh_exec(ssh_client, "echo 'SecRequestBodyAccess On' >> /etc/httpd/conf.d/mod_security.conf")
                            
                            # Restart Apache
                            ssh_exec(ssh_client, "systemctl restart httpd")
                            
                            results.append(f"ModSecurity setup on {server_ip}")
                            log2('info', f"ModSecurity setup on {server_ip}")
                        else:
                            results.append(f"Failed to SSH into {server_ip}")
                    except Exception as e:
                        results.append(f"Error setting up ModSecurity on {server_ip}: {str(e)}")
            
            return results
        except Exception as e:
            log2('error', f"An error occurred in setup_and_configure_modsecurity: {e}")
            return [f"Error: {str(e)}"]
    
    def remove_modsecurity(self, LIST_file_path):
        """
        Main function to remove ModSecurity
        """
        log2('info', 'Removing ModSecurity')
        try:
            results = []
            for server in merge_and_read_csv(LIST_file_path):
                server_ip, ssh_username, ssh_password = server_details(server)
                if server_ip:
                    try:
                        ssh_client = Ssh_into_server(server_ip, ssh_username, ssh_password)
                        if ssh_client:
                            ssh_exec(ssh_client, "yum remove -y mod_security")
                            ssh_exec(ssh_client, "rm -f /etc/httpd/conf.d/mod_security.conf")
                            ssh_exec(ssh_client, "systemctl restart httpd")
                            
                            results.append(f"ModSecurity removed from {server_ip}")
                            log2('info', f"ModSecurity removed from {server_ip}")
                        else:
                            results.append(f"Failed to SSH into {server_ip}")
                    except Exception as e:
                        results.append(f"Error removing ModSecurity from {server_ip}: {str(e)}")
            
            return results
        except Exception as e:
            log2('error', f"An error occurred in remove_modsecurity: {e}")
            return [f"Error: {str(e)}"]
    
    def enable_modsecurity(self, LIST_file_path):
        """
        Main function to enable ModSecurity
        """
        log2('info', 'Enabling ModSecurity')
        try:
            results = []
            for server in merge_and_read_csv(LIST_file_path):
                server_ip, ssh_username, ssh_password = server_details(server)
                if server_ip:
                    try:
                        ssh_client = Ssh_into_server(server_ip, ssh_username, ssh_password)
                        if ssh_client:
                            ssh_exec(ssh_client, "echo 'SecRuleEngine On' > /etc/httpd/conf.d/mod_security.conf")
                            ssh_exec(ssh_client, "systemctl restart httpd")
                            
                            results.append(f"ModSecurity enabled on {server_ip}")
                            log2('info', f"ModSecurity enabled on {server_ip}")
                        else:
                            results.append(f"Failed to SSH into {server_ip}")
                    except Exception as e:
                        results.append(f"Error enabling ModSecurity on {server_ip}: {str(e)}")
            
            return results
        except Exception as e:
            log2('error', f"An error occurred in enable_modsecurity: {e}")
            return [f"Error: {str(e)}"]
    
    def disable_modsecurity(self, LIST_file_path):
        """
        Main function to disable ModSecurity
        """
        log2('info', 'Disabling ModSecurity')
        try:
            results = []
            for server in merge_and_read_csv(LIST_file_path):
                server_ip, ssh_username, ssh_password = server_details(server)
                if server_ip:
                    try:
                        ssh_client = Ssh_into_server(server_ip, ssh_username, ssh_password)
                        if ssh_client:
                            ssh_exec(ssh_client, "echo 'SecRuleEngine Off' > /etc/httpd/conf.d/mod_security.conf")
                            ssh_exec(ssh_client, "systemctl restart httpd")
                            
                            results.append(f"ModSecurity disabled on {server_ip}")
                            log2('info', f"ModSecurity disabled on {server_ip}")
                        else:
                            results.append(f"Failed to SSH into {server_ip}")
                    except Exception as e:
                        results.append(f"Error disabling ModSecurity on {server_ip}: {str(e)}")
            
            return results
        except Exception as e:
            log2('error', f"An error occurred in disable_modsecurity: {e}")
            return [f"Error: {str(e)}"]

