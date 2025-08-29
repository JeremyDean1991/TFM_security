import sys
import os

# Add paths for imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../../plg_SRC/a0_plg_TFM')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../../plg_SRC_CUSTOM/a0_plg_CUSTOM')))

from plg_SSH import *
from plg_CSV import *
from plg_String import *
from plg_Date_time import *

class Lynis_audit_TaskExecutor:
    """
    Task Executor for Lynis security auditing
    Contains the core logic for security auditing operations
    """
    
    def install_lynis(self, LIST_file_path):
        """
        Install Lynis on target servers
        """
        try:
            servers = read_csv(LIST_file_path)
            if not servers:
                log2('error', 'No servers found in CSV file')
                return False
            
            results = []
            for server in servers:
                try:
                    ssh = connect_ssh(server['IP'], server['USERNAME'], server['PASSWORD'])
                    if not ssh:
                        log2('error', f'Failed to connect to {server["IP"]}')
                        continue
                    
                    install_cmd = "yum install -y lynis" if "centos" in server.get('OS', '').lower() else "apt-get install -y lynis"
                    result = execute_ssh_command(ssh, install_cmd)
                    
                    if result['success']:
                        log2('info', f'Lynis installed on {server["IP"]}')
                        results.append({'server': server['IP'], 'status': 'success', 'message': 'Lynis installed'})
                    else:
                        log2('error', f'Failed to install Lynis on {server["IP"]}: {result["error"]}')
                        results.append({'server': server['IP'], 'status': 'error', 'message': result['error']})
                    
                    ssh.close()
                    
                except Exception as e:
                    log2('error', f'Error installing Lynis on {server["IP"]}: {str(e)}')
                    results.append({'server': server['IP'], 'status': 'error', 'message': str(e)})
            
            return results
            
        except Exception as e:
            log2('error', f'Error in install_lynis: {str(e)}')
            return False

    def run_lynis_audit(self, LIST_file_path):
        """
        Run Lynis security audit
        """
        try:
            servers = read_csv(LIST_file_path)
            if not servers:
                return False
            
            results = []
            for server in servers:
                try:
                    ssh = connect_ssh(server['IP'], server['USERNAME'], server['PASSWORD'])
                    if not ssh:
                        continue
                    
                    result = execute_ssh_command(ssh, 'lynis audit system --quick')
                    if result['success']:
                        results.append({'server': server['IP'], 'status': 'success', 'message': 'Lynis audit completed'})
                    else:
                        results.append({'server': server['IP'], 'status': 'error', 'message': 'Lynis audit failed'})
                    
                    ssh.close()
                    
                except Exception as e:
                    results.append({'server': server['IP'], 'status': 'error', 'message': str(e)})
            
            return results
            
        except Exception as e:
            log2('error', f'Error in run_lynis_audit: {str(e)}')
            return False

    def generate_lynis_report(self, LIST_file_path):
        """
        Generate Lynis audit report
        """
        try:
            servers = read_csv(LIST_file_path)
            if not servers:
                return False
            
            results = []
            for server in servers:
                try:
                    ssh = connect_ssh(server['IP'], server['USERNAME'], server['PASSWORD'])
                    if not ssh:
                        continue
                    
                    result = execute_ssh_command(ssh, 'lynis audit system --quick --report-file /tmp/lynis_report.txt')
                    if result['success']:
                        results.append({'server': server['IP'], 'status': 'success', 'message': 'Report generated'})
                    else:
                        results.append({'server': server['IP'], 'status': 'error', 'message': 'Failed to generate report'})
                    
                    ssh.close()
                    
                except Exception as e:
                    results.append({'server': server['IP'], 'status': 'error', 'message': str(e)})
            
            return results
            
        except Exception as e:
            log2('error', f'Error in generate_lynis_report: {str(e)}')
            return False

    def configure_lynis(self, LIST_file_path):
        """
        Configure Lynis settings
        """
        try:
            servers = read_csv(LIST_file_path)
            if not servers:
                return False
            
            results = []
            for server in servers:
                try:
                    ssh = connect_ssh(server['IP'], server['USERNAME'], server['PASSWORD'])
                    if not ssh:
                        continue
                    
                    profile_content = 'PROFILE="custom"\nSKIP_TESTS=""\nSKIP_CONTENT=""\nSKIP_PRIVILEGED_TESTS=""'
                    result = execute_ssh_command(ssh, f'echo "{profile_content}" > /etc/lynis/default.prf')
                    if result['success']:
                        results.append({'server': server['IP'], 'status': 'success', 'message': 'Lynis profile configured'})
                    else:
                        results.append({'server': server['IP'], 'status': 'error', 'message': 'Failed to configure profile'})
                    
                    ssh.close()
                    
                except Exception as e:
                    results.append({'server': server['IP'], 'status': 'error', 'message': str(e)})
            
            return results
            
        except Exception as e:
            log2('error', f'Error in configure_lynis: {str(e)}')
            return False

    def remove_lynis(self, LIST_file_path):
        """
        Remove Lynis from target servers
        """
        try:
            servers = read_csv(LIST_file_path)
            if not servers:
                return False
            
            results = []
            for server in servers:
                try:
                    ssh = connect_ssh(server['IP'], server['USERNAME'], server['PASSWORD'])
                    if not ssh:
                        continue
                    
                    uninstall_cmd = "yum remove -y lynis" if "centos" in server.get('OS', '').lower() else "apt-get remove -y lynis"
                    execute_ssh_command(ssh, uninstall_cmd)
                    execute_ssh_command(ssh, 'rm -f /etc/lynis/default.prf')
                    execute_ssh_command(ssh, 'rm -f /tmp/lynis_report.txt')
                    
                    results.append({'server': server['IP'], 'status': 'success', 'message': 'Lynis removed'})
                    ssh.close()
                    
                except Exception as e:
                    results.append({'server': server['IP'], 'status': 'error', 'message': str(e)})
            
            return results
            
        except Exception as e:
            log2('error', f'Error in remove_lynis: {str(e)}')
            return False

