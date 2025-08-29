

from urllib.parse import urlparse




def get_url_domain (url):

   domain = urlparse(url).netloc
   
   #print(domain)  
   return domain


'''
url_D = 'https://www.msn.com/en-au/news/other/elon-musk-wants-to-abolish-daylight-savings-time-and-it-might-actually-be-a-good-idea/ar-AA1vhPvk?ocid=hpmsn&cvid=df66ee8337364739a2cc674a8877062e&ei=21'
get_url_domain (url=url_D)
'''