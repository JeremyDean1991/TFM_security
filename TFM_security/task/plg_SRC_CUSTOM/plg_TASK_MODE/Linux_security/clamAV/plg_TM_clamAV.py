import sys
import os

# Add paths for imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../../plg_SRC/a0_plg_TFM')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../../plg_SRC_CUSTOM/a0_plg_CUSTOM')))

from plg_SSH import *
from plg_CSV import *
from plg_String import *
from plg_Date_time import *
from plg_TASK_MODE.Linux_security.clamAV.plg_TSK_clamAV import *

class ClamAV_TaskManager:
    """
    Task Manager for ClamAV security operations
    Handles the coordination of ClamAV security tasks
    """
    
    def __init__(self):
        self.task_executor = ClamAV_TaskExecutor()
    
    def setup_and_configure_clamav(self, LIST_file_path):
        """
        Setup and configure ClamAV on target servers
        """
        log2('info', 'Setting up and configuring ClamAV')
        return self.task_executor.setup_and_configure_clamav(LIST_file_path)
    
    def modify_clamav_config(self, LIST_file_path):
        """
        Modify ClamAV configuration on target servers
        """
        log2('info', 'Modifying ClamAV configuration')
        return self.task_executor.modify_clamav_config(LIST_file_path)
    
    def stop_clamav(self, LIST_file_path):
        """
        Stop ClamAV service on target servers
        """
        log2('info', 'Stopping ClamAV service')
        return self.task_executor.stop_clamav(LIST_file_path)
    
    def remove_clamav(self, LIST_file_path):
        """
        Remove ClamAV from target servers
        """
        log2('info', 'Removing ClamAV')
        return self.task_executor.remove_clamav(LIST_file_path)
    
    def start_clamav_scan(self, LIST_file_path):
        """
        Start ClamAV virus scan on target servers
        """
        log2('info', 'Starting ClamAV virus scan')
        return self.task_executor.start_clamav_scan(LIST_file_path)
    
    def enable_clamav(self, LIST_file_path):
        """
        Enable ClamAV service on target servers
        """
        log2('info', 'Enabling ClamAV service')
        return self.task_executor.enable_clamav(LIST_file_path)

