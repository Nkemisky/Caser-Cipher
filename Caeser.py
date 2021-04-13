import string
import collections
#This is a library used to get all the letters


def encrypcaeser(plain_text, no_of_shift):
    
    upper = collections.deque(string.ascii_uppercase)
    lower = collections.deque(string.ascii_lowercase)
    
    upper.rotate(no_of_shift)
    lower.rotate(no_of_shift)
    
    

