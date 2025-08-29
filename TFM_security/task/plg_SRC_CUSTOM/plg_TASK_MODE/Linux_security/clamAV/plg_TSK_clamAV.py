import sys
import os

# Add paths for imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../../plg_SRC/a0_plg_TFM')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../../plg_SRC_CUSTOM/a0_plg_CUSTOM')))

from plg_SSH import *
from plg_CSV import *
from plg_String import *
from plg_Date_time import *
from plg_cmd_CENTOS import *
from plg_cmd_UBUNTU import *

class ClamAV_TaskExecutor:
    """
    Task Executor for ClamAV security operations
    Contains the single function that performs ClamAV tasks
    """
    
    def __init__(self):
        pass
    
    def setup_and_configure_clamav(self, LIST_file_path):
        """
        Main function to setup and configure ClamAV on target servers
        This is the single function that gets called by the TM
        """
        log2('info', 'Setting up and configuring ClamAV')
        try:
            results = []
            for server in merge_and_read_csv(LIST_file_path):
                server_ip, ssh_username, ssh_password = server_details(server)
                if server_ip:
                    try:
                        ssh_client = Ssh_into_server(server_ip, ssh_username, ssh_password)
                        if ssh_client:
                            # Install EPEL release first
                            ssh_exec(ssh_client, cmd_install_epel_release)
                            
                            # Install ClamAV
                            ssh_exec(ssh_client, cmd_install_ClamAV)
                            
                            # Configure ClamAV SELinux
                            ssh_exec(ssh_client, clamav_selinux_config)
                            
                            # Configure ClamAV
                            ssh_exec(ssh_client, clamav_config)
                            
                            # Enable ClamAV service
                            ssh_exec(ssh_client, clamav_enable_cmd)
                            
                            results.append(f"Successfully configured ClamAV on {server_ip}")
                            log2('info', f"ClamAV configured successfully on {server_ip}")
                        else:
                            results.append(f"Failed to SSH into {server_ip}")
                            log2('error', f"Failed to SSH into {server_ip}")
                    except Exception as e:
                        results.append(f"Error configuring ClamAV on {server_ip}: {str(e)}")
                        log2('error', f"Error configuring ClamAV on {server_ip}: {str(e)}")
            
            return results
        except Exception as e:
            log2('error', f"An error occurred in setup_and_configure_clamav: {e}")
            return [f"Error: {str(e)}"]
    
    def modify_clamav_config(self, LIST_file_path):
        """
        Main function to modify ClamAV configuration
        """
        log2('info', 'Modifying ClamAV configuration')
        try:
            results = []
            for server in merge_and_read_csv(LIST_file_path):
                server_ip, ssh_username, ssh_password = server_details(server)
                if server_ip:
                    try:
                        ssh_client = Ssh_into_server(server_ip, ssh_username, ssh_password)
                        sftp = SSH_into_server_transport(server_ip, ssh_username, ssh_password)
                        if ssh_client and sftp:
                            filename = "/etc/clamd.d/scan.conf"
                            
                            with sftp.open(filename, 'r+') as file:
                                contents = file.read()
                                contents = contents.replace(b"Example", b"#Example")
                                contents = contents.replace(b"#LogFileMaxSize 2M", b"LogFileMaxSize 5M")
                                contents = contents.replace(b"#LogTime yes", b"LogTime yes")
                                contents = contents.replace(b"#LogRotate yes", b"LogRotate yes")
                                file.seek(0)
                                file.write(contents)
                            
                            ssh_exec(ssh_client, clamav_restart_cmd)
                            results.append(f"Configuration modified successfully on {server_ip}")
                            log2('info', f"ClamAV configuration modified on {server_ip}")
                        else:
                            results.append(f"Failed to connect to {server_ip}")
                    except Exception as e:
                        results.append(f"Error modifying config on {server_ip}: {str(e)}")
            
            return results
        except Exception as e:
            log2('error', f"An error occurred in modify_clamav_config: {e}")
            return [f"Error: {str(e)}"]
    
    def stop_clamav(self, LIST_file_path):
        """
        Main function to stop ClamAV service
        """
        log2('info', 'Stopping ClamAV service')
        try:
            results = []
            for server in merge_and_read_csv(LIST_file_path):
                server_ip, ssh_username, ssh_password = server_details(server)
                if server_ip:
                    try:
                        ssh_client = Ssh_into_server(server_ip, ssh_username, ssh_password)
                        if ssh_client:
                            ssh_exec(ssh_client, cmd_stop_ClamAV)
                            results.append(f"ClamAV stopped on {server_ip}")
                            log2('info', f"ClamAV stopped on {server_ip}")
                        else:
                            results.append(f"Failed to SSH into {server_ip}")
                    except Exception as e:
                        results.append(f"Error stopping ClamAV on {server_ip}: {str(e)}")
            
            return results
        except Exception as e:
            log2('error', f"An error occurred in stop_clamav: {e}")
            return [f"Error: {str(e)}"]
    
    def remove_clamav(self, LIST_file_path):
        """
        Main function to remove ClamAV
        """
        log2('info', 'Removing ClamAV')
        try:
            results = []
            for server in merge_and_read_csv(LIST_file_path):
                server_ip, ssh_username, ssh_password = server_details(server)
                if server_ip:
                    try:
                        ssh_client = Ssh_into_server(server_ip, ssh_username, ssh_password)
                        if ssh_client:
                            ssh_exec(ssh_client, cmd_uninstall_ClamAV)
                            results.append(f"ClamAV removed from {server_ip}")
                            log2('info', f"ClamAV removed from {server_ip}")
                        else:
                            results.append(f"Failed to SSH into {server_ip}")
                    except Exception as e:
                        results.append(f"Error removing ClamAV from {server_ip}: {str(e)}")
            
            return results
        except Exception as e:
            log2('error', f"An error occurred in remove_clamav: {e}")
            return [f"Error: {str(e)}"]
    
    def start_clamav_scan(self, LIST_file_path):
        """
        Main function to start ClamAV virus scan
        """
        log2('info', 'Starting ClamAV virus scan')
        try:
            results = []
            for server in merge_and_read_csv(LIST_file_path):
                server_ip, ssh_username, ssh_password = server_details(server)
                if server_ip:
                    try:
                        ssh_client = Ssh_into_server(server_ip, ssh_username, ssh_password)
                        if ssh_client:
                            ssh_exec(ssh_client, clamav_scan)
                            results.append(f"ClamAV scan started on {server_ip}")
                            log2('info', f"ClamAV scan started on {server_ip}")
                        else:
                            results.append(f"Failed to SSH into {server_ip}")
                    except Exception as e:
                        results.append(f"Error starting scan on {server_ip}: {str(e)}")
            
            return results
        except Exception as e:
            log2('error', f"An error occurred in start_clamav_scan: {e}")
            return [f"Error: {str(e)}"]
    
    def enable_clamav(self, LIST_file_path):
        """
        Main function to enable ClamAV service
        """
        log2('info', 'Enabling ClamAV service')
        try:
            results = []
            for server in merge_and_read_csv(LIST_file_path):
                server_ip, ssh_username, ssh_password = server_details(server)
                if server_ip:
                    try:
                        ssh_client = Ssh_into_server(server_ip, ssh_username, ssh_password)
                        if ssh_client:
                            ssh_exec(ssh_client, clamav_enable_cmd)
                            results.append(f"ClamAV enabled on {server_ip}")
                            log2('info', f"ClamAV enabled on {server_ip}")
                        else:
                            results.append(f"Failed to SSH into {server_ip}")
                    except Exception as e:
                        results.append(f"Error enabling ClamAV on {server_ip}: {str(e)}")
            
            return results
        except Exception as e:
            log2('error', f"An error occurred in enable_clamav: {e}")
            return [f"Error: {str(e)}"]

