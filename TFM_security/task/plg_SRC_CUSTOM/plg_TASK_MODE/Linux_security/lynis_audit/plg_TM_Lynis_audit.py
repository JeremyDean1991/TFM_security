import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../../plg_SRC/a0_plg_TFM')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../../plg_SRC_CUSTOM/a0_plg_CUSTOM')))
from plg_SSH import *
from plg_CSV import *
from plg_String import *
from plg_Date_time import *
from plg_TASK_MODE.Linux_security.Lynis_audit.plg_TSK_Lynis_audit import *

class Lynis_audit_TaskManager:
    def __init__(self):
        self.task_executor = Lynis_audit_TaskExecutor()
    
    def install_lynis(self, LIST_file_path):
        """Install Lynis on target servers"""
        log2('info', 'Installing Lynis')
        return self.task_executor.install_lynis(LIST_file_path)
    
    def run_lynis_audit(self, LIST_file_path):
        """Run Lynis security audit"""
        log2('info', 'Running Lynis audit')
        return self.task_executor.run_lynis_audit(LIST_file_path)
    
    def generate_lynis_report(self, LIST_file_path):
        """Generate Lynis audit report"""
        log2('info', 'Generating Lynis report')
        return self.task_executor.generate_lynis_report(LIST_file_path)
    
    def configure_lynis(self, LIST_file_path):
        """Configure Lynis settings"""
        log2('info', 'Configuring Lynis')
        return self.task_executor.configure_lynis(LIST_file_path)
    
    def remove_lynis(self, LIST_file_path):
        """Remove Lynis from target servers"""
        log2('info', 'Removing Lynis')
        return self.task_executor.remove_lynis(LIST_file_path)

