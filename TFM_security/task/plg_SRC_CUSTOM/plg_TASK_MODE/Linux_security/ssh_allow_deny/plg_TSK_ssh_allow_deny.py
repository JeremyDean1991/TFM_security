import sys
import os

# Add paths for imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../../plg_SRC/a0_plg_TFM')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../../plg_SRC_CUSTOM/a0_plg_CUSTOM')))

from plg_SSH import *
from plg_CSV import *
from plg_String import *
from plg_Date_time import *

class SSH_AllowDeny_TaskExecutor:
    """
    Task Executor for SSH allow/deny security operations
    """
    
    def __init__(self):
        pass
    
    def setup_ssh_allow_deny_hosts(self, LIST_file_path):
        """
        Main function to setup SSH allow/deny hosts configuration
        """
        log2('info', 'Setting up SSH allow/deny hosts configuration')
        try:
            results = []
            for server in merge_and_read_csv(LIST_file_path):
                server_ip, ssh_username, ssh_password = server_details(server)
                if server_ip:
                    try:
                        ssh_client = Ssh_into_server(server_ip, ssh_username, ssh_password)
                        if ssh_client:
                            # Create basic SSH configuration
                            ssh_exec(ssh_client, "echo 'sshd: 127.0.0.1' > /etc/hosts.allow")
                            ssh_exec(ssh_client, "echo 'sshd: ALL' > /etc/hosts.deny")
                            ssh_exec(ssh_client, "systemctl restart sshd")
                            
                            results.append(f"SSH allow/deny configuration setup on {server_ip}")
                            log2('info', f"SSH allow/deny configuration setup on {server_ip}")
                        else:
                            results.append(f"Failed to SSH into {server_ip}")
                    except Exception as e:
                        results.append(f"Error setting up SSH config on {server_ip}: {str(e)}")
            
            return results
        except Exception as e:
            log2('error', f"An error occurred in setup_ssh_allow_deny_hosts: {e}")
            return [f"Error: {str(e)}"]
    
    def modify_ssh_allow_deny_hosts(self, LIST_file_path):
        """
        Main function to modify SSH allow/deny hosts configuration
        """
        log2('info', 'Modifying SSH allow/deny hosts configuration')
        try:
            results = []
            for server in merge_and_read_csv(LIST_file_path):
                server_ip, ssh_username, ssh_password = server_details(server)
                if server_ip:
                    try:
                        ssh_client = Ssh_into_server(server_ip, ssh_username, ssh_password)
                        if ssh_client:
                            # Update SSH configuration
                            ssh_exec(ssh_client, "systemctl restart sshd")
                            
                            results.append(f"SSH allow/deny configuration modified on {server_ip}")
                            log2('info', f"SSH allow/deny configuration modified on {server_ip}")
                        else:
                            results.append(f"Failed to connect to {server_ip}")
                    except Exception as e:
                        results.append(f"Error modifying SSH config on {server_ip}: {str(e)}")
            
            return results
        except Exception as e:
            log2('error', f"An error occurred in modify_ssh_allow_deny_hosts: {e}")
            return [f"Error: {str(e)}"]
    
    def add_allowed_host(self, LIST_file_path, allowed_host):
        """
        Main function to add an allowed host
        """
        log2('info', f'Adding allowed host: {allowed_host}')
        try:
            results = []
            for server in merge_and_read_csv(LIST_file_path):
                server_ip, ssh_username, ssh_password = server_details(server)
                if server_ip:
                    try:
                        ssh_client = Ssh_into_server(server_ip, ssh_username, ssh_password)
                        if ssh_client:
                            ssh_exec(ssh_client, f"echo 'sshd: {allowed_host}' >> /etc/hosts.allow")
                            ssh_exec(ssh_client, "systemctl restart sshd")
                            
                            results.append(f"Added {allowed_host} to allowed hosts on {server_ip}")
                            log2('info', f"Added {allowed_host} to allowed hosts on {server_ip}")
                        else:
                            results.append(f"Failed to connect to {server_ip}")
                    except Exception as e:
                        results.append(f"Error adding allowed host on {server_ip}: {str(e)}")
            
            return results
        except Exception as e:
            log2('error', f"An error occurred in add_allowed_host: {e}")
            return [f"Error: {str(e)}"]
    
    def remove_allowed_host(self, LIST_file_path, host_to_remove):
        """
        Main function to remove an allowed host
        """
        log2('info', f'Removing allowed host: {host_to_remove}')
        try:
            results = []
            for server in merge_and_read_csv(LIST_file_path):
                server_ip, ssh_username, ssh_password = server_details(server)
                if server_ip:
                    try:
                        ssh_client = Ssh_into_server(server_ip, ssh_username, ssh_password)
                        if ssh_client:
                            ssh_exec(ssh_client, f"sed -i '/{host_to_remove}/d' /etc/hosts.allow")
                            ssh_exec(ssh_client, "systemctl restart sshd")
                            
                            results.append(f"Removed {host_to_remove} from allowed hosts on {server_ip}")
                            log2('info', f"Removed {host_to_remove} from allowed hosts on {server_ip}")
                        else:
                            results.append(f"Failed to connect to {server_ip}")
                    except Exception as e:
                        results.append(f"Error removing allowed host on {server_ip}: {str(e)}")
            
            return results
        except Exception as e:
            log2('error', f"An error occurred in remove_allowed_host: {e}")
            return [f"Error: {str(e)}"]
    
    def add_denied_host(self, LIST_file_path, denied_host):
        """
        Main function to add a denied host
        """
        log2('info', f'Adding denied host: {denied_host}')
        try:
            results = []
            for server in merge_and_read_csv(LIST_file_path):
                server_ip, ssh_username, ssh_password = server_details(server)
                if server_ip:
                    try:
                        ssh_client = Ssh_into_server(server_ip, ssh_username, ssh_password)
                        if ssh_client:
                            ssh_exec(ssh_client, f"echo 'sshd: {denied_host}' >> /etc/hosts.deny")
                            ssh_exec(ssh_client, "systemctl restart sshd")
                            
                            results.append(f"Added {denied_host} to denied hosts on {server_ip}")
                            log2('info', f"Added {denied_host} to denied hosts on {server_ip}")
                        else:
                            results.append(f"Failed to connect to {server_ip}")
                    except Exception as e:
                        results.append(f"Error adding denied host on {server_ip}: {str(e)}")
            
            return results
        except Exception as e:
            log2('error', f"An error occurred in add_denied_host: {e}")
            return [f"Error: {str(e)}"]
    
    def remove_denied_host(self, LIST_file_path, host_to_remove):
        """
        Main function to remove a denied host
        """
        log2('info', f'Removing denied host: {host_to_remove}')
        try:
            results = []
            for server in merge_and_read_csv(LIST_file_path):
                server_ip, ssh_username, ssh_password = server_details(server)
                if server_ip:
                    try:
                        ssh_client = Ssh_into_server(server_ip, ssh_username, ssh_password)
                        if ssh_client:
                            ssh_exec(ssh_client, f"sed -i '/{host_to_remove}/d' /etc/hosts.deny")
                            ssh_exec(ssh_client, "systemctl restart sshd")
                            
                            results.append(f"Removed {host_to_remove} from denied hosts on {server_ip}")
                            log2('info', f"Removed {host_to_remove} from denied hosts on {server_ip}")
                        else:
                            results.append(f"Failed to connect to {server_ip}")
                    except Exception as e:
                        results.append(f"Error removing denied host on {server_ip}: {str(e)}")
            
            return results
        except Exception as e:
            log2('error', f"An error occurred in remove_denied_host: {e}")
            return [f"Error: {str(e)}"]
