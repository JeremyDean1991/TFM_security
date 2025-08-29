import sys
import os

# Add paths for imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../../plg_SRC/a0_plg_TFM')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../../plg_SRC_CUSTOM/a0_plg_CUSTOM')))

from plg_SSH import *
from plg_CSV import *
from plg_String import *
from plg_Date_time import *

class Joomla_Captcha_TaskExecutor:
    """
    Task Executor for Joomla Captcha security operations
    Contains the single function that performs Joomla Captcha tasks
    """
    
    def __init__(self):
        pass
    
    def setup_captcha_plugin(self, LIST_file_path):
        """
        Main function to setup Captcha plugin on Joomla sites
        """
        log2('info', 'Setting up Captcha plugin on Joomla sites')
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
                            
                            # Install Captcha plugin via Joomla CLI
                            ssh_exec(ssh_client, "php cli/joomla.php extension:install --type=plugin --group=captcha --name=recaptcha")
                            
                            # Enable the plugin
                            ssh_exec(ssh_client, "php cli/joomla.php extension:enable --type=plugin --group=captcha --name=recaptcha")
                            
                            results.append(f"Captcha plugin setup on {server_ip}")
                            log2('info', f"Captcha plugin setup on {server_ip}")
                        else:
                            results.append(f"Failed to SSH into {server_ip}")
                    except Exception as e:
                        results.append(f"Error setting up Captcha on {server_ip}: {str(e)}")
            
            return results
        except Exception as e:
            log2('error', f"An error occurred in setup_captcha_plugin: {e}")
            return [f"Error: {str(e)}"]
    
    def configure_captcha_settings(self, LIST_file_path):
        """
        Main function to configure Captcha settings
        """
        log2('info', 'Configuring Captcha settings on Joomla sites')
        try:
            results = []
            for server in merge_and_read_csv(LIST_file_path):
                server_ip, ssh_username, ssh_password = server_details(server)
                if server_ip:
                    try:
                        ssh_client = Ssh_into_server(server_ip, ssh_username, ssh_password)
                        if ssh_client:
                            # Configure Captcha settings
                            ssh_exec(ssh_client, "cd /var/www/html")
                            ssh_exec(ssh_client, "php cli/joomla.php extension:config --type=plugin --group=captcha --name=recaptcha --set=public_key=YOUR_PUBLIC_KEY")
                            ssh_exec(ssh_client, "php cli/joomla.php extension:config --type=plugin --group=captcha --name=recaptcha --set=private_key=YOUR_PRIVATE_KEY")
                            
                            results.append(f"Captcha settings configured on {server_ip}")
                            log2('info', f"Captcha settings configured on {server_ip}")
                        else:
                            results.append(f"Failed to connect to {server_ip}")
                    except Exception as e:
                        results.append(f"Error configuring Captcha on {server_ip}: {str(e)}")
            
            return results
        except Exception as e:
            log2('error', f"An error occurred in configure_captcha_settings: {e}")
            return [f"Error: {str(e)}"]
    
    def enable_captcha_on_forms(self, LIST_file_path):
        """
        Main function to enable Captcha on forms
        """
        log2('info', 'Enabling Captcha on Joomla forms')
        try:
            results = []
            for server in merge_and_read_csv(LIST_file_path):
                server_ip, ssh_username, ssh_password = server_details(server)
                if server_ip:
                    try:
                        ssh_client = Ssh_into_server(server_ip, ssh_username, ssh_password)
                        if ssh_client:
                            # Enable Captcha on specific forms
                            ssh_exec(ssh_client, "cd /var/www/html")
                            ssh_exec(ssh_client, "php cli/joomla.php extension:config --type=plugin --group=captcha --name=recaptcha --set=forms=contact,user,login")
                            
                            results.append(f"Captcha enabled on forms for {server_ip}")
                            log2('info', f"Captcha enabled on forms for {server_ip}")
                        else:
                            results.append(f"Failed to connect to {server_ip}")
                    except Exception as e:
                        results.append(f"Error enabling Captcha on forms for {server_ip}: {str(e)}")
            
            return results
        except Exception as e:
            log2('error', f"An error occurred in enable_captcha_on_forms: {e}")
            return [f"Error: {str(e)}"]
    
    def disable_captcha_plugin(self, LIST_file_path):
        """
        Main function to disable Captcha plugin
        """
        log2('info', 'Disabling Captcha plugin on Joomla sites')
        try:
            results = []
            for server in merge_and_read_csv(LIST_file_path):
                server_ip, ssh_username, ssh_password = server_details(server)
                if server_ip:
                    try:
                        ssh_client = Ssh_into_server(server_ip, ssh_username, ssh_password)
                        if ssh_client:
                            ssh_exec(ssh_client, "cd /var/www/html")
                            ssh_exec(ssh_client, "php cli/joomla.php extension:disable --type=plugin --group=captcha --name=recaptcha")
                            
                            results.append(f"Captcha plugin disabled on {server_ip}")
                            log2('info', f"Captcha plugin disabled on {server_ip}")
                        else:
                            results.append(f"Failed to connect to {server_ip}")
                    except Exception as e:
                        results.append(f"Error disabling Captcha on {server_ip}: {str(e)}")
            
            return results
        except Exception as e:
            log2('error', f"An error occurred in disable_captcha_plugin: {e}")
            return [f"Error: {str(e)}"]
    
    def remove_captcha_plugin(self, LIST_file_path):
        """
        Main function to remove Captcha plugin
        """
        log2('info', 'Removing Captcha plugin from Joomla sites')
        try:
            results = []
            for server in merge_and_read_csv(LIST_file_path):
                server_ip, ssh_username, ssh_password = server_details(server)
                if server_ip:
                    try:
                        ssh_client = Ssh_into_server(server_ip, ssh_username, ssh_password)
                        if ssh_client:
                            ssh_exec(ssh_client, "cd /var/www/html")
                            ssh_exec(ssh_client, "php cli/joomla.php extension:uninstall --type=plugin --group=captcha --name=recaptcha")
                            
                            results.append(f"Captcha plugin removed from {server_ip}")
                            log2('info', f"Captcha plugin removed from {server_ip}")
                        else:
                            results.append(f"Failed to connect to {server_ip}")
                    except Exception as e:
                        results.append(f"Error removing Captcha from {server_ip}: {str(e)}")
            
            return results
        except Exception as e:
            log2('error', f"An error occurred in remove_captcha_plugin: {e}")
            return [f"Error: {str(e)}"]

