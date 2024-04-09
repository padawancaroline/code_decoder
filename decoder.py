import json
import streamlit as st
import streamlit.components.v1 as com
from streamlit_lottie import st_lottie
from streamlit_extras.stylable_container import stylable_container

# Global variable name              # Type
message = ''                        # string
cipher_type = ''                    # string
encrypt_or_decrypt = ''             # string
keyword = ''                        # string
offset = ''                         # string
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
            if encrypt_or_decrypt == 'Decrypt':
                output_message_v += alphabet[(character_index + keyword_offset_index) % 26]
            # Encryption
            elif encrypt_or_decrypt == 'Encrypt':
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
            if encrypt_or_decrypt == 'Decrypt':
                character_index = alphabet.find(character)
                output_message_c += alphabet[(character_index + offset) % 26]
                # Encryption
            elif encrypt_or_decrypt == 'Encrypt':
                output_message_c += alphabet[(character_index - offset) % 26]
        #if character is a special character, add character as is
        else: 
            output_message_c += character
    return output_message_c