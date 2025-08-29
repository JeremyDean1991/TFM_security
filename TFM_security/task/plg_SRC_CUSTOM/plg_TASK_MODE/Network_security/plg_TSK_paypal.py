import sys
import os

# Add paths for imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../plg_SRC/a0_plg_TFM')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../plg_SRC_CUSTOM/a0_plg_CUSTOM')))

from plg_SSH import *
from plg_CSV import *
from plg_String import *
from plg_Date_time import *

class PayPal_TaskExecutor:
    """
    Task Executor for PayPal security operations
    Contains the single function that performs PayPal security tasks
    """
    
    def __init__(self):
        pass
    
    def setup_paypal_security(self, LIST_file_path):
        """
        Main function to setup PayPal security measures
        """
        log2('info', 'Setting up PayPal security measures')
        try:
            results = []
            for server in merge_and_read_csv(LIST_file_path):
                server_ip, ssh_username, ssh_password = server_details(server)
                if server_ip:
                    try:
                        ssh_client = Ssh_into_server(server_ip, ssh_username, ssh_password)
                        if ssh_client:
                            # Setup basic PayPal security
                            ssh_exec(ssh_client, "mkdir -p /etc/paypal/security")
                            ssh_exec(ssh_client, "echo 'PayPal security configuration' > /etc/paypal/security/config.conf")
                            
                            results.append(f"PayPal security setup on {server_ip}")
                            log2('info', f"PayPal security setup on {server_ip}")
                        else:
                            results.append(f"Failed to SSH into {server_ip}")
                    except Exception as e:
                        results.append(f"Error setting up PayPal security on {server_ip}: {str(e)}")
            
            return results
        except Exception as e:
            log2('error', f"An error occurred in setup_paypal_security: {e}")
            return [f"Error: {str(e)}"]
    
    def configure_paypal_webhook(self, LIST_file_path):
        """
        Main function to configure PayPal webhook security
        """
        log2('info', 'Configuring PayPal webhook security')
        try:
            results = []
            for server in merge_and_read_csv(LIST_file_path):
                server_ip, ssh_username, ssh_password = server_details(server)
                if server_ip:
                    try:
                        ssh_client = Ssh_into_server(server_ip, ssh_username, ssh_password)
                        if ssh_client:
                            # Configure webhook security
                            ssh_exec(ssh_client, "echo 'webhook_security_enabled=true' >> /etc/paypal/security/config.conf")
                            ssh_exec(ssh_client, "echo 'webhook_ssl_verify=true' >> /etc/paypal/security/config.conf")
                            
                            results.append(f"PayPal webhook security configured on {server_ip}")
                            log2('info', f"PayPal webhook security configured on {server_ip}")
                        else:
                            results.append(f"Failed to connect to {server_ip}")
                    except Exception as e:
                        results.append(f"Error configuring webhook security on {server_ip}: {str(e)}")
            
            return results
        except Exception as e:
            log2('error', f"An error occurred in configure_paypal_webhook: {e}")
            return [f"Error: {str(e)}"]
    
    def enable_paypal_fraud_protection(self, LIST_file_path):
        """
        Main function to enable PayPal fraud protection
        """
        log2('info', 'Enabling PayPal fraud protection features')
        try:
            results = []
            for server in merge_and_read_csv(LIST_file_path):
                server_ip, ssh_username, ssh_password = server_details(server)
                if server_ip:
                    try:
                        ssh_client = Ssh_into_server(server_ip, ssh_username, ssh_password)
                        if ssh_client:
                            # Enable fraud protection
                            ssh_exec(ssh_client, "echo 'fraud_protection_enabled=true' >> /etc/paypal/security/config.conf")
                            ssh_exec(ssh_client, "echo 'risk_assessment_level=high' >> /etc/paypal/security/config.conf")
                            
                            results.append(f"PayPal fraud protection enabled on {server_ip}")
                            log2('info', f"PayPal fraud protection enabled on {server_ip}")
                        else:
                            results.append(f"Failed to connect to {server_ip}")
                    except Exception as e:
                        results.append(f"Error enabling fraud protection on {server_ip}: {str(e)}")
            
            return results
        except Exception as e:
            log2('error', f"An error occurred in enable_paypal_fraud_protection: {e}")
            return [f"Error: {str(e)}"]
    
    def setup_paypal_ip_whitelist(self, LIST_file_path):
        """
        Main function to setup PayPal IP whitelist
        """
        log2('info', 'Setting up PayPal IP whitelist')
        try:
            results = []
            for server in merge_and_read_csv(LIST_file_path):
                server_ip, ssh_username, ssh_password = server_details(server)
                if server_ip:
                    try:
                        ssh_client = Ssh_into_server(server_ip, ssh_username, ssh_password)
                        if ssh_client:
                            # Setup IP whitelist
                            ssh_exec(ssh_client, "echo '173.0.81.0/24' > /etc/paypal/security/ip_whitelist.txt")
                            ssh_exec(ssh_client, "echo '173.0.81.1' >> /etc/paypal/security/ip_whitelist.txt")
                            ssh_exec(ssh_client, "echo '173.0.81.33' >> /etc/paypal/security/ip_whitelist.txt")
                            
                            results.append(f"PayPal IP whitelist setup on {server_ip}")
                            log2('info', f"PayPal IP whitelist setup on {server_ip}")
                        else:
                            results.append(f"Failed to connect to {server_ip}")
                    except Exception as e:
                        results.append(f"Error setting up IP whitelist on {server_ip}: {str(e)}")
            
            return results
        except Exception as e:
            log2('error', f"An error occurred in setup_paypal_ip_whitelist: {e}")
            return [f"Error: {str(e)}"]
    
    def configure_paypal_ssl_verification(self, LIST_file_path):
        """
        Main function to configure PayPal SSL verification
        """
        log2('info', 'Configuring PayPal SSL verification')
        try:
            results = []
            for server in merge_and_read_csv(LIST_file_path):
                server_ip, ssh_username, ssh_password = server_details(server)
                if server_ip:
                    try:
                        ssh_client = Ssh_into_server(server_ip, ssh_username, ssh_password)
                        if ssh_client:
                            # Configure SSL verification
                            ssh_exec(ssh_client, "echo 'ssl_verification_enabled=true' >> /etc/paypal/security/config.conf")
                            ssh_exec(ssh_client, "echo 'ssl_cert_path=/etc/ssl/certs' >> /etc/paypal/security/config.conf")
                            
                            results.append(f"PayPal SSL verification configured on {server_ip}")
                            log2('info', f"PayPal SSL verification configured on {server_ip}")
                        else:
                            results.append(f"Failed to connect to {server_ip}")
                    except Exception as e:
                        results.append(f"Error configuring SSL verification on {server_ip}: {str(e)}")
            
            return results
        except Exception as e:
            log2('error', f"An error occurred in configure_paypal_ssl_verification: {e}")
            return [f"Error: {str(e)}"]



