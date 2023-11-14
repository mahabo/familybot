import openai
import streamlit as st
from PIL import Image



def generate_image(image_description):
  img_response = openai.Image.create(
    prompt = image_description,
    n=1,
    size="512x512")
  img_url = img_response['data'][0]['url']
  return img_url

st.title("💬 Mark's OPEN AI Family Chatbot")


st.write('<style>div.row-widget.stRadio > div{flex-direction:row;justify-content: center;} </style>', unsafe_allow_html=True)
st.write('<style>div.st-bf{flex-direction:column;} div.st-ag{font-weight:bold;padding-left:2px;}</style>', unsafe_allow_html=True)
choose=st.radio(" ",(" Text Chat"," Picture"))
st.caption("___________________________________________________")

if "messages" not in st.session_state:
   st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
    
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    
    
    if choose == ' Text Chat':
       
       # add your Azure API Keys
       openai.api_type = "azure"
       openai.api_base = 'xxx'
       openai.api_version = "xxx"
       openai.api_key = 'xxx'
       response = openai.ChatCompletion.create(engine="xxx",messages=st.session_state.messages) 
       msg = response.choices[0].message
       st.session_state.messages.append(msg)
       st.chat_message("assistant").write(msg.content)  	
    else: 
       
       # add your Dall-E Azure API Keys
       openai.api_base = 'xxx'
       openai.api_key = 'xxx'     
       # Assign the API version (DALL-E is currently supported for the 2023-06-01-preview API version only)
       openai.api_version = 'xxx'
       openai.api_type = 'azure'
       generated_img = generate_image(prompt)
       st.image(generated_img)

    
