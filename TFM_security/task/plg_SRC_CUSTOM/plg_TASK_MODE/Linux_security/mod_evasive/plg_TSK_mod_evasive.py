import sys
import os

# Add paths for imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../../plg_SRC/a0_plg_TFM')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../../plg_SRC_CUSTOM/a0_plg_CUSTOM')))

from plg_SSH import *
from plg_CSV import *
from plg_String import *
from plg_Date_time import *

class ModEvasive_TaskExecutor:
    """
    Task Executor for ModEvasive DDoS protection
    Contains the core logic for ModEvasive operations
    """
    
    def install_mod_evasive(self, LIST_file_path):
        """
        Install ModEvasive on target servers
        """
        try:
            results = []
            for server in merge_and_read_csv(LIST_file_path):
                server_ip, ssh_username, ssh_password = server_details(server)
                if server_ip:
                    ssh_client = Ssh_into_server(server_ip, ssh_username, ssh_password)
                    if ssh_client:
                        # Install ModEvasive
                        ssh_exec(ssh_client, "yum install -y mod_evasive")
                        ssh_exec(ssh_client, "systemctl restart httpd")
                        results.append(f"Successfully installed ModEvasive on {server_ip}")
                    else:
                        results.append(f"Failed to connect to {server_ip}")
            return results
        except Exception as e:
            log2('error', f"An error occurred: {e}")
            return [f"Error: {str(e)}"]

    def configure_mod_evasive(self, LIST_file_path):
        """
        Configure ModEvasive settings
        """
        try:
            results = []
            for server in merge_and_read_csv(LIST_file_path):
                server_ip, ssh_username, ssh_password = server_details(server)
                if server_ip:
                    ssh_client = Ssh_into_server(server_ip, ssh_username, ssh_password)
                    if ssh_client:
                        # Create custom configuration
                        config_content = '''
<IfModule mod_evasive20.c>
    DOSHashTableSize    3097
    DOSPageCount        2
    DOSSiteCount        50
    DOSPageInterval     1
    DOSSiteInterval     1
    DOSBlockingPeriod   10
</IfModule>
'''
                        ssh_exec(ssh_client, f'echo "{config_content}" > /etc/httpd/conf.d/mod_evasive.conf')
                        ssh_exec(ssh_client, "systemctl restart httpd")
                        results.append(f"Successfully configured ModEvasive on {server_ip}")
                    else:
                        results.append(f"Failed to connect to {server_ip}")
            return results
        except Exception as e:
            log2('error', f"An error occurred: {e}")
            return [f"Error: {str(e)}"]

    def enable_mod_evasive(self, LIST_file_path):
        """
        Enable ModEvasive protection
        """
        try:
            results = []
            for server in merge_and_read_csv(LIST_file_path):
                server_ip, ssh_username, ssh_password = server_details(server)
                if server_ip:
                    ssh_client = Ssh_into_server(server_ip, ssh_username, ssh_password)
                    if ssh_client:
                        # Ensure module is loaded
                        ssh_exec(ssh_client, "echo 'LoadModule evasive20_module modules/mod_evasive20.so' >> /etc/httpd/conf/httpd.conf")
                        ssh_exec(ssh_client, "systemctl restart httpd")
                        results.append(f"Successfully enabled ModEvasive on {server_ip}")
                    else:
                        results.append(f"Failed to connect to {server_ip}")
            return results
        except Exception as e:
            log2('error', f"An error occurred: {e}")
            return [f"Error: {str(e)}"]

    def disable_mod_evasive(self, LIST_file_path):
        """
        Disable ModEvasive protection
        """
        try:
            results = []
            for server in merge_and_read_csv(LIST_file_path):
                server_ip, ssh_username, ssh_password = server_details(server)
                if server_ip:
                    ssh_client = Ssh_into_server(server_ip, ssh_username, ssh_password)
                    if ssh_client:
                        # Comment out module loading
                        ssh_exec(ssh_client, "sed -i 's/LoadModule evasive20_module/#LoadModule evasive20_module/' /etc/httpd/conf/httpd.conf")
                        ssh_exec(ssh_client, "systemctl restart httpd")
                        results.append(f"Successfully disabled ModEvasive on {server_ip}")
                    else:
                        results.append(f"Failed to connect to {server_ip}")
            return results
        except Exception as e:
            log2('error', f"An error occurred: {e}")
            return [f"Error: {str(e)}"]

    def remove_mod_evasive(self, LIST_file_path):
        """
        Remove ModEvasive from target servers
        """
        try:
            results = []
            for server in merge_and_read_csv(LIST_file_path):
                server_ip, ssh_username, ssh_password = server_details(server)
                if server_ip:
                    ssh_client = Ssh_into_server(server_ip, ssh_username, ssh_password)
                    if ssh_client:
                        # Remove package and configuration
                        ssh_exec(ssh_client, "yum remove -y mod_evasive")
                        ssh_exec(ssh_client, "rm -f /etc/httpd/conf.d/mod_evasive.conf")
                        ssh_exec(ssh_client, "sed -i '/LoadModule evasive20_module/d' /etc/httpd/conf/httpd.conf")
                        ssh_exec(ssh_client, "systemctl restart httpd")
                        results.append(f"Successfully removed ModEvasive from {server_ip}")
                    else:
                        results.append(f"Failed to connect to {server_ip}")
            return results
        except Exception as e:
            log2('error', f"An error occurred: {e}")
            return [f"Error: {str(e)}"]
