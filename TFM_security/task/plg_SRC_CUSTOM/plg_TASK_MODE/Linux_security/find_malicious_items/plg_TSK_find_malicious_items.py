import sys
import os

# Add paths for imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../../plg_SRC/a0_plg_TFM')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../../plg_SRC_CUSTOM/a0_plg_CUSTOM')))

from plg_SSH import *
from plg_CSV import *
from plg_String import *
from plg_Date_time import *

class FindMaliciousItems_TaskExecutor:
    """
    Task Executor for finding malicious items on Linux servers
    Contains the single function that performs malicious item detection tasks
    """
    
    def __init__(self):
        pass
    
    def scan_for_malicious_files(self, LIST_file_path):
        """
        Main function to scan for malicious files
        """
        log2('info', 'Scanning for malicious files')
        try:
            results = []
            for server in merge_and_read_csv(LIST_file_path):
                server_ip, ssh_username, ssh_password = server_details(server)
                if server_ip:
                    try:
                        ssh_client = Ssh_into_server(server_ip, ssh_username, ssh_password)
                        if ssh_client:
                            # Scan for common malicious file patterns
                            ssh_exec(ssh_client, "find /tmp -name '*.php' -o -name '*.pl' -o -name '*.py' 2>/dev/null")
                            ssh_exec(ssh_client, "find /var/www -name '*.php' -exec grep -l 'eval(' {} \\; 2>/dev/null")
                            ssh_exec(ssh_client, "find /home -name '.*' -type f -exec file {} \\; | grep 'executable'")
                            
                            results.append(f"Malicious file scan completed on {server_ip}")
                            log2('info', f"Malicious file scan completed on {server_ip}")
                        else:
                            results.append(f"Failed to SSH into {server_ip}")
                    except Exception as e:
                        results.append(f"Error scanning for malicious files on {server_ip}: {str(e)}")
            
            return results
        except Exception as e:
            log2('error', f"An error occurred in scan_for_malicious_files: {e}")
            return [f"Error: {str(e)}"]
    
    def scan_for_suspicious_processes(self, LIST_file_path):
        """
        Main function to scan for suspicious processes
        """
        log2('info', 'Scanning for suspicious processes')
        try:
            results = []
            for server in merge_and_read_csv(LIST_file_path):
                server_ip, ssh_username, ssh_password = server_details(server)
                if server_ip:
                    try:
                        ssh_client = Ssh_into_server(server_ip, ssh_username, ssh_password)
                        if ssh_client:
                            # Check for suspicious processes
                            ssh_exec(ssh_client, "ps aux | grep -E '(nc|netcat|nmap|wget|curl)' | grep -v grep")
                            ssh_exec(ssh_client, "lsof -i | grep LISTEN")
                            ssh_exec(ssh_client, "netstat -tulpn | grep LISTEN")
                            
                            results.append(f"Suspicious process scan completed on {server_ip}")
                            log2('info', f"Suspicious process scan completed on {server_ip}")
                        else:
                            results.append(f"Failed to SSH into {server_ip}")
                    except Exception as e:
                        results.append(f"Error scanning for suspicious processes on {server_ip}: {str(e)}")
            
            return results
        except Exception as e:
            log2('error', f"An error occurred in scan_for_suspicious_processes: {e}")
            return [f"Error: {str(e)}"]
    
    def scan_for_unauthorized_connections(self, LIST_file_path):
        """
        Main function to scan for unauthorized connections
        """
        log2('info', 'Scanning for unauthorized connections')
        try:
            results = []
            for server in merge_and_read_csv(LIST_file_path):
                server_ip, ssh_username, ssh_password = server_details(server)
                if server_ip:
                    try:
                        ssh_client = Ssh_into_server(server_ip, ssh_username, ssh_password)
                        if ssh_client:
                            # Check for unauthorized connections
                            ssh_exec(ssh_client, "who")
                            ssh_exec(ssh_client, "last")
                            ssh_exec(ssh_client, "netstat -an | grep ESTABLISHED")
                            
                            results.append(f"Unauthorized connection scan completed on {server_ip}")
                            log2('info', f"Unauthorized connection scan completed on {server_ip}")
                        else:
                            results.append(f"Failed to SSH into {server_ip}")
                    except Exception as e:
                        results.append(f"Error scanning for unauthorized connections on {server_ip}: {str(e)}")
            
            return results
        except Exception as e:
            log2('error', f"An error occurred in scan_for_unauthorized_connections: {e}")
            return [f"Error: {str(e)}"]
    
    def scan_for_modified_system_files(self, LIST_file_path):
        """
        Main function to scan for modified system files
        """
        log2('info', 'Scanning for modified system files')
        try:
            results = []
            for server in merge_and_read_csv(LIST_file_path):
                server_ip, ssh_username, ssh_password = server_details(server)
                if server_ip:
                    try:
                        ssh_client = Ssh_into_server(server_ip, ssh_username, ssh_password)
                        if ssh_client:
                            # Check for modified system files
                            ssh_exec(ssh_client, "find /etc -type f -mtime -7 -ls")
                            ssh_exec(ssh_client, "find /bin -type f -mtime -7 -ls")
                            ssh_exec(ssh_client, "find /sbin -type f -mtime -7 -ls")
                            
                            results.append(f"Modified system file scan completed on {server_ip}")
                            log2('info', f"Modified system file scan completed on {server_ip}")
                        else:
                            results.append(f"Failed to SSH into {server_ip}")
                    except Exception as e:
                        results.append(f"Error scanning for modified system files on {server_ip}: {str(e)}")
            
            return results
        except Exception as e:
            log2('error', f"An error occurred in scan_for_modified_system_files: {e}")
            return [f"Error: {str(e)}"]
    
    def comprehensive_malware_scan(self, LIST_file_path):
        """
        Main function to perform comprehensive malware scan
        """
        log2('info', 'Performing comprehensive malware scan')
        try:
            results = []
            for server in merge_and_read_csv(LIST_file_path):
                server_ip, ssh_username, ssh_password = server_details(server)
                if server_ip:
                    try:
                        ssh_client = Ssh_into_server(server_ip, ssh_username, ssh_password)
                        if ssh_client:
                            # Comprehensive malware scan
                            ssh_exec(ssh_client, "rpm -Va | grep '^..5'")
                            ssh_exec(ssh_client, "find /var/log -name '*.log' -exec grep -i 'error\|warning\|failed' {} \\;")
                            ssh_exec(ssh_client, "crontab -l")
                            ssh_exec(ssh_client, "ls -la /etc/cron.*")
                            
                            results.append(f"Comprehensive malware scan completed on {server_ip}")
                            log2('info', f"Comprehensive malware scan completed on {server_ip}")
                        else:
                            results.append(f"Failed to SSH into {server_ip}")
                    except Exception as e:
                        results.append(f"Error performing comprehensive malware scan on {server_ip}: {str(e)}")
            
            return results
        except Exception as e:
            log2('error', f"An error occurred in comprehensive_malware_scan: {e}")
            return [f"Error: {str(e)}"]

