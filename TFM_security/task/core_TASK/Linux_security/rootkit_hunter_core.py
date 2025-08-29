import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../plg_SRC_CUSTOM/plg_TASK_MODE/Linux_security/rootkit_hunter')))
from plg_TM_rootkit_hunter import RootKit_Hunter_TaskManager

class RootKit_Hunter_CoreTask:
    """
    Core Task for RootKit Hunter
    Provides interface to TFM router
    """
    
    def __init__(self):
        self.task_manager = RootKit_Hunter_TaskManager()
    
    def install_rootkit_hunter(self, LIST_file_path):
        """Install RootKit Hunter"""
        return self.task_manager.install_rootkit_hunter(LIST_file_path)
    
    def run_rootkit_scan(self, LIST_file_path):
        """Run RootKit Hunter scan"""
        return self.task_manager.run_rootkit_scan(LIST_file_path)
    
    def update_rootkit_hunter(self, LIST_file_path):
        """Update RootKit Hunter database"""
        return self.task_manager.update_rootkit_hunter(LIST_file_path)
    
    def configure_rootkit_hunter(self, LIST_file_path):
        """Configure RootKit Hunter"""
        return self.task_manager.configure_rootkit_hunter(LIST_file_path)
    
    def remove_rootkit_hunter(self, LIST_file_path):
        """Remove RootKit Hunter"""
        return self.task_manager.remove_rootkit_hunter(LIST_file_path)

