

from a0_items import *
import os



def read_TXT_file (path_TXT):

   with open(path_TXT, 'r' ,  encoding='UTF-8') as file:
   
      LIST_line = file.readlines()
           
   return LIST_line
   
   
# print(read_TXT_file (path_TXT='shaneTXT.txt')  ) 



def create_TXT_file (path_TXT):

   if os.path.exists(path_TXT):
   
      print (path_TXT + ' alraedy exists')
      
   else:
  
      with open(path_TXT, 'w') as f: 
         pass #create an empty text file 
     
      print (path_TXT + ' NOT exists, is created!')


#create_TXT_file (path_TXT='shaneHELLO.txt')




# write 1 line only 
def write_to_TXT_file_1 (path_TXT, line_to_write):

   with open(path_TXT, "a+") as file:
      
      #write 1 line only
      file.write(line_to_write)




#write multiple lines at once 
def write_to_TXT_file_2 (path_TXT, LIST_to_write):

   with open(path_TXT, "a+") as file:

      #Use writelines() to write the list of strings to the file
      file.writelines(LIST_to_write)

'''
# Step 2: Create a list of strings, where each string represents a line
LIST_lines = [
     "This is the first line \n",
     "This is the second line \n",
     "This is the third line \n"
    ]
    
write_to_TXT_file_2 (path_TXT='shaneTXT.txt', lines_to_write = LIST_lines)
'''


def write_to_TXT_file_3 (path_TXT, LIST_to_write):

   with open(path_TXT, "w") as file:

      # Use writelines() to write the list of strings to the file. 
      # Cannot write a list, only a list of strings 
      file.writelines(LIST_to_write)




def rewrite_txt_line (path_TXT, line_num, rewrite_line_to):

   LIST_value = read_TXT_file (path_TXT=path_TXT)
   
   LIST_value [line_num] = rewrite_line_to
   
   write_to_TXT_file_3 (path_TXT=path_TXT, LIST_to_write=LIST_value)




def append_txt_line (path_TXT, line_num, txt_to_append):

   LIST_value = read_TXT_file (path_TXT=path_TXT)
   
   LIST_value.insert(line_num, str(txt_to_append))
   
   # Cannot write a list, only a list of strings 
   write_to_TXT_file_3 (path_TXT=path_TXT, LIST_to_write=LIST_value)   
   
   
   


def delete_TXT_file (path_TXT):

   if os.path.exists(path_TXT):
      os.remove(path_TXT)
      
      
   else:
     print(path_TXT + " NOT exists")
   
   
#delete_TXT_file (path_TXT)   
   

def get_file_num(full_file_path, file_prefix, file_extension):

   file_num = remove_all_before_and_after_texts (before_text=file_prefix, after_text=file_extension, text_main=full_file_path)
   INT_file_num = int(file_num)
   
   return INT_file_num


