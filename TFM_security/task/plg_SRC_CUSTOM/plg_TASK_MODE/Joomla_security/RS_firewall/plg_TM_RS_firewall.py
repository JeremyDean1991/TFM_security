import sys
import os

# Add paths for imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../../plg_SRC/a0_plg_TFM')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../../plg_SRC_CUSTOM/a0_plg_CUSTOM')))

from plg_SSH import *
from plg_CSV import *
from plg_String import *
from plg_Date_time import *
from plg_TASK_MODE.Joomla_security.RS_firewall.plg_TSK_RS_firewall import *

class RS_Firewall_TaskManager:
    """
    Task Manager for Joomla RS Firewall security operations
    Handles the coordination of RS Firewall security tasks
    """
    
    def __init__(self):
        self.task_executor = RS_Firewall_TaskExecutor()
    
    def setup_rs_firewall(self, LIST_file_path):
        """
        Setup RS Firewall on Joomla sites
        """
        log2('info', 'Setting up RS Firewall on Joomla sites')
        return self.task_executor.setup_rs_firewall(LIST_file_path)
    
    def configure_rs_firewall(self, LIST_file_path):
        """
        Configure RS Firewall settings on Joomla sites
        """
        log2('info', 'Configuring RS Firewall settings on Joomla sites')
        return self.task_executor.configure_rs_firewall(LIST_file_path)
    
    def enable_rs_firewall(self, LIST_file_path):
        """
        Enable RS Firewall on Joomla sites
        """
        log2('info', 'Enabling RS Firewall on Joomla sites')
        return self.task_executor.enable_rs_firewall(LIST_file_path)
    
    def disable_rs_firewall(self, LIST_file_path):
        """
        Disable RS Firewall on Joomla sites
        """
        log2('info', 'Disabling RS Firewall on Joomla sites')
        return self.task_executor.disable_rs_firewall(LIST_file_path)
    
    def remove_rs_firewall(self, LIST_file_path):
        """
        Remove RS Firewall from Joomla sites
        """
        log2('info', 'Removing RS Firewall from Joomla sites')
        return self.task_executor.remove_rs_firewall(LIST_file_path)
    
    def update_rs_firewall(self, LIST_file_path):
        """
        Update RS Firewall on Joomla sites
        """
        log2('info', 'Updating RS Firewall on Joomla sites')
        return self.task_executor.update_rs_firewall(LIST_file_path)

