

import sys
import csv
import feedparser


# https://stackoverflow.com/questions/75249065/reading-rss-feed-in-python

# https://medium.com/@jonathanmondaut/fetching-data-from-rss-feeds-in-python-a-comprehensive-guide-a3dc86a5b7bc
def get_RSS_feed_data (rss_url):

   LIST_rss_data = []
   
   try:

      feed = feedparser.parse(rss_url)
   
      #print (feed.keys())
      rss_entry_count = len(feed.entries)
      #print (rss_entry_count)

      if feed.status == 200:
   
         for entry in feed.entries:
              
            #print(entry.title)
            #print (entry.published)        
            #print (entry.summary)
            #print(entry.link)
            #print ('\n')
         
            #LIST_rss_content.append (' ##title ' + str(entry.title.encode('utf-8')) + ' ##pulished ' + str(entry.published.encode('utf-8')) + ' ##link ' + str(entry.link.encode('utf-8')) + ' ##summary ' + str(entry.summary.encode('utf-8'))) 
            LIST_rss_data.append (' ##title ' + entry.title + ' ##pulished ' + entry.published + ' ##link ' + entry.link + ' ##summary ' + entry.summary)     
      else:
      
         print("Failed to get RSS feed. Status code:" + str(feed.status) )
      
      LIST_rss_data.insert(0, ' ##entry_count ' + str(rss_entry_count))
      
   except:
    
      print ('ERROR')
      
   #print (LIST_rss_content)
   return LIST_rss_data        

#rss_url_1 = 'https://deadspin.com/rss/'
#rss_url_1 = 'https://www.atptour.com/en/media/rss-feed/xml-feed'
#rss_url_1 = 'https://feeds.feedburner.com/FeatureShoot'
rss_url_1 = 'https://www.9news.com.au/rss'

LIST_rss_data = get_RSS_feed_data (rss_url= rss_url_1)  

'''
for x in LIST_rss_data :

   y=x.encode()
   z=str(y).replace("b'", "").replace('b"', '')
   
   print (z)
'''


#Input search query into search engine to get RSS urls by category 
def create_RSS_search_query (LIST_country, LIST_topic):

   LIST_rss_search_query = []

   for country in LIST_country:

      for rss_topic in LIST_topic:
      
         LIST_rss_search_query.append('Top rss feed ' + country + ' ' + rss_topic)
         
   
   print (LIST_rss_search_query)
   return LIST_rss_search_query

            
   
   '''
LIST_country = ['', 'China', 'Russia']
LIST_topic = ['', 'news', 'business', 'games', 'videos', 'sports', 'politics'] #can come from search query / keywords 
create_RSS_search_query(LIST_country, LIST_topic)
'''