import sys
import os

# Add paths for imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../../plg_SRC/a0_plg_TFM')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../../plg_SRC_CUSTOM/a0_plg_CUSTOM')))

from plg_SSH import *
from plg_CSV import *
from plg_String import *
from plg_Date_time import *

class RS_Firewall_TaskExecutor:
    """
    Task Executor for Joomla RS Firewall security operations
    Contains the single function that performs RS Firewall tasks
    """
    
    def __init__(self):
        pass
    
    def setup_rs_firewall(self, LIST_file_path):
        """
        Main function to setup RS Firewall on Joomla sites
        """
        log2('info', 'Setting up RS Firewall on Joomla sites')
        try:
            results = []
            for server in merge_and_read_csv(LIST_file_path):
                server_ip, ssh_username, ssh_password = server_details(server)
                if server_ip:
                    try:
                        ssh_client = Ssh_into_server(server_ip, ssh_username, ssh_password)
                        if ssh_client:
                            # Navigate to Joomla directory
                            ssh_exec(ssh_client, "cd /var/www/html")
                            
                            # Install RS Firewall via Joomla CLI
                            ssh_exec(ssh_client, "php cli/joomla.php extension:install --type=component --name=com_rsfirewall")
                            
                            # Enable the component
                            ssh_exec(ssh_client, "php cli/joomla.php extension:enable --type=component --name=com_rsfirewall")
                            
                            results.append(f"RS Firewall setup on {server_ip}")
                            log2('info', f"RS Firewall setup on {server_ip}")
                        else:
                            results.append(f"Failed to SSH into {server_ip}")
                    except Exception as e:
                        results.append(f"Error setting up RS Firewall on {server_ip}: {str(e)}")
            
            return results
        except Exception as e:
            log2('error', f"An error occurred in setup_rs_firewall: {e}")
            return [f"Error: {str(e)}"]
    
    def configure_rs_firewall(self, LIST_file_path):
        """
        Main function to configure RS Firewall settings
        """
        log2('info', 'Configuring RS Firewall settings on Joomla sites')
        try:
            results = []
            for server in merge_and_read_csv(LIST_file_path):
                server_ip, ssh_username, ssh_password = server_details(server)
                if server_ip:
                    try:
                        ssh_client = Ssh_into_server(server_ip, ssh_username, ssh_password)
                        if ssh_client:
                            # Configure RS Firewall settings
                            ssh_exec(ssh_client, "cd /var/www/html")
                            ssh_exec(ssh_client, "php cli/joomla.php extension:config --type=component --name=com_rsfirewall --set=firewall_enabled=1")
                            ssh_exec(ssh_client, "php cli/joomla.php extension:config --type=component --name=com_rsfirewall --set=monitor_system=1")
                            ssh_exec(ssh_client, "php cli/joomla.php extension:config --type=component --name=com_rsfirewall --set=monitor_files=1")
                            
                            results.append(f"RS Firewall settings configured on {server_ip}")
                            log2('info', f"RS Firewall settings configured on {server_ip}")
                        else:
                            results.append(f"Failed to connect to {server_ip}")
                    except Exception as e:
                        results.append(f"Error configuring RS Firewall on {server_ip}: {str(e)}")
            
            return results
        except Exception as e:
            log2('error', f"An error occurred in configure_rs_firewall: {e}")
            return [f"Error: {str(e)}"]
    
    def enable_rs_firewall(self, LIST_file_path):
        """
        Main function to enable RS Firewall
        """
        log2('info', 'Enabling RS Firewall on Joomla sites')
        try:
            results = []
            for server in merge_and_read_csv(LIST_file_path):
                server_ip, ssh_username, ssh_password = server_details(server)
                if server_ip:
                    try:
                        ssh_client = Ssh_into_server(server_ip, ssh_username, ssh_password)
                        if ssh_client:
                            ssh_exec(ssh_client, "cd /var/www/html")
                            ssh_exec(ssh_client, "php cli/joomla.php extension:enable --type=component --name=com_rsfirewall")
                            
                            results.append(f"RS Firewall enabled on {server_ip}")
                            log2('info', f"RS Firewall enabled on {server_ip}")
                        else:
                            results.append(f"Failed to connect to {server_ip}")
                    except Exception as e:
                        results.append(f"Error enabling RS Firewall on {server_ip}: {str(e)}")
            
            return results
        except Exception as e:
            log2('error', f"An error occurred in enable_rs_firewall: {e}")
            return [f"Error: {str(e)}"]
    
    def disable_rs_firewall(self, LIST_file_path):
        """
        Main function to disable RS Firewall
        """
        log2('info', 'Disabling RS Firewall on Joomla sites')
        try:
            results = []
            for server in merge_and_read_csv(LIST_file_path):
                server_ip, ssh_username, ssh_password = server_details(server)
                if server_ip:
                    try:
                        ssh_client = Ssh_into_server(server_ip, ssh_username, ssh_password)
                        if ssh_client:
                            ssh_exec(ssh_client, "cd /var/www/html")
                            ssh_exec(ssh_client, "php cli/joomla.php extension:disable --type=component --name=com_rsfirewall")
                            
                            results.append(f"RS Firewall disabled on {server_ip}")
                            log2('info', f"RS Firewall disabled on {server_ip}")
                        else:
                            results.append(f"Failed to connect to {server_ip}")
                    except Exception as e:
                        results.append(f"Error disabling RS Firewall on {server_ip}: {str(e)}")
            
            return results
        except Exception as e:
            log2('error', f"An error occurred in disable_rs_firewall: {e}")
            return [f"Error: {str(e)}"]
    
    def remove_rs_firewall(self, LIST_file_path):
        """
        Main function to remove RS Firewall
        """
        log2('info', 'Removing RS Firewall from Joomla sites')
        try:
            results = []
            for server in merge_and_read_csv(LIST_file_path):
                server_ip, ssh_username, ssh_password = server_details(server)
                if server_ip:
                    try:
                        ssh_client = Ssh_into_server(server_ip, ssh_username, ssh_password)
                        if ssh_client:
                            ssh_exec(ssh_client, "cd /var/www/html")
                            ssh_exec(ssh_client, "php cli/joomla.php extension:uninstall --type=component --name=com_rsfirewall")
                            
                            results.append(f"RS Firewall removed from {server_ip}")
                            log2('info', f"RS Firewall removed from {server_ip}")
                        else:
                            results.append(f"Failed to connect to {server_ip}")
                    except Exception as e:
                        results.append(f"Error removing RS Firewall from {server_ip}: {str(e)}")
            
            return results
        except Exception as e:
            log2('error', f"An error occurred in remove_rs_firewall: {e}")
            return [f"Error: {str(e)}"]
    
    def update_rs_firewall(self, LIST_file_path):
        """
        Main function to update RS Firewall
        """
        log2('info', 'Updating RS Firewall on Joomla sites')
        try:
            results = []
            for server in merge_and_read_csv(LIST_file_path):
                server_ip, ssh_username, ssh_password = server_details(server)
                if server_ip:
                    try:
                        ssh_client = Ssh_into_server(server_ip, ssh_username, ssh_password)
                        if ssh_client:
                            ssh_exec(ssh_client, "cd /var/www/html")
                            ssh_exec(ssh_client, "php cli/joomla.php extension:update --type=component --name=com_rsfirewall")
                            
                            results.append(f"RS Firewall updated on {server_ip}")
                            log2('info', f"RS Firewall updated on {server_ip}")
                        else:
                            results.append(f"Failed to connect to {server_ip}")
                    except Exception as e:
                        results.append(f"Error updating RS Firewall on {server_ip}: {str(e)}")
            
            return results
        except Exception as e:
            log2('error', f"An error occurred in update_rs_firewall: {e}")
            return [f"Error: {str(e)}"]

