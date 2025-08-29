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

class Fail2ban_TaskExecutor:
    """
    Task Executor for Fail2ban security operations
    Contains the single function that performs Fail2ban tasks
    """
    
    def __init__(self):
        pass
    
    def setup_and_configure_fail2ban(self, LIST_file_path):
        """
        Main function to setup and configure Fail2ban on target servers
        """
        log2('info', 'Setting up and configuring Fail2ban')
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
                            
                            # Install Fail2ban
                            ssh_exec(ssh_client, cmd_install_fail2ban)
                            
                            # Configure Fail2ban
                            ssh_exec(ssh_client, fail2ban_config)
                            
                            # Start and enable Fail2ban service
                            ssh_exec(ssh_client, fail2ban_start_cmd)
                            ssh_exec(ssh_client, fail2ban_enable_cmd)
                            
                            results.append(f"Successfully configured Fail2ban on {server_ip}")
                            log2('info', f"Fail2ban configured successfully on {server_ip}")
                        else:
                            results.append(f"Failed to SSH into {server_ip}")
                            log2('error', f"Failed to SSH into {server_ip}")
                    except Exception as e:
                        results.append(f"Error configuring Fail2ban on {server_ip}: {str(e)}")
                        log2('error', f"Error configuring Fail2ban on {server_ip}: {str(e)}")
            
            return results
        except Exception as e:
            log2('error', f"An error occurred in setup_and_configure_fail2ban: {e}")
            return [f"Error: {str(e)}"]
    
    def modify_fail2ban_config(self, LIST_file_path):
        """
        Main function to modify Fail2ban configuration
        """
        log2('info', 'Modifying Fail2ban configuration')
        try:
            results = []
            for server in merge_and_read_csv(LIST_file_path):
                server_ip, ssh_username, ssh_password = server_details(server)
                if server_ip:
                    try:
                        ssh_client = Ssh_into_server(server_ip, ssh_username, ssh_password)
                        sftp = SSH_into_server_transport(server_ip, ssh_username, ssh_password)
                        if ssh_client and sftp:
                            filename = "/etc/fail2ban/jail.local"
                            
                            with sftp.open(filename, 'w') as file:
                                config_content = """[DEFAULT]
bantime = 3600
findtime = 600
maxretry = 3

[sshd]
enabled = true
port = ssh
filter = sshd
logpath = /var/log/auth.log
maxretry = 3
bantime = 3600"""
                                file.write(config_content.encode())
                            
                            ssh_exec(ssh_client, fail2ban_reload_cmd)
                            results.append(f"Configuration modified successfully on {server_ip}")
                            log2('info', f"Fail2ban configuration modified on {server_ip}")
                        else:
                            results.append(f"Failed to connect to {server_ip}")
                    except Exception as e:
                        results.append(f"Error modifying config on {server_ip}: {str(e)}")
            
            return results
        except Exception as e:
            log2('error', f"An error occurred in modify_fail2ban_config: {e}")
            return [f"Error: {str(e)}"]
    
    def remove_fail2ban(self, LIST_file_path):
        """
        Main function to remove Fail2ban
        """
        log2('info', 'Removing Fail2ban')
        try:
            results = []
            for server in merge_and_read_csv(LIST_file_path):
                server_ip, ssh_username, ssh_password = server_details(server)
                if server_ip:
                    try:
                        ssh_client = Ssh_into_server(server_ip, ssh_username, ssh_password)
                        if ssh_client:
                            ssh_exec(ssh_client, cmd_uninstall_fail2ban)
                            results.append(f"Fail2ban removed from {server_ip}")
                            log2('info', f"Fail2ban removed from {server_ip}")
                        else:
                            results.append(f"Failed to SSH into {server_ip}")
                    except Exception as e:
                        results.append(f"Error removing Fail2ban from {server_ip}: {str(e)}")
            
            return results
        except Exception as e:
            log2('error', f"An error occurred in remove_fail2ban: {e}")
            return [f"Error: {str(e)}"]
    
    def start_fail2ban(self, LIST_file_path):
        """
        Main function to start Fail2ban service
        """
        log2('info', 'Starting Fail2ban service')
        try:
            results = []
            for server in merge_and_read_csv(LIST_file_path):
                server_ip, ssh_username, ssh_password = server_details(server)
                if server_ip:
                    try:
                        ssh_client = Ssh_into_server(server_ip, ssh_username, ssh_password)
                        if ssh_client:
                            ssh_exec(ssh_client, fail2ban_start_cmd)
                            results.append(f"Fail2ban started on {server_ip}")
                            log2('info', f"Fail2ban started on {server_ip}")
                        else:
                            results.append(f"Failed to SSH into {server_ip}")
                    except Exception as e:
                        results.append(f"Error starting Fail2ban on {server_ip}: {str(e)}")
            
            return results
        except Exception as e:
            log2('error', f"An error occurred in start_fail2ban: {e}")
            return [f"Error: {str(e)}"]
    
    def stop_fail2ban(self, LIST_file_path):
        """
        Main function to stop Fail2ban service
        """
        log2('info', 'Stopping Fail2ban service')
        try:
            results = []
            for server in merge_and_read_csv(LIST_file_path):
                server_ip, ssh_username, ssh_password = server_details(server)
                if server_ip:
                    try:
                        ssh_client = Ssh_into_server(server_ip, ssh_username, ssh_password)
                        if ssh_client:
                            ssh_exec(ssh_client, fail2ban_stop_cmd)
                            results.append(f"Fail2ban stopped on {server_ip}")
                            log2('info', f"Fail2ban stopped on {server_ip}")
                        else:
                            results.append(f"Failed to SSH into {server_ip}")
                    except Exception as e:
                        results.append(f"Error stopping Fail2ban on {server_ip}: {str(e)}")
            
            return results
        except Exception as e:
            log2('error', f"An error occurred in stop_fail2ban: {e}")
            return [f"Error: {str(e)}"]
    
    def restart_fail2ban(self, LIST_file_path):
        """
        Main function to restart Fail2ban service
        """
        log2('info', 'Restarting Fail2ban service')
        try:
            results = []
            for server in merge_and_read_csv(LIST_file_path):
                server_ip, ssh_username, ssh_password = server_details(server)
                if server_ip:
                    try:
                        ssh_client = Ssh_into_server(server_ip, ssh_username, ssh_password)
                        if ssh_client:
                            ssh_exec(ssh_client, fail2ban_restart_cmd)
                            results.append(f"Fail2ban restarted on {server_ip}")
                            log2('info', f"Fail2ban restarted on {server_ip}")
                        else:
                            results.append(f"Failed to SSH into {server_ip}")
                    except Exception as e:
                        results.append(f"Error restarting Fail2ban on {server_ip}: {str(e)}")
            
            return results
        except Exception as e:
            log2('error', f"An error occurred in restart_fail2ban: {e}")
            return [f"Error: {str(e)}"]

