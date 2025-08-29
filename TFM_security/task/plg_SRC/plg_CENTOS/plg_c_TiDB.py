

import sys
sys.path.append('../plg_CUSTOM/') 
sys.path.append('../plg_TFM/') 

from plg_SSH import * 



###TiDb####
cmd_install_tidb_server = "yum install tidb tidb-client tidb-ctl -y"
cmd_install_pd = "yum install pd -y"
cmd_install_tikv = "yum install tikv -y"

cmd_make_cluster_yaml="""
echo "
# For more information about the format of the tiup cluster topology file, consult
# https://docs.pingcap.com/tidb/stable/production-deployment-using-tiup#step-3-initialize-cluster-topology-file

# # Global variables are applied to all deployments and used as the default value of
# # the deployments if a specific deployment value is missing.
global:
  # # The OS user who runs the tidb cluster.
  user: \"tidb\"
  # # SSH port of servers in the managed cluster.
  ssh_port: 22
  # # Storage directory for cluster deployment files, startup scripts, and configuration files.
  deploy_dir: \"/tidb-deploy\"
  # # TiDB Cluster data storage directory
  data_dir: \"/tidb-data\"
  # # Supported values: \"amd64\", \"arm64\" (default: \"amd64\")
  arch: \"amd64\"

pd_servers:
  - host: 172.20.0.2

tidb_servers:
  - host: 172.20.0.3

tikv_servers:
  - host: 172.20.0.4

monitoring_servers:
  - host: 172.20.0.5

grafana_servers:
  - host: 172.20.0.6
" > cluster.yaml
"""



cmd_start_tidb_server = "tidb-server --config=tidb-server.toml"
cmd_start_pd_server = "pd-server --config=pd.toml"
cmd_start_tikv_server= "tikv-server --config=tikv.toml"

cmd_enable_tidb_server = "systemctl enable tidb; systemctl start tidb"
cmd_enable_pd_server = "tiup cluster start pd --config=pd.toml"
cmd_enable_tikv_server = "tiup cluster start tikv --config=tikv.toml"

# node status
cmd_update_tidb_node_status = (
    "sed -i 's/status: 0/status: 1/' /var/lib/tidb/tidbstate.dat"
)

## Firewall##

# fire_wall_add_pd_port = f"firewall-cmd --zone=public --add-port={server.pd_port}/tcp --permanent"
# fire_wall_add_tikv_port = f"firewall-cmd --zone=public --add-port={server.tikv_port}/tcp --permanent"
# fire_wall_add_tidb_port = f"firewall-cmd --zone=public --add-port={server.tidb_port}/tcp --permanent"
# fire_wall_add_tispark_port = f"firewall-cmd --zone=public --add-port={server.tispark_port}/tcp --permanent"
# fire_wall_reload = "firewall-cmd --reload"


# Set up TiDB cluster
cmd_setup_tidb_cluster = "tidb-ctl create-cluster"

# Stop TiDB
cmd_stop_tidb = "systemctl stop tidb"

# Configure TiDB firewall
cmd_configure_tidb_firewall_4000 = "firewall-cmd --permanent --add-port=4000/tcp"
cmd_configure_tidb_firewall_10080 = "firewall-cmd --permanent --add-port=10080/tcp"
cmd_reload_firewall = "firewall-cmd --reload"

cmd_install_firewall = "yum install firewalld -y"
#cmd_tidb_configure_firewall = "ufw allow from 0.0.0.0 to any port 4000"





#https://stackoverflow.com/questions/62656579/why-im-getting-unicodeencodeerror-charmap-codec-cant-encode-character-u2 
def test ():  
 
   #client1 = SSH_into_server (server_ip='107.150.45.226', SSH_username='root', SSH_password='Y4wxyopsvgu2!')  
   client1 = SSH_into_server (server_ip='173.208.150.146', SSH_username='root', SSH_password='Vgd9x0ay6i7p!')  
   #_stdin_1, _stdout_1,_stderr_1 = client1.exec_command(test_print (msg1="man", msg2=" fuck"))
   
   _stdin_1, _stdout_1,_stderr_1 = client1.exec_command(get_filesystem_space(option="2"))
   _stdin_2, _stdout_2,_stderr_2 = client1.exec_command("lsblk")

   #encoding = locale.getpreferredencoding()

   print(_stdout_1.read().decode())
   print ('\n')
   #print(_stdout_2.read().decode(encoding))
   print(_stdout_2.read().decode('ascii', 'ignore'))

   client1.close()
   
test()