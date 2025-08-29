
# https://stackoverflow.com/questions/71845927/get-all-titles-from-wikipedia-with-python
import requests
  
  
def get_Wiki_titles ():  
  
   S = requests.Session()

   URL = "https://it.wikipedia.org/w/api.php"

   PARAMS = {
            "action": "query",
            "format": "json",
            "list": "allpages",
            "aplimit": "max",
     }
   
   R = S.get(url=URL, params=PARAMS)
   DATA = R.json()
   PAGES = DATA["query"]["allpages"]

   full_data=[]
   full_data.extend(DATA["query"]["allpages"])

   for page in PAGES:
      print(str(page['title']).encode(), flush=True)
      
    
   print (len(PAGES))



  
def get_Wiki_titles_ALL ():

   S = requests.Session()

   URL = "https://it.wikipedia.org/w/api.php"

   PARAMS = {
            "action": "query",
            "format": "json",
            "list": "allpages",
            "aplimit": "max",
     }
   
   R = S.get(url=URL, params=PARAMS)
   DATA = R.json()
   PAGES = DATA["query"]["allpages"]

   full_data=[]
   full_data.extend(DATA["query"]["allpages"])

   while DATA["batchcomplete"] == "":
      PARAMS.update(DATA["continue"])
      R = S.get(url=URL, params=PARAMS)
      DATA = R.json()
      
      PAGES = DATA["query"]["allpages"]
      
      print (str(PAGES).encode(), flush=True)

'''  
   for page in PAGES:
   
      print (page['title'].encode(), flush=True)
'''

#get_Wiki_titles_ALL ()


def get_title_TEST ():

   url = 'https://api.wikimedia.org/core/v1/wikipedia/en/search/title'
   search_query = 'earth'
   number_of_results = 5
   parameters = {'q': search_query, 'limit': number_of_results}

   headers = {
  'Authorization': 'Bearer YOUR_ACCESS_TOKEN',
  'User-Agent': 'YOUR_APP_NAME (YOUR_EMAIL_OR_CONTACT_PAGE)'
   }

   response = requests.get(url, headers=headers, params=parameters)
   data = response.json()
   print(data)
   
   
#get_title_TEST ()   



import gzip

#https://stackoverflow.com/questions/12902540/read-a-gzip-file-in-python
def read_gz_file ():


   with gzip.open('../../data/raw/RAW_rss_feeds/a2_ALL_topics/Wiki keywords/enwiki-latest-all-titles.gz','r') as file:        
      
      for line in file:        
        
        print( line)
        
      print (len(file))
   
read_gz_file ()