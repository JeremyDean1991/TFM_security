import sys
import os

# Add paths for imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../plg_SRC/a0_plg_TFM')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../plg_SRC_CUSTOM/a0_plg_CUSTOM')))

from plg_SSH import *
from plg_CSV import *
from plg_String import *
from plg_Date_time import *
from plg_TASK_MODE.Network_security.plg_TSK_paypal import *

class PayPal_TaskManager:
    """
    Task Manager for PayPal security operations
    Handles the coordination of PayPal security tasks
    """
    
    def __init__(self):
        self.task_executor = PayPal_TaskExecutor()
    
    def setup_paypal_security(self, LIST_file_path):
        """
        Setup PayPal security measures
        """
        log2('info', 'Setting up PayPal security measures')
        return self.task_executor.setup_paypal_security(LIST_file_path)
    
    def configure_paypal_webhook(self, LIST_file_path):
        """
        Configure PayPal webhook security
        """
        log2('info', 'Configuring PayPal webhook security')
        return self.task_executor.configure_paypal_webhook(LIST_file_path)
    
    def enable_paypal_fraud_protection(self, LIST_file_path):
        """
        Enable PayPal fraud protection features
        """
        log2('info', 'Enabling PayPal fraud protection features')
        return self.task_executor.enable_paypal_fraud_protection(LIST_file_path)
    
    def setup_paypal_ip_whitelist(self, LIST_file_path):
        """
        Setup PayPal IP whitelist
        """
        log2('info', 'Setting up PayPal IP whitelist')
        return self.task_executor.setup_paypal_ip_whitelist(LIST_file_path)
    
    def configure_paypal_ssl_verification(self, LIST_file_path):
        """
        Configure PayPal SSL verification
        """
        log2('info', 'Configuring PayPal SSL verification')
        return self.task_executor.configure_paypal_ssl_verification(LIST_file_path)



