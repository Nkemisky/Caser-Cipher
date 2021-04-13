import string


plaintext = input('Enter your text: ')
key = input(': ')


def caeser(input_text,key):
    ciphertext = ""
   
    input_text = plaintext.lower() 
    for c in input_text:
       
       if c in string.ascii_letters:
           temp = ord(c) + int(key)
           
           if temp > ord('z'):
               temp = temp - 26
               
           ciphertext = ciphertext + chr(temp)
       else:
            ciphertext = ciphertext + c
            
    return ciphertext





