import sys
import os

# Add paths for imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../plg_SRC_CUSTOM/plg_TASK_MODE')))

from Linux_security.fail2ban.plg_TM_fail2ban import Fail2ban_TaskManager

class Fail2ban_CoreTask:
    """
    Core Task class for Fail2ban security operations
    Imports and uses functions from the Task Manager
    """
    
    def __init__(self):
        self.task_manager = Fail2ban_TaskManager()
    
    def setup_fail2ban(self, LIST_file_path):
        """
        Setup and configure Fail2ban on target servers
        """
        return self.task_manager.setup_and_configure_fail2ban(LIST_file_path)
    
    def modify_fail2ban_config(self, LIST_file_path):
        """
        Modify Fail2ban configuration on target servers
        """
        return self.task_manager.modify_fail2ban_config(LIST_file_path)
    
    def remove_fail2ban(self, LIST_file_path):
        """
        Remove Fail2ban from target servers
        """
        return self.task_manager.remove_fail2ban(LIST_file_path)
    
    def start_fail2ban_service(self, LIST_file_path):
        """
        Start Fail2ban service on target servers
        """
        return self.task_manager.start_fail2ban(LIST_file_path)
    
    def stop_fail2ban_service(self, LIST_file_path):
        """
        Stop Fail2ban service on target servers
        """
        return self.task_manager.stop_fail2ban(LIST_file_path)
    
    def restart_fail2ban_service(self, LIST_file_path):
        """
        Restart Fail2ban service on target servers
        """
        return self.task_manager.restart_fail2ban(LIST_file_path)

