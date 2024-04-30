import os
from dotenv import load_dotenv
from openai import OpenAI
import streamlit as st

# 加载 .env 文件中的环境变量
load_dotenv()

# 从环境变量获取 API 密钥
api_key = os.getenv('OPENAI_API_KEY')

# 创建 OpenAI API 客户端
client = OpenAI()

st.set_page_config(
    page_title="English Speaking Practice Tool",
    page_icon="👨🏻‍💻",
    layout="wide",  # centered or wide
    initial_sidebar_state="auto",
)

# 口语翻译
def translate_to_english(user_input):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": f"Translate the following text into American English suitable for informal conversation: '{user_input}'"},
        ],
        temperature=0.5,
        top_p=1.0
    )
    return response.choices[0].message.content

def conversation_reply(user_input):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a native American English speaker engaged in a friendly, informal conversation. Keep the dialogue engaging and natural."},
            {"role": "user", "content": user_input}
        ],
        temperature=0.9,
        top_p=1.0
    )
    return response.choices[0].message.content


# Initialize session state for conversation history and user input
if 'user_input' not in st.session_state:
    st.session_state['user_input'] = ""
if 'display_text_translation' not in st.session_state:
    st.session_state['display_text_translation'] = ""
if 'display_text_dialogue' not in st.session_state:
    st.session_state['display_text_dialogue'] = ""

# Layout configuration
st.title('English Speaking Practice Tool')

# Mode selector at the top
mode = st.radio("Select Mode:", ["Spoken Translation", "Spoken Dialogue"], index=0, help="Choose 'Spoken Translation' to translate text into English or 'Spoken Dialogue' to have a conversation in English.")

# Current conversation display in the middle
st.subheader("Current Conversation")
if 'display_text_translation' in st.session_state and mode == "Spoken Translation":
    st.text(st.session_state['display_text_translation'])
if 'display_text_dialogue' in st.session_state and mode == "Spoken Dialogue":
    st.text(st.session_state['display_text_dialogue'])

# User input at the bottom
with st.container():
    user_input = st.text_area("Enter your text here", value=st.session_state.user_input, help="Input non-English text for translation or English text for dialogue")
    submit_button = st.button("Submit")

if submit_button:
    if user_input:
        if mode == "Spoken Translation":
            result = translate_to_english(user_input)
            st.session_state['display_text_translation'] += f"User: {user_input}\n"
            st.session_state['display_text_translation'] += f"Translation: {result}\n"
        elif mode == "Spoken Dialogue":
            result = conversation_reply(user_input)
            st.session_state['display_text_dialogue'] += f"User: {user_input}\n"
            st.session_state['display_text_dialogue'] += f"Reply: {result}\n"
        
        st.session_state.user_input = ""
        # Rerun the app to clear the input box and update the display text
        st.rerun() 