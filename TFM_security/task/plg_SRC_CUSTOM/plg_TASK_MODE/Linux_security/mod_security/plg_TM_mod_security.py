import sys
import os

# Add paths for imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../../plg_SRC/a0_plg_TFM')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../../plg_SRC_CUSTOM/a0_plg_CUSTOM')))

from plg_SSH import *
from plg_CSV import *
from plg_String import *
from plg_Date_time import *
from plg_TASK_MODE.Linux_security.mod_security.plg_TSK_mod_security import *

class ModSecurity_TaskManager:
    """
    Task Manager for ModSecurity operations
    Handles the coordination of ModSecurity tasks
    """
    
    def __init__(self):
        self.task_executor = ModSecurity_TaskExecutor()
    
    def setup_and_configure_modsecurity(self, LIST_file_path):
        """
        Setup and configure ModSecurity on target servers
        """
        log2('info', 'Setting up and configuring ModSecurity')
        return self.task_executor.setup_and_configure_modsecurity(LIST_file_path)
    
    def remove_modsecurity(self, LIST_file_path):
        """
        Remove ModSecurity from target servers
        """
        log2('info', 'Removing ModSecurity')
        return self.task_executor.remove_modsecurity(LIST_file_path)
    
    def enable_modsecurity(self, LIST_file_path):
        """
        Enable ModSecurity on target servers
        """
        log2('info', 'Enabling ModSecurity')
        return self.task_executor.enable_modsecurity(LIST_file_path)
    
    def disable_modsecurity(self, LIST_file_path):
        """
        Disable ModSecurity on target servers
        """
        log2('info', 'Disabling ModSecurity')
        return self.task_executor.disable_modsecurity(LIST_file_path)

