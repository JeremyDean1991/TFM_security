import sys
import os

# Add paths for imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../plg_SRC_CUSTOM/plg_TASK_MODE')))

from Linux_security.mod_security.plg_TM_mod_security import ModSecurity_TaskManager

class ModSecurity_CoreTask:
    """
    Core Task class for ModSecurity operations
    Imports and uses functions from the Task Manager
    """
    
    def __init__(self):
        self.task_manager = ModSecurity_TaskManager()
    
    def setup_modsecurity(self, LIST_file_path):
        """
        Setup and configure ModSecurity on target servers
        """
        return self.task_manager.setup_and_configure_modsecurity(LIST_file_path)
    
    def remove_modsecurity(self, LIST_file_path):
        """
        Remove ModSecurity from target servers
        """
        return self.task_manager.remove_modsecurity(LIST_file_path)
    
    def enable_modsecurity(self, LIST_file_path):
        """
        Enable ModSecurity on target servers
        """
        return self.task_manager.enable_modsecurity(LIST_file_path)
    
    def disable_modsecurity(self, LIST_file_path):
        """
        Disable ModSecurity on target servers
        """
        return self.task_manager.disable_modsecurity(LIST_file_path)

