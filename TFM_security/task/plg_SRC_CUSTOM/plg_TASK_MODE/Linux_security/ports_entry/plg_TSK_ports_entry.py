import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../../plg_SRC/a0_plg_TFM')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../../plg_SRC_CUSTOM/a0_plg_CUSTOM')))
from plg_SSH import *
from plg_CSV import *
from plg_String import *
from plg_Date_time import *

class Ports_Entry_TaskExecutor:
    def configure_firewall_ports(self, LIST_file_path):
        try:
            results = []
            for server in merge_and_read_csv(LIST_file_path):
                server_ip, ssh_username, ssh_password = server_details(server)
                if server_ip:
                    ssh_client = Ssh_into_server(server_ip, ssh_username, ssh_password)
                    if ssh_client:
                        ssh_exec(ssh_client, "systemctl start firewalld")
                        ssh_exec(ssh_client, "firewall-cmd --permanent --add-service=ssh")
                        ssh_exec(ssh_client, "firewall-cmd --reload")
                        results.append(f"Firewall configured on {server_ip}")
            return results
        except Exception as e:
            return [f"Error: {str(e)}"]

    def block_dangerous_ports(self, LIST_file_path):
        try:
            results = []
            for server in merge_and_read_csv(LIST_file_path):
                server_ip, ssh_username, ssh_password = server_details(server)
                if server_ip:
                    ssh_client = Ssh_into_server(server_ip, ssh_username, ssh_password)
                    if ssh_client:
                        ssh_exec(ssh_client, "firewall-cmd --permanent --add-rich-rule='rule family=\"ipv4\" port port=\"23\" protocol=\"tcp\" reject'")
                        ssh_exec(ssh_client, "firewall-cmd --reload")
                        results.append(f"Dangerous ports blocked on {server_ip}")
            return results
        except Exception as e:
            return [f"Error: {str(e)}"]

    def monitor_ports(self, LIST_file_path):
        try:
            results = []
            for server in merge_and_read_csv(LIST_file_path):
                server_ip, ssh_username, ssh_password = server_details(server)
                if server_ip:
                    ssh_client = Ssh_into_server(server_ip, ssh_username, ssh_password)
                    if ssh_client:
                        ssh_exec(ssh_client, "netstat -tuln > /tmp/open_ports.txt")
                        results.append(f"Ports monitored on {server_ip}")
            return results
        except Exception as e:
            return [f"Error: {str(e)}"]
