
import gzip

# https://dumps.wikimedia.org/enwiki/latest/

#https://stackoverflow.com/questions/12902540/read-a-gzip-file-in-python
def read_gzip_file (gizp_path):

   with gzip.open(gzip_path,'r') as file:        
      
      for line in file:        
        
        print( line)
        
      print (len(file))
 
 
# read_gz_file (gzip_path)

'''
# import gzip and compress 
import gzip 
s = b'GeeksForGeeks@12345678'
s = gzip.compress(s) 
'''


#  https://stackoverflow.com/questions/31028815/how-to-unzip-gz-file-using-python

# using gzip.decompress(s) method 
import shutil

def gzip_to_txt_file (gzip_path, txt_path):

   with gzip.open(gzip_path, 'rb') as f_in:
   
      with open(txt_path, 'wb') as f_out:
      
         shutil.copyfileobj(f_in, f_out)

'''         
gzip_path= '../../data/raw/RAW_rss_feeds/a2_ALL_topics/Wiki keywords/enwiki-latest-all-titles.gz'
txt_path = '../../data/raw/RAW_rss_feeds/a2_ALL_topics/Wiki keywords/gzip_file.txt' 
#gzip_to_txt_file (gzip_path, txt_path)
'''         
