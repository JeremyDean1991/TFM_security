import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../../plg_SRC/a0_plg_TFM')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../../plg_SRC_CUSTOM/a0_plg_CUSTOM')))
from plg_SSH import *
from plg_CSV import *
from plg_String import *
from plg_Date_time import *
from plg_TASK_MODE.Linux_security.rootkit_hunter.plg_TSK_rootkit_hunter import *

class RootKit_Hunter_TaskManager:
    """
    Task Manager for RootKit Hunter
    Coordinates rootkit detection operations through the Task Executor
    """
    
    def __init__(self):
        self.task_executor = RootKit_Hunter_TaskExecutor()
    
    def install_rootkit_hunter(self, LIST_file_path):
        """Install RootKit Hunter on target servers"""
        log2('info', 'Installing RootKit Hunter')
        return self.task_executor.install_rootkit_hunter(LIST_file_path)
    
    def run_rootkit_scan(self, LIST_file_path):
        """Run RootKit Hunter scan"""
        log2('info', 'Running RootKit scan')
        return self.task_executor.run_rootkit_scan(LIST_file_path)
    
    def update_rootkit_hunter(self, LIST_file_path):
        """Update RootKit Hunter database"""
        log2('info', 'Updating RootKit Hunter')
        return self.task_executor.update_rootkit_hunter(LIST_file_path)
    
    def configure_rootkit_hunter(self, LIST_file_path):
        """Configure RootKit Hunter settings"""
        log2('info', 'Configuring RootKit Hunter')
        return self.task_executor.configure_rootkit_hunter(LIST_file_path)
    
    def remove_rootkit_hunter(self, LIST_file_path):
        """Remove RootKit Hunter from target servers"""
        log2('info', 'Removing RootKit Hunter')
        return self.task_executor.remove_rootkit_hunter(LIST_file_path)

