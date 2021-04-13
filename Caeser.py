import string
import collections
#This is a library used to get all the letters


def encrypcaeser(plain_text, no_of_shift):
    
    upper = collections.deque(string.ascii_uppercase)
    lower = collections.deque(string.ascii_lowercase)
    
    upper.rotate(no_of_shift)
    lower.rotate(no_of_shift)
    
    upper = ''.join(list(upper))
    lower = ''.join(list(lower))
    
    return plain_text.translate(str.maketrans(string.ascii_uppercase, upper)).translate(str.maketrans(string.ascii_lowercase, lower))


