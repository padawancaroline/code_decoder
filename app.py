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
col1, col2, col3 = st.columns([1,0.5,1])
with col1:  
    with stylable_container(
        key = 'picker',
        css_styles="""
            {
            font-size: 10px;
            }
                """
    ):
        st.subheader('Pick a Cipher')
    cipher_type = st.selectbox('', 
        ['Caesar\'s Cipher',
        'Vigenère\'s Cipher'])
with col3: 
    with stylable_container(
    key = 'picker',
    css_styles="""
        {
            font-size: 10px;
        }
            """
    ):
        st.subheader('...and conversion type')
        encrypt_or_decrypt = st.radio('', ['Decrypt','Encrypt'])

#select cipher key  
with st.form("encryption_form"):    
    st.subheader('Enter your Key')
    if cipher_type == 'Caesar\'s Cipher':
        offset = st.slider('Select offset',0, 26,10, help='Offset is what Caesar\'s Cipher takes to define the distance between the character that will be switched'
            + ' (if unknown pick 0)',disabled=False)
    elif cipher_type == 'Vigenère\'s Cipher':
        keyword = st.text_input('Enter Keyword', placeholder='Placeholder goes here', help='Vigenère\'s cipher uses a keyword to determine the offset value it will use',disabled=False)
    message = st.text_area(
        'Add text you want to run through Cipher',
        placeholder='Placeholder goes here - Lorem Ipsum is simply dummy text of the printing and typesetting industry. \
        Lorem Ipsum has been the industry standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to ',
        help='Text to encrypt or decrypt')
    submit = st.form_submit_button('Hit me')


