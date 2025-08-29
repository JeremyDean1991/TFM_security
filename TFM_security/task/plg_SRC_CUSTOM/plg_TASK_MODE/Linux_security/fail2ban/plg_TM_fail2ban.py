import sys
import os

# Add paths for imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../../plg_SRC/a0_plg_TFM')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../../plg_SRC_CUSTOM/a0_plg_CUSTOM')))

from plg_SSH import *
from plg_CSV import *
from plg_String import *
from plg_Date_time import *
from plg_TASK_MODE.Linux_security.fail2ban.plg_TSK_fail2ban import *

class Fail2ban_TaskManager:
    """
    Task Manager for Fail2ban security operations
    Handles the coordination of Fail2ban security tasks
    """
    
    def __init__(self):
        self.task_executor = Fail2ban_TaskExecutor()
    
    def setup_and_configure_fail2ban(self, LIST_file_path):
        """
        Setup and configure Fail2ban on target servers
        """
        log2('info', 'Setting up and configuring Fail2ban')
        return self.task_executor.setup_and_configure_fail2ban(LIST_file_path)
    
    def modify_fail2ban_config(self, LIST_file_path):
        """
        Modify Fail2ban configuration on target servers
        """
        log2('info', 'Modifying Fail2ban configuration')
        return self.task_executor.modify_fail2ban_config(LIST_file_path)
    
    def remove_fail2ban(self, LIST_file_path):
        """
        Remove Fail2ban from target servers
        """
        log2('info', 'Removing Fail2ban')
        return self.task_executor.remove_fail2ban(LIST_file_path)
    
    def start_fail2ban(self, LIST_file_path):
        """
        Start Fail2ban service on target servers
        """
        log2('info', 'Starting Fail2ban service')
        return self.task_executor.start_fail2ban(LIST_file_path)
    
    def stop_fail2ban(self, LIST_file_path):
        """
        Stop Fail2ban service on target servers
        """
        log2('info', 'Stopping Fail2ban service')
        return self.task_executor.stop_fail2ban(LIST_file_path)
    
    def restart_fail2ban(self, LIST_file_path):
        """
        Restart Fail2ban service on target servers
        """
        log2('info', 'Restarting Fail2ban service')
        return self.task_executor.restart_fail2ban(LIST_file_path)

