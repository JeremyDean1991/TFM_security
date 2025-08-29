import sys
import os

# Add paths for imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../../plg_SRC/a0_plg_TFM')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../../plg_SRC_CUSTOM/a0_plg_CUSTOM')))

from plg_SSH import *
from plg_CSV import *
from plg_String import *
from plg_Date_time import *

class RootKit_Hunter_TaskExecutor:
    """
    Task Executor for RootKit Hunter
    Contains the core logic for rootkit detection operations
    """
    
    def install_rootkit_hunter(self, LIST_file_path):
        """
        Install RootKit Hunter on target servers
        """
        try:
            results = []
            for server in merge_and_read_csv(LIST_file_path):
                server_ip, ssh_username, ssh_password = server_details(server)
                if server_ip:
                    ssh_client = Ssh_into_server(server_ip, ssh_username, ssh_password)
                    if ssh_client:
                        # Install RootKit Hunter
                        ssh_exec(ssh_client, "yum install -y rkhunter")
                        ssh_exec(ssh_client, "rkhunter --update")
                        results.append(f"Successfully installed RootKit Hunter on {server_ip}")
                    else:
                        results.append(f"Failed to connect to {server_ip}")
            return results
        except Exception as e:
            log2('error', f"An error occurred: {e}")
            return [f"Error: {str(e)}"]

    def run_rootkit_scan(self, LIST_file_path):
        """
        Run RootKit Hunter scan
        """
        try:
            results = []
            for server in merge_and_read_csv(LIST_file_path):
                server_ip, ssh_username, ssh_password = server_details(server)
                if server_ip:
                    ssh_client = Ssh_into_server(server_ip, ssh_username, ssh_password)
                    if ssh_client:
                        # Run scan
                        ssh_exec(ssh_client, "rkhunter --check --skip-keypress")
                        results.append(f"Successfully ran RootKit scan on {server_ip}")
                    else:
                        results.append(f"Failed to connect to {server_ip}")
            return results
        except Exception as e:
            log2('error', f"An error occurred: {e}")
            return [f"Error: {str(e)}"]

    def update_rootkit_hunter(self, LIST_file_path):
        """
        Update RootKit Hunter database
        """
        try:
            results = []
            for server in merge_and_read_csv(LIST_file_path):
                server_ip, ssh_username, ssh_password = server_details(server)
                if server_ip:
                    ssh_client = Ssh_into_server(server_ip, ssh_username, ssh_password)
                    if ssh_client:
                        # Update database
                        ssh_exec(ssh_client, "rkhunter --update")
                        results.append(f"Successfully updated RootKit Hunter on {server_ip}")
                    else:
                        results.append(f"Failed to connect to {server_ip}")
            return results
        except Exception as e:
            log2('error', f"An error occurred: {e}")
            return [f"Error: {str(e)}"]

    def configure_rootkit_hunter(self, LIST_file_path):
        """
        Configure RootKit Hunter settings
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
# RootKit Hunter Configuration
UPDATE_MIRRORS=1
MIRRORS_MODE=0
WEB_CMD=""
TMPDIR=/tmp
DBDIR=/var/lib/rkhunter/db
LOGFILE=/var/log/rkhunter.log
INSTALLDIR=/usr
SCRIPTDIR=/usr/share/rkhunter/scripts
'''
                        ssh_exec(ssh_client, f'echo "{config_content}" > /etc/rkhunter.conf.local')
                        results.append(f"Successfully configured RootKit Hunter on {server_ip}")
                    else:
                        results.append(f"Failed to connect to {server_ip}")
            return results
        except Exception as e:
            log2('error', f"An error occurred: {e}")
            return [f"Error: {str(e)}"]

    def remove_rootkit_hunter(self, LIST_file_path):
        """
        Remove RootKit Hunter from target servers
        """
        try:
            results = []
            for server in merge_and_read_csv(LIST_file_path):
                server_ip, ssh_username, ssh_password = server_details(server)
                if server_ip:
                    ssh_client = Ssh_into_server(server_ip, ssh_username, ssh_password)
                    if ssh_client:
                        # Remove package and configuration
                        ssh_exec(ssh_client, "yum remove -y rkhunter")
                        ssh_exec(ssh_client, "rm -f /etc/rkhunter.conf.local")
                        ssh_exec(ssh_client, "rm -rf /var/lib/rkhunter")
                        results.append(f"Successfully removed RootKit Hunter from {server_ip}")
                    else:
                        results.append(f"Failed to connect to {server_ip}")
            return results
        except Exception as e:
            log2('error', f"An error occurred: {e}")
            return [f"Error: {str(e)}"]

