import sys
import os

# Add paths for imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../plg_SRC_CUSTOM/plg_TASK_MODE')))

from Joomla_security.Captcha.plg_TM_Captcha import Joomla_Captcha_TaskManager

class Joomla_Captcha_CoreTask:
    """
    Core Task class for Joomla Captcha security operations
    Imports and uses functions from the Task Manager
    """
    
    def __init__(self):
        self.task_manager = Joomla_Captcha_TaskManager()
    
    def setup_captcha(self, LIST_file_path):
        """
        Setup Captcha plugin on Joomla sites
        """
        return self.task_manager.setup_captcha_plugin(LIST_file_path)
    
    def configure_captcha(self, LIST_file_path):
        """
        Configure Captcha settings on Joomla sites
        """
        return self.task_manager.configure_captcha_settings(LIST_file_path)
    
    def enable_captcha_forms(self, LIST_file_path):
        """
        Enable Captcha on Joomla forms
        """
        return self.task_manager.enable_captcha_on_forms(LIST_file_path)
    
    def disable_captcha(self, LIST_file_path):
        """
        Disable Captcha plugin on Joomla sites
        """
        return self.task_manager.disable_captcha_plugin(LIST_file_path)
    
    def remove_captcha(self, LIST_file_path):
        """
        Remove Captcha plugin from Joomla sites
        """
        return self.task_manager.remove_captcha_plugin(LIST_file_path)

