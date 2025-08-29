import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../../plg_SRC/a0_plg_TFM')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../../plg_SRC_CUSTOM/a0_plg_CUSTOM')))
from plg_SSH import *
from plg_CSV import *
from plg_String import *
from plg_Date_time import *
from plg_TASK_MODE.Linux_security.mod_evasive.plg_TSK_mod_evasive import *

class ModEvasive_TaskManager:
    """
    Task Manager for ModEvasive DDoS protection
    Coordinates ModEvasive operations through the Task Executor
    """
    
    def __init__(self):
        self.task_executor = ModEvasive_TaskExecutor()
    
    def install_mod_evasive(self, LIST_file_path):
        """Install ModEvasive on target servers"""
        log2('info', 'Installing ModEvasive')
        return self.task_executor.install_mod_evasive(LIST_file_path)
    
    def configure_mod_evasive(self, LIST_file_path):
        """Configure ModEvasive settings"""
        log2('info', 'Configuring ModEvasive')
        return self.task_executor.configure_mod_evasive(LIST_file_path)
    
    def enable_mod_evasive(self, LIST_file_path):
        """Enable ModEvasive protection"""
        log2('info', 'Enabling ModEvasive')
        return self.task_executor.enable_mod_evasive(LIST_file_path)
    
    def disable_mod_evasive(self, LIST_file_path):
        """Disable ModEvasive protection"""
        log2('info', 'Disabling ModEvasive')
        return self.task_executor.disable_mod_evasive(LIST_file_path)
    
    def remove_mod_evasive(self, LIST_file_path):
        """Remove ModEvasive from target servers"""
        log2('info', 'Removing ModEvasive')
        return self.task_executor.remove_mod_evasive(LIST_file_path)

