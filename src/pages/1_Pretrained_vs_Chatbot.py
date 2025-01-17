import streamlit as st
from utils import get_pretrained_response, get_chatbot_response

st.set_page_config(
    page_title="Pre-trained vs chatbot",
    page_icon="🤖"
)

st.title("Pre-trained model vs chatbot model")

st.markdown("""
The outcome of pre-training is a model that tries to predict the next word, as if the text appeared somewhere on the internet.
This is not the same as having a helpful chatbot, which is why there are extra steps (like scaffolding, fine tuning or RLHF).
This page allows you to send text to both types of models and explicitly see the difference.
            
WARNING: This uses a tool called [Replicate](https://replicate.com/), which can be slow for the first time you generate (two to three minutes). If it is taking long, just go do something else and come back. 
""")

# User input
user_input = st.text_area("Enter your text:", height=100)

# Button between text box and columns
generate_button = st.button("Generate Responses")

# Create two columns for side-by-side comparison
col1, col2 = st.columns(2)

# Headers and response display
with col1:
    st.subheader("Pretrained Model")
    if user_input and generate_button:
        try:
            with st.spinner("Generating responses..."):
                pretrained_response = get_pretrained_response(user_input)
                st.write(pretrained_response)
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")

with col2:
    st.subheader("Chatbot Model")
    if user_input and generate_button:
        try:
            with st.spinner("Generating responses..."):
                chatbot_response = get_chatbot_response(user_input)
                st.write(chatbot_response)
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")

if generate_button and not user_input:
    st.warning("Please enter some text first!") 