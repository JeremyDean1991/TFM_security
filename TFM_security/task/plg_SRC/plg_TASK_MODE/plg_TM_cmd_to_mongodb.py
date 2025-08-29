

import sys
sys.path.append('../plg_TFM/') 
sys.path.append('../plg_DICT/') 

from plg_DICT_database import * 



RAW - get a list of installed packages 

COOKED - a list of package already installed

TO_BE - a list of packages to be installed 

do_TO_BE - install the packages using subprocess or os.sys