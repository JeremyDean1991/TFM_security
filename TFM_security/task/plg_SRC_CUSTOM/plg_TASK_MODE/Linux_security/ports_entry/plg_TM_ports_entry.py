import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../../plg_SRC/a0_plg_TFM')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../../plg_SRC_CUSTOM/a0_plg_CUSTOM')))
from plg_SSH import *
from plg_CSV import *
from plg_String import *
from plg_Date_time import *
from plg_TASK_MODE.Linux_security.ports_entry.plg_TSK_ports_entry import *

class Ports_Entry_TaskManager:
    def __init__(self):
        self.task_executor = Ports_Entry_TaskExecutor()
    
    def configure_firewall_ports(self, LIST_file_path):
        """Configure firewall ports"""
        log2('info', 'Configuring firewall ports')
        return self.task_executor.configure_firewall_ports(LIST_file_path)
    
    def block_dangerous_ports(self, LIST_file_path):
        """Block dangerous ports"""
        log2('info', 'Blocking dangerous ports')
        return self.task_executor.block_dangerous_ports(LIST_file_path)
    
    def monitor_ports(self, LIST_file_path):
        """Monitor open ports"""
        log2('info', 'Monitoring ports')
        return self.task_executor.monitor_ports(LIST_file_path)

