import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../plg_SRC_CUSTOM/plg_TASK_MODE/Linux_security/Lynis_audit')))
from plg_TM_Lynis_audit import Lynis_audit_TaskManager

class Lynis_audit_CoreTask:
    def __init__(self):
        self.task_manager = Lynis_audit_TaskManager()
    
    def install_lynis(self, LIST_file_path):
        """Install Lynis"""
        return self.task_manager.install_lynis(LIST_file_path)
    
    def run_lynis_audit(self, LIST_file_path):
        """Run Lynis audit"""
        return self.task_manager.run_lynis_audit(LIST_file_path)
    
    def generate_lynis_report(self, LIST_file_path):
        """Generate Lynis report"""
        return self.task_manager.generate_lynis_report(LIST_file_path)
    
    def configure_lynis(self, LIST_file_path):
        """Configure Lynis"""
        return self.task_manager.configure_lynis(LIST_file_path)
    
    def remove_lynis(self, LIST_file_path):
        """Remove Lynis"""
        return self.task_manager.remove_lynis(LIST_file_path)

