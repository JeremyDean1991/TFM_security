import sys
import os

# Add paths for imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../../plg_SRC/a0_plg_TFM')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../../plg_SRC_CUSTOM/a0_plg_CUSTOM')))

from plg_SSH import *
from plg_CSV import *
from plg_String import *
from plg_Date_time import *
from plg_TASK_MODE.Linux_security.Inotify.plg_TSK_Inotify import *

class Inotify_TaskManager:
    """
    Task Manager for Inotify file system monitoring operations
    Handles the coordination of file system monitoring tasks
    """
    
    def __init__(self):
        self.task_executor = Inotify_TaskExecutor()
    
    def setup_inotify_monitoring(self, LIST_file_path):
        """
        Setup Inotify monitoring on target servers
        """
        log2('info', 'Setting up Inotify monitoring')
        return self.task_executor.setup_inotify_monitoring(LIST_file_path)
    
    def configure_inotify_watches(self, LIST_file_path):
        """
        Configure Inotify watch directories
        """
        log2('info', 'Configuring Inotify watch directories')
        return self.task_executor.configure_inotify_watches(LIST_file_path)
    
    def start_inotify_monitoring(self, LIST_file_path):
        """
        Start Inotify monitoring service
        """
        log2('info', 'Starting Inotify monitoring service')
        return self.task_executor.start_inotify_monitoring(LIST_file_path)
    
    def stop_inotify_monitoring(self, LIST_file_path):
        """
        Stop Inotify monitoring service
        """
        log2('info', 'Stopping Inotify monitoring service')
        return self.task_executor.stop_inotify_monitoring(LIST_file_path)
    
    def remove_inotify(self, LIST_file_path):
        """
        Remove Inotify from target servers
        """
        log2('info', 'Removing Inotify')
        return self.task_executor.remove_inotify(LIST_file_path)

