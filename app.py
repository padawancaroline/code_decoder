import json
from json import decoder
import streamlit as st
import streamlit.components.v1 as com
from streamlit_extras.stylable_container import stylable_container
from decoder import caesar_cipher
from decoder import vigenere_cipher

# Global variable name              # Type
message = ''                        # string
cipher_type = ''                    # string
encrypt_or_decrypt = ''             # string
keyword = ''                        # string
offset = ''                         # string
output_message = ''                 # string
offset_incremental = 1              #integer
keyword_input = ''

# lottie animation 
with stylable_container(
    key = 'hero',
    css_styles="""
    {
        border_radius: 100px;
        background: linear-gradient(315deg, #4f2991 3%, #7dc4ff 38%, #36cfcc 68%, #a92ed3 98%);
        border-radius: 20px;
        padding: 20px;
        box-shadow: 2px 3px #888888;
        }
    """
): 
    col1, col2 = st.columns([2,3])
    with col1:
        with stylable_container(
        key = 'img',
        css_styles="""
        {
            height=500, 
            width=500, 
        }
        """
        ): 
            animation = com.iframe('https://lottie.host/embed/f08465c1-b91b-4f2f-8cb9-bbe83adcd8df/HHaPOIHhnN.json')

    with col2:
        with stylable_container(
            key = 'title',
            css_styles="""
            {
                font-size:40px;
                font-color: white;
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
with st.form("encryption_form"):
        header = st.columns([3,2])
        header[0].subheader('Pick a Cipher')
        header[1].subheader('Enter your Key')

        row1 = st.columns([3,2])
        cipher_type=row1[0].selectbox('Select your cipher',['Caesar\'s Cipher', 'Vigenère\'s Cipher'])
        encrypt_or_decrypt=row1[1].radio('Pick conversion type', ['Decrypt','Encrypt'])

        row2 = st.columns([3,2])
        offset=row2[0].slider('Select offset',0, 26,10, help='Offset is what Caesar\'s Cipher takes to define the distance between the character that will be switched (if unknown pick 0)',disabled=False)
        keyword=row2[1].text_input('Enter Keyword', placeholder='Enter keyword', help='Vigenère\'s cipher uses a keyword to determine the offset value it will use',disabled=False)

        row3 = st.columns([3])
        message=row3[0].text_area('Add text you want to run through Cipher', placeholder='Enter your message here...',
        help='Text to encrypt or decrypt')
        submitted = st.form_submit_button("Submit")
if submitted:
    if cipher_type == 'Vigenère\'s Cipher':
        if encrypt_or_decrypt == 'Decrypt':
            output_message = vigenere_cipher(encrypt_or_decrypt, message, keyword)
            st.write('Yay! Secret message cracked! Let\'s encrypt your response if you are ready.')
            st.write('Decrypted message: ' + output_message)
        elif encrypt_or_decrypt == 'Encrypt':
            output_message = vigenere_cipher(encrypt_or_decrypt, message, keyword)
            st.write('Yay! Secret message encrypted! Don\'t forget to share the offset or keyword value with your fellow spy!')
            st.write('Decrypted message: ' + output_message)
        else:
            st.write('Please make sure you correctly entered the cypher parameters.')
    elif cipher_type == 'Caesar\'s Cipher':
        if encrypt_or_decrypt == 'Decrypt':
                if offset != 0:
                    output_message = caesar_cipher(encrypt_or_decrypt, message, offset)
                    st.write('Yay! Secret message encrypted! Don\'t forget to share the offset or keyword value with your fellow spy!')
                    st.write('Decrypted message: ' + output_message)
                elif offset == 0: 
                    for x in range(1,26):
                        output_message = caesar_cipher(encrypt_or_decrypt, message, offset)
                        offset_incremental += 1
                        st.write('Offset = ' + str(offset_incremental) + ': ' + output_message)
        elif encrypt_or_decrypt == 'Encrypt':
            output_message = caesar_cipher(encrypt_or_decrypt, message, offset)
            st.write('Yay! Secret message encrypted! Don\'t forget to share the offset or keyword value with your fellow spy!')
            st.write('Decrypted message: ' + output_message)
        else:
            st.write('Please make sure you correctly entered the cypher parameters.')
    else:
        st.write('Please make sure you correctly entered the cypher parameters.')        
        
        
        
        
