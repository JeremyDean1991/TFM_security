

import sys
sys.path.append('../plg_CUSTOM/') 
sys.path.append('../plg_TFM/') 

from plg_SSH import * 


### 7zip for file zip -- https://elearning.wsldp.com/pcmagazine/extract-7zip-centos-7/
cmd_install_p7zip = 'yes | sudo yum install p7zip'

#https://unix.stackexchange.com/questions/470266/how-to-locate-a-package-installed-by-yum/470458
cmd_p7zip_install_path = 'rpm -q --filesbypkg p7zip'
cmd_search_7zip_version = 'yum search 7zip'
cmd_info_7zip_version = 'yum info 7zip'

cmd_remove_p7zip = 'yes | yum remove p7zip'
cmd_update_after_remove_7zip = 'yum update'