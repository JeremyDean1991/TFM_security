
from a0_items import * 

import sys
sys.path.append('../plg_TFM/') 



def str_to_lowercase (string):

   lower_str = string.lower()

   return lower_str
   
#print (str_to_lowercase (string='ABC_HELLO'))

 
 
def LIST_2_letter_str ():

   LIST_letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

   LIST_first_2_letters = []
   
   for x in LIST_letter:

      for y in LIST_letter:
   
         z = x+y
         #print (z)
         
         LIST_first_2_letters.append(z)
   
   return LIST_first_2_letters
   
#print (len(LIST_2_letter_str ()))
         
      
      
     
def check_str_index (string, start_index, end_index):

   first_N_chars = string [start_index:end_index]
   
   return first_N_chars      
      

#print(check_str_index (string='shane fang', start_index=0, end_index=2))



def get_Nth_letter (string, str_index):

   Nth_letter = string[str_index]
   
   return Nth_letter
   

'''
str_1 = "hey ohw are u"   
letter_1 = get_Nth_letter (string = str_1, str_index = 2)   

print (letter_1)
'''



# https://stackoverflow.com/questions/25346058/removing-list-of-words-from-a-string

def remove_words_from_text (LIST_word_to_remove, txt_main):

   LIST_txt_main = txt_main.split()
   
   LIST_saved_txt = []
     
   for word in LIST_txt_main:
   
      if word.lower() in LIST_word_to_remove:
      
         print ('words removed => ' + word)
                 
      else:
      
         print ('words NOT removed => ' + word)
         LIST_saved_txt.append(word)
         
                  
   new_txt_main = ' '.join(LIST_new_txt)
   
   print (LIST_saved_txt)
   print (new_txt_main)   
   return LIST_saved_txt, new_txt_main 
         
     
'''
txt_main = 'What is hello shane'
LIST_word_to_remove = ['what', 'who', 'is', 'a', 'at', 'is', 'he']     
remove_words_from_text (LIST_word_to_remove, txt_main)
'''


# compare two strings to get the output string which has the same letters in both strings 
def get_same_string(str1, str2):

   LIST_letter_same = []
   LIST_letter_diff = []

   for str1_letter, str2_letter in zip(str1, str2):
    
       if str1_letter != str2_letter:
            
           #print (' diff => ' + str1_letter +str2_letter)
           LIST_letter_diff.append(str1_letter + str2_letter)
                                    
       else:
       
           #print (' same => ' + str1_letter+str2_letter)
           LIST_letter_same.append(str1_letter)
            
            
   same_string = ''.join(LIST_letter_same)
   
   print (same_string)
   return same_string

'''
link_1 ='https://www.youtube.com/watch?v=4N4rq4PVoe4'
link_2 = 'https://www.youtube.com/watch?v=OhRwppJWyBI'

get_same_string(str1=link_1, str2 = link_2)
'''