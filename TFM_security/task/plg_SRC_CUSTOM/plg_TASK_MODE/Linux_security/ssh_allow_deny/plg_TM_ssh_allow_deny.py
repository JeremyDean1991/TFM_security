import sys
import os

# Add paths for imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../../plg_SRC/a0_plg_TFM')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../../plg_SRC_CUSTOM/a0_plg_CUSTOM')))

from plg_SSH import *
from plg_CSV import *
from plg_String import *
from plg_Date_time import *
from plg_TASK_MODE.Linux_security.ssh_allow_deny.plg_TSK_ssh_allow_deny import *

class SSH_AllowDeny_TaskManager:
    """
    Task Manager for SSH allow/deny security operations
    Handles the coordination of SSH access control tasks
    """
    
    def __init__(self):
        self.task_executor = SSH_AllowDeny_TaskExecutor()
    
    def setup_ssh_allow_deny_hosts(self, LIST_file_path):
        """
        Setup SSH allow/deny hosts configuration on target servers
        """
        log2('info', 'Setting up SSH allow/deny hosts configuration')
        return self.task_executor.setup_ssh_allow_deny_hosts(LIST_file_path)
    
    def modify_ssh_allow_deny_hosts(self, LIST_file_path):
        """
        Modify SSH allow/deny hosts configuration on target servers
        """
        log2('info', 'Modifying SSH allow/deny hosts configuration')
        return self.task_executor.modify_ssh_allow_deny_hosts(LIST_file_path)
    
    def add_allowed_host(self, LIST_file_path, allowed_host):
        """
        Add a new allowed host to SSH configuration
        """
        log2('info', f'Adding allowed host: {allowed_host}')
        return self.task_executor.add_allowed_host(LIST_file_path, allowed_host)
    
    def remove_allowed_host(self, LIST_file_path, host_to_remove):
        """
        Remove an allowed host from SSH configuration
        """
        log2('info', f'Removing allowed host: {host_to_remove}')
        return self.task_executor.remove_allowed_host(LIST_file_path, host_to_remove)
    
    def add_denied_host(self, LIST_file_path, denied_host):
        """
        Add a new denied host to SSH configuration
        """
        log2('info', f'Adding denied host: {denied_host}')
        return self.task_executor.add_denied_host(LIST_file_path, denied_host)
    
    def remove_denied_host(self, LIST_file_path, host_to_remove):
        """
        Remove a denied host from SSH configuration
        """
        log2('info', f'Removing denied host: {host_to_remove}')
        return self.task_executor.remove_denied_host(LIST_file_path, host_to_remove)

