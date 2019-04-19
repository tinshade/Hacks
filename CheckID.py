# Python script to extract emails from the String By Regular Expression.  
# Importing module required for regular expressions
import re  
  
# Example string  
s = 'Hello from mail@gmail.com to something@yahoo.com'

#To Extract only email IDs from the string  
# @ for as in the Email 
# + for Repeats a character one or more times 
lst = re.findall(r'mailID+@\S+', s)     
  
# Printing of List 
print(lst) 

# Example String  
s1 = 'shutdown'

sub = re.findall('shutdown', s1)     
if not sub:
  print("List is empty")
# Printing of List 
print(sub)
print(type(sub))