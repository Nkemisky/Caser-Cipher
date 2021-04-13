import string


plaintext = input('Enter your text: ')
key = input('Enter your secret key: ')
is_encrypt = input('Are you encrypting or decrypting? Enter 1 for encrypting and 0 for decrypting: ')

if is_encrypt == '0':
    key = 26 - int(key)


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


print(caeser(plaintext, key))


