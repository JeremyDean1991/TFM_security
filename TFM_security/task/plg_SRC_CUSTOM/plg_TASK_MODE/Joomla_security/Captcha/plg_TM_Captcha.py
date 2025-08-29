import sys
import os

# Add paths for imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../../plg_SRC/a0_plg_TFM')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../../plg_SRC_CUSTOM/a0_plg_CUSTOM')))

from plg_SSH import *
from plg_CSV import *
from plg_String import *
from plg_Date_time import *
from plg_TASK_MODE.Joomla_security.Captcha.plg_TSK_Captcha import *

class Joomla_Captcha_TaskManager:
    """
    Task Manager for Joomla Captcha security operations
    Handles the coordination of Joomla Captcha security tasks
    """
    
    def __init__(self):
        self.task_executor = Joomla_Captcha_TaskExecutor()
    
    def setup_captcha_plugin(self, LIST_file_path):
        """
        Setup Captcha plugin on Joomla sites
        """
        log2('info', 'Setting up Captcha plugin on Joomla sites')
        return self.task_executor.setup_captcha_plugin(LIST_file_path)
    
    def configure_captcha_settings(self, LIST_file_path):
        """
        Configure Captcha settings on Joomla sites
        """
        log2('info', 'Configuring Captcha settings on Joomla sites')
        return self.task_executor.configure_captcha_settings(LIST_file_path)
    
    def enable_captcha_on_forms(self, LIST_file_path):
        """
        Enable Captcha on Joomla forms
        """
        log2('info', 'Enabling Captcha on Joomla forms')
        return self.task_executor.enable_captcha_on_forms(LIST_file_path)
    
    def disable_captcha_plugin(self, LIST_file_path):
        """
        Disable Captcha plugin on Joomla sites
        """
        log2('info', 'Disabling Captcha plugin on Joomla sites')
        return self.task_executor.disable_captcha_plugin(LIST_file_path)
    
    def remove_captcha_plugin(self, LIST_file_path):
        """
        Remove Captcha plugin from Joomla sites
        """
        log2('info', 'Removing Captcha plugin from Joomla sites')
        return self.task_executor.remove_captcha_plugin(LIST_file_path)

