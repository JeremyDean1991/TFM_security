import sys
import os

# Add paths for imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../plg_SRC_CUSTOM/plg_TASK_MODE')))

from Network_security.plg_TM_paypal import PayPal_TaskManager

class PayPal_CoreTask:
    """
    Core Task class for PayPal security operations
    Imports and uses functions from the Task Manager
    """
    
    def __init__(self):
        self.task_manager = PayPal_TaskManager()
    
    def setup_paypal_security(self, LIST_file_path):
        """
        Setup PayPal security measures
        """
        return self.task_manager.setup_paypal_security(LIST_file_path)
    
    def configure_paypal_webhook(self, LIST_file_path):
        """
        Configure PayPal webhook security
        """
        return self.task_manager.configure_paypal_webhook(LIST_file_path)
    
    def enable_paypal_fraud_protection(self, LIST_file_path):
        """
        Enable PayPal fraud protection features
        """
        return self.task_manager.enable_paypal_fraud_protection(LIST_file_path)
    
    def setup_paypal_ip_whitelist(self, LIST_file_path):
        """
        Setup PayPal IP whitelist
        """
        return self.task_manager.setup_paypal_ip_whitelist(LIST_file_path)
    
    def configure_paypal_ssl_verification(self, LIST_file_path):
        """
        Configure PayPal SSL verification
        """
        return self.task_manager.configure_paypal_ssl_verification(LIST_file_path)

