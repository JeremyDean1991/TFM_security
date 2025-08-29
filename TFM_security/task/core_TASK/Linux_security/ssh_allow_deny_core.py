import sys
import os

# Add paths for imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../plg_SRC_CUSTOM/plg_TASK_MODE')))

from Linux_security.ssh_allow_deny.plg_TM_ssh_allow_deny import SSH_AllowDeny_TaskManager

class SSH_AllowDeny_CoreTask:
    """
    Core Task class for SSH allow/deny security operations
    Imports and uses functions from the Task Manager
    """
    
    def __init__(self):
        self.task_manager = SSH_AllowDeny_TaskManager()
    
    def setup_ssh_allow_deny(self, LIST_file_path):
        """
        Setup SSH allow/deny hosts configuration on target servers
        """
        return self.task_manager.setup_ssh_allow_deny_hosts(LIST_file_path)
    
    def modify_ssh_allow_deny(self, LIST_file_path):
        """
        Modify SSH allow/deny hosts configuration on target servers
        """
        return self.task_manager.modify_ssh_allow_deny_hosts(LIST_file_path)
    
    def add_allowed_host(self, LIST_file_path, allowed_host):
        """
        Add a new allowed host to SSH configuration
        """
        return self.task_manager.add_allowed_host(LIST_file_path, allowed_host)
    
    def remove_allowed_host(self, LIST_file_path, host_to_remove):
        """
        Remove an allowed host from SSH configuration
        """
        return self.task_manager.remove_allowed_host(LIST_file_path, host_to_remove)
    
    def add_denied_host(self, LIST_file_path, denied_host):
        """
        Add a new denied host to SSH configuration
        """
        return self.task_manager.add_denied_host(LIST_file_path, denied_host)
    
    def remove_denied_host(self, LIST_file_path, host_to_remove):
        """
        Remove a denied host from SSH configuration
        """
        return self.task_manager.remove_denied_host(LIST_file_path, host_to_remove)

