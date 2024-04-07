# Global variable name              # Type
message = ''                        # string
cipher_type = ''                    # string
encrypt_or_decrypt = ''             # string
keyword = ''                        # string
offset = ''                         # string
output_message = ''                 # string
offset_incremental = 1              #integer

#define alphabet
import string
alphabet = string.ascii_lowercase
#print (alphabet)           #uncomment for QA validation

def vigenere_cipher(encrypt_or_decrypt, message, keyword):
    #function variables
    keyword_phrase = ''
    keyword_index = 0
    output_message_v = ''
    message_lower = message.lower()

    #Step 1: define length of keyword phrase to match message
    for character in message_lower:
        #reset keyword index to keep cycling through keyword
        if keyword_index >= len(keyword):
            keyword_index = 0
        # create keyword letter sequence by repeting the keyword letters based on len(message)
        if character in alphabet:
            keyword_phrase += keyword[keyword_index]
            keyword_index += 1
        else:
            keyword_phrase += character 
        
    #Step 2: decode message based on index diff between message and keyword phrase letter position
    for i in range(len(message)):
        if message_lower[i] in alphabet:
            character_index = alphabet.find(message_lower[i])
            keyword_offset_index = alphabet.find(keyword_phrase[i])
            # Decryption
            if encrypt_or_decrypt == 'd':
                output_message_v += alphabet[(character_index + keyword_offset_index) % 26]
            # Encryption
            elif encrypt_or_decrypt == 'e':
                output_message_v += alphabet[(character_index - keyword_offset_index) % 26]
        else:
            output_message_v += message[i]
    return output_message_v

def caesar_cipher(encrypt_or_decrypt, message, offset):
    #function variables
    output_message_c = ''
    message_lower = message.lower()
    
    
    # Cipher logic
    #if character is a letter, decode by finding decoded letter position
    for character in message_lower:
        if character in alphabet:
            character_index = alphabet.find(character)
            # Decryption
            if encrypt_or_decrypt == 'd':
                if offset != 0:
                    character_index = alphabet.find(character)
                    output_message_c += alphabet[(character_index + offset) % 26]
                elif offset == 0:
                    output_message_c += alphabet[(character_index + (offset_incremental)) % 26]
                else: 
                    output_message_c += character
                # Encryption
            elif encrypt_or_decrypt == 'e':
                output_message_c += alphabet[(character_index - offset) % 26]
        #if character is a special character, add character as is
        else: 
            output_message_c += character
    return output_message_c



if cipher_type == 'v':
    if encrypt_or_decrypt == 'd':
        output_message = vigenere_cipher(encrypt_or_decrypt, message, keyword)
        print('Yay! Secret message cracked! Let\'s encrypt your response if you are ready.')
        print('Decrypted message: {decrypted}'.format(decrypted=output_message))
    elif encrypt_or_decrypt == 'e':
        output_message = vigenere_cipher(encrypt_or_decrypt, message, keyword)
        print('Yay! Secret message encrypted! Don\'t forget to share the offset or keyword value with your fellow spy!')
        print('Decrypted message: {encrypted}'.format(encrypted=output_message))
    else:
        print('Please make sure you correctly entered the cypher parameters.')
elif cipher_type == 'c':
    if encrypt_or_decrypt == 'd':
            if offset != 0:
                output_message = caesar_cipher(encrypt_or_decrypt, message, offset)
                print('Yay! Secret message encrypted! Don\'t forget to share the offset or keyword value with your fellow spy!')
                print('Decrypted message: {decrypted}'.format(decrypted=output_message))
            elif offset == 0: 
                for x in range(1,26):
                    output_message = caesar_cipher(encrypt_or_decrypt, message, offset)
                    offset_incremental += 1
                    print('Offset = ' + str(offset_incremental) + ': ' + output_message)
    elif encrypt_or_decrypt == 'e':
        output_message = caesar_cipher(encrypt_or_decrypt, message, offset)
        print('Yay! Secret message encrypted! Don\'t forget to share the offset or keyword value with your fellow spy!')
        print('Decrypted message: {encrypted}'.format(encrypted=output_message))
    else:
        print('Please make sure you correctly entered the cypher parameters.')
else:
    print('Please make sure you correctly entered the cypher parameters.')