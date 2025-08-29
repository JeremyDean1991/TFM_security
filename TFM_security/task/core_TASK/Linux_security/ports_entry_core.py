import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../plg_SRC_CUSTOM/plg_TASK_MODE/Linux_security/ports_entry')))
from plg_TM_ports_entry import Ports_Entry_TaskManager

class Ports_Entry_CoreTask:
    def __init__(self):
        self.task_manager = Ports_Entry_TaskManager()
    
    def configure_firewall_ports(self, LIST_file_path):
        """Configure firewall ports"""
        return self.task_manager.configure_firewall_ports(LIST_file_path)
    
    def block_dangerous_ports(self, LIST_file_path):
        """Block dangerous ports"""
        return self.task_manager.block_dangerous_ports(LIST_file_path)
    
    def monitor_ports(self, LIST_file_path):
        """Monitor open ports"""
        return self.task_manager.monitor_ports(LIST_file_path)

