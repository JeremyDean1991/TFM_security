import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../plg_SRC_CUSTOM/plg_TASK_MODE/Linux_security/mod_evasive')))
from plg_TM_mod_evasive import ModEvasive_TaskManager

class ModEvasive_CoreTask:
    """
    Core Task for ModEvasive DDoS protection
    Provides interface to TFM router
    """
    
    def __init__(self):
        self.task_manager = ModEvasive_TaskManager()
    
    def install_mod_evasive(self, LIST_file_path):
        """Install ModEvasive"""
        return self.task_manager.install_mod_evasive(LIST_file_path)
    
    def configure_mod_evasive(self, LIST_file_path):
        """Configure ModEvasive"""
        return self.task_manager.configure_mod_evasive(LIST_file_path)
    
    def enable_mod_evasive(self, LIST_file_path):
        """Enable ModEvasive"""
        return self.task_manager.enable_mod_evasive(LIST_file_path)
    
    def disable_mod_evasive(self, LIST_file_path):
        """Disable ModEvasive"""
        return self.task_manager.disable_mod_evasive(LIST_file_path)
    
    def remove_mod_evasive(self, LIST_file_path):
        """Remove ModEvasive"""
        return self.task_manager.remove_mod_evasive(LIST_file_path)

