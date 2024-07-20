import json
from json import decoder
import streamlit as st
import streamlit.components.v1 as com
from streamlit_lottie import st_lottie
from streamlit_extras.stylable_container import stylable_container
from decoder import caesar_cipher, vigenere_cipher

# Global variable name              # Type
message = ''                        # string
cipher_type = ''                    # string
encrypt_or_decrypt = ''             # string
keyword = ''                        # string
offset = ''                         # string
output_message = ''                 # string

# lottie animation 
with stylable_container(
    key = 'hero',
    css_styles="""
    {
        border_radius: 100px;
        background: linear-gradient(315deg, #4f2991 3%, #7dc4ff 38%, #36cfcc 68%, #a92ed3 98%);
        border-radius: 20px;
        padding: 20px;
        box-shadow: 2px 3px 10px #393B3B;
        }
    """
): 
    col1, col2 = st.columns([2,3])
    with col1:
        with stylable_container(
        key = 'img',
        css_styles="""
        {
            height:500;
            width:500; 
        }
        """
        ): 
            animation = com.iframe('https://lottie.host/embed/e804d59b-2d2c-4992-8926-1e71e867ec24/c6ROqey5rT.json')
        #below to display from file
        #with open('animationlock.json') as file: 
        #animation = json.load(file)

        #st_lottie(animation,
            #height=500, 
            #width=500, 
            #speed=1, 
            #loop=True, 
            #quality='high', 
            #key='lock' )

    with col2:
        with stylable_container(
            key = 'title',
            css_styles="""
            {
                font-size:40px;
                border-raduis: 2em;
                padding: 10px;
                float: center;
                }
            """
        ):
            st.title('Welcome to CipherFun!')

with stylable_container(
    key = 'header',
    css_styles="""
    {
        font-size: 30px;
        text-align: center; 
        }
    """
):
    st.header('Cipher')
with stylable_container(
    key = 'text',
    css_styles="""
    {
        text-align: center;
        }
    """
    ):
        st.caption('/`saɪfər/ - ci-pher')
        st.markdown('(noun) a secret or disguised way of writing; a code.')

#select cipher and encryption type     
#with st.form("encryption_form"):
header = st.columns([3, 2])
row1 = st.columns([3, 2])
row2 = st.columns([3, 2])
row3 = st.columns([3])

message = st.text_area('Type the message you want CipherFun to encrypt or decrypt', placeholder='Enter your message here... \n e.g. Hi Friend, I\'ve been having fun encrypting my message with CipherFun ', help='Text for CipherFun to encrypt or decrypt.')
encrypt_or_decrypt=st.radio('Pick conversion type', ['Decrypt','Encrypt'])
cipher_type = st.selectbox('Select the cipher method to use', ['Caesar\'s Cipher', 'Vigenère\'s Cipher'])

if cipher_type == "Vigenère\'s Cipher":
    keyword = st.text_input('Enter keyword', placeholder='e.g.fun, friends, cat', help='Vigenère\'s cipher uses a keyword to determine the shift value it will use.')
else:
    keyword = ''

if cipher_type == "Caesar\'s Cipher":
    offset = st.slider('Select shift/key number', 0, 26, 10, help='Shift/key number is what Caesar\'s Cipher takes to define the distance between the character that will be switched (if unknown pick 0)', disabled=False)
else:
    offset = ''

submit = st.button("Submit")

if submit:
    if message.strip():
        if cipher_type == 'Vigenère\'s Cipher':
            if keyword.strip():
                if encrypt_or_decrypt == 'Decrypt':
                    output_message = vigenere_cipher(encrypt_or_decrypt, message, keyword)
                    st.write('Yay! Secret message cracked! Let\'s encrypt your response if you are ready.')
                    st.write('Decrypted message: ' + output_message)
                elif encrypt_or_decrypt == 'Encrypt':
                    output_message = vigenere_cipher(encrypt_or_decrypt, message, keyword)
                    st.write('Yay! Secret message encrypted! Don\'t forget to share the offset or keyword value with your fellow spy!')
                    st.write('Encrypted message: ' + output_message)
                else:
                    st.write('Please make sure you correctly entered the cypher parameters.')
            else: 
                st.write('Please make sure you specified a keyword.')
        elif cipher_type == 'Caesar\'s Cipher':
            if encrypt_or_decrypt == 'Decrypt':
                if offset != 0:
                    output_message = caesar_cipher(encrypt_or_decrypt, message, offset)
                    st.write('Yay! Secret message encrypted! Don\'t forget to share the offset or keyword value with your fellow spy!')
                    st.write('Decrypted message: ' + output_message)
                elif offset == 0:
                    offset_incremental = 0
                    st.write('Here are are all the offset variations we could find.')
                    for x in range(0, 26):
                        decoded_message = caesar_cipher(encrypt_or_decrypt, message, offset)
                        st.write('Offset ' + str(offset) + ': ' + decoded_message)
                        offset += 1
            elif encrypt_or_decrypt == 'Encrypt':
                output_message = caesar_cipher(encrypt_or_decrypt, message, offset)
                st.write('Yay! Secret message encrypted! Don\'t forget to share the offset or keyword value with your fellow spy!')
                st.write('Encrypted message: ' + output_message)
            else:
                st.write('Please make sure you correctly entered the cypher parameters.')
        else:
            st.write('Please make sure you correctly entered the cypher parameters.')
    else:
        st.write('Please make sure to type in the text you want to run through cipher.')
    
        
        
