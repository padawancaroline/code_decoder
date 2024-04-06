import json
import streamlit as st
from streamlit_lottie import st_lottie 

# app color
primaryColor="#F63366"
backgroundColor="#FFFFFF"
secondaryBackgroundColor="#F0F2F6"
textColor="##52697a"
font="monospace"

path = "<Provide entire Path of the downloaded JSON file>"
with open(path,"r") as file: 
    url = json.load(file) 
  
# lottie animation  
  
st.title("Adding Lottie Animation in Streamlit WebApp") 
  
st_lottie(url, 
    reverse=True, 
    height=400, 
    width=400, 
    speed=1, 
    loop=True, 
    quality='high', 
    key='Car'
)

st.title(
  'Welcome to CipherFun!'
)
st.header(
    'Cipher'
)
st.subheader(
    'a secret or disguised way of writing; a code.'
)


st.text(
  'Select your cipher'
)
cipher_type = st.selectbox(
    'Select', [
        'Caesar\'s Cipher (using offset number)',
        'Vigenère\'s Cipher (using keyword value)'
        ]
)


col1, col2 = st.columns(2)
col1.write('Column 1')
col2.write('Column 2')

# Three columns with different widths
col1, col2, col3 = st.columns([3,1,3])
# col1 is wider

# Using 'with' notation:
with col1:
    st.slider(
        'Select offset',
        0,
        26,
        10,
        help='Caesar\'s Cipher uses a number offset',
        disabled=False
    )

with col3:
    keyword = st.text_input(
        'Keyword',
        placeholder='Placeholder goes here',
        help='Vigenère\'s cipher uses a keyword',
        disabled=False
    )

message = st.text_area(
  'Add text you want to run through Cipher',
  placeholder='Placeholder goes here - Lorem Ipsum is simply dummy text of the printing and typesetting industry. \
  Lorem Ipsum has been the industry standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to ',
  help='Text to encrypt or decrypt'
)

st.button('Hit me')

#display result code

