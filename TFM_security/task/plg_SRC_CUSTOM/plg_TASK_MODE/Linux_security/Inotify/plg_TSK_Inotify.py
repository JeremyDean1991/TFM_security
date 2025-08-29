import sys
import os

# Add paths for imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../../plg_SRC/a0_plg_TFM')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../../plg_SRC_CUSTOM/a0_plg_CUSTOM')))

from plg_SSH import *
from plg_CSV import *
from plg_String import *
from plg_Date_time import *

class Inotify_TaskExecutor:
    """
    Task Executor for Inotify file system monitoring
    Contains the core logic for file system monitoring operations
    """
    
    def setup_inotify_monitoring(self, LIST_file_path):
        """
        Setup Inotify monitoring on target servers
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
                    
                    install_cmd = "yum install -y inotify-tools" if "centos" in server.get('OS', '').lower() else "apt-get install -y inotify-tools"
                    result = execute_ssh_command(ssh, install_cmd)
                    
                    if result['success']:
                        log2('info', f'Inotify installed on {server["IP"]}')
                        results.append({'server': server['IP'], 'status': 'success', 'message': 'Inotify installed'})
                    else:
                        log2('error', f'Failed to install Inotify on {server["IP"]}: {result["error"]}')
                        results.append({'server': server['IP'], 'status': 'error', 'message': result['error']})
                    
                    ssh.close()
                    
                except Exception as e:
                    log2('error', f'Error setting up Inotify on {server["IP"]}: {str(e)}')
                    results.append({'server': server['IP'], 'status': 'error', 'message': str(e)})
            
            return results
            
        except Exception as e:
            log2('error', f'Error in setup_inotify_monitoring: {str(e)}')
            return False
    
    def configure_inotify_watches(self, LIST_file_path):
        """
        Configure Inotify watch directories
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
                        continue
                    
                    monitor_script = '''#!/bin/bash
WATCH_DIRS="/var/www /etc /home"
LOG_FILE="/var/log/inotify_monitor.log"

for dir in $WATCH_DIRS; do
    if [ -d "$dir" ]; then
        inotifywait -m -r -e modify,create,delete,move "$dir" >> "$LOG_FILE" 2>&1 &
        echo "Monitoring $dir"
    fi
done
'''
                    
                    result = execute_ssh_command(ssh, f'echo "{monitor_script}" > /usr/local/bin/inotify_monitor.sh')
                    if result['success']:
                        execute_ssh_command(ssh, 'chmod +x /usr/local/bin/inotify_monitor.sh')
                        results.append({'server': server['IP'], 'status': 'success', 'message': 'Monitoring script configured'})
                    else:
                        results.append({'server': server['IP'], 'status': 'error', 'message': 'Failed to configure monitoring script'})
                    
                    ssh.close()
                    
                except Exception as e:
                    results.append({'server': server['IP'], 'status': 'error', 'message': str(e)})
            
            return results
            
        except Exception as e:
            log2('error', f'Error in configure_inotify_watches: {str(e)}')
            return False
    
    def start_inotify_monitoring(self, LIST_file_path):
        """
        Start Inotify monitoring service
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
                    
                    result = execute_ssh_command(ssh, '/usr/local/bin/inotify_monitor.sh')
                    if result['success']:
                        results.append({'server': server['IP'], 'status': 'success', 'message': 'Monitoring started'})
                    else:
                        results.append({'server': server['IP'], 'status': 'error', 'message': 'Failed to start monitoring'})
                    
                    ssh.close()
                    
                except Exception as e:
                    results.append({'server': server['IP'], 'status': 'error', 'message': str(e)})
            
            return results
            
        except Exception as e:
            log2('error', f'Error in start_inotify_monitoring: {str(e)}')
            return False
    
    def stop_inotify_monitoring(self, LIST_file_path):
        """
        Stop Inotify monitoring service
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
                    
                    execute_ssh_command(ssh, 'pkill -f inotifywait')
                    results.append({'server': server['IP'], 'status': 'success', 'message': 'Monitoring stopped'})
                    
                    ssh.close()
                    
                except Exception as e:
                    results.append({'server': server['IP'], 'status': 'error', 'message': str(e)})
            
            return results
            
        except Exception as e:
            log2('error', f'Error in stop_inotify_monitoring: {str(e)}')
            return False
    
    def remove_inotify(self, LIST_file_path):
        """
        Remove Inotify from target servers
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
                    
                    execute_ssh_command(ssh, 'pkill -f inotifywait')
                    execute_ssh_command(ssh, 'rm -f /usr/local/bin/inotify_monitor.sh')
                    execute_ssh_command(ssh, 'rm -f /var/log/inotify_monitor.log')
                    
                    uninstall_cmd = "yum remove -y inotify-tools" if "centos" in server.get('OS', '').lower() else "apt-get remove -y inotify-tools"
                    execute_ssh_command(ssh, uninstall_cmd)
                    
                    results.append({'server': server['IP'], 'status': 'success', 'message': 'Inotify removed'})
                    ssh.close()
                    
                except Exception as e:
                    results.append({'server': server['IP'], 'status': 'error', 'message': str(e)})
            
            return results
            
        except Exception as e:
            log2('error', f'Error in remove_inotify: {str(e)}')
            return False
