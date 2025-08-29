import sys
import os

# Add paths for imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../../plg_SRC/a0_plg_TFM')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../../plg_SRC_CUSTOM/a0_plg_CUSTOM')))

from plg_SSH import *
from plg_CSV import *
from plg_String import *
from plg_Date_time import *
from plg_TASK_MODE.Linux_security.find_malicious_items.plg_TSK_find_malicious_items import *

class FindMaliciousItems_TaskManager:
    """
    Task Manager for finding malicious items on Linux servers
    Handles the coordination of malicious file detection tasks
    """
    
    def __init__(self):
        self.task_executor = FindMaliciousItems_TaskExecutor()
    
    def scan_for_malicious_files(self, LIST_file_path):
        """
        Scan for malicious files on target servers
        """
        log2('info', 'Scanning for malicious files')
        return self.task_executor.scan_for_malicious_files(LIST_file_path)
    
    def scan_for_suspicious_processes(self, LIST_file_path):
        """
        Scan for suspicious processes on target servers
        """
        log2('info', 'Scanning for suspicious processes')
        return self.task_executor.scan_for_suspicious_processes(LIST_file_path)
    
    def scan_for_unauthorized_connections(self, LIST_file_path):
        """
        Scan for unauthorized network connections
        """
        log2('info', 'Scanning for unauthorized connections')
        return self.task_executor.scan_for_unauthorized_connections(LIST_file_path)
    
    def scan_for_modified_system_files(self, LIST_file_path):
        """
        Scan for modified system files
        """
        log2('info', 'Scanning for modified system files')
        return self.task_executor.scan_for_modified_system_files(LIST_file_path)
    
    def comprehensive_malware_scan(self, LIST_file_path):
        """
        Perform comprehensive malware scan
        """
        log2('info', 'Performing comprehensive malware scan')
        return self.task_executor.comprehensive_malware_scan(LIST_file_path)

