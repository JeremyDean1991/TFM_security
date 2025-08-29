import sys
import os

# Add paths for imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../plg_SRC_CUSTOM/plg_TASK_MODE')))

from Linux_security.clamAV.plg_TM_clamAV import ClamAV_TaskManager

class ClamAV_CoreTask:
    """
    Core Task class for ClamAV security operations
    Imports and uses functions from the Task Manager
    """
    
    def __init__(self):
        self.task_manager = ClamAV_TaskManager()
    
    def setup_clamav(self, LIST_file_path):
        """
        Setup and configure ClamAV on target servers
        """
        return self.task_manager.setup_and_configure_clamav(LIST_file_path)
    
    def modify_clamav_config(self, LIST_file_path):
        """
        Modify ClamAV configuration on target servers
        """
        return self.task_manager.modify_clamav_config(LIST_file_path)
    
    def stop_clamav_service(self, LIST_file_path):
        """
        Stop ClamAV service on target servers
        """
        return self.task_manager.stop_clamav(LIST_file_path)
    
    def remove_clamav(self, LIST_file_path):
        """
        Remove ClamAV from target servers
        """
        return self.task_manager.remove_clamav(LIST_file_path)
    
    def start_clamav_scan(self, LIST_file_path):
        """
        Start ClamAV virus scan on target servers
        """
        return self.task_manager.start_clamav_scan(LIST_file_path)
    
    def enable_clamav_service(self, LIST_file_path):
        """
        Enable ClamAV service on target servers
        """
        return self.task_manager.enable_clamav(LIST_file_path)

