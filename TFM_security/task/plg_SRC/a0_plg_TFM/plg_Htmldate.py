

from htmldate import find_date




def get_html_page_date (url):

   page_date = find_date(url)
   
   print (page_date, flush=True)
   return page_date
   
'''
#url123 ='https://stackoverflow.com/questions/33771712/find-date-in-generic-webpage-using-python'
url123 ='https://www.youtube.com/watch?v=ZapTCgZzVec'

get_html_page_date (url=url123)  
'''