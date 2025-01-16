import streamlit as st
from utils import get_pretrained_response, get_chatbot_response

def main():
    st.title("LLM Playground")
    st.write("Compare responses from pretrained and chatbot models")

    # User input
    user_input = st.text_area("Enter your text:", height=100)

    if st.button("Generate Responses"):
        if user_input:
            try:
                with st.spinner("Generating responses..."):
                    # Create two columns for side-by-side comparison
                    col1, col2 = st.columns(2)
                    
                    with col1:
                        st.subheader("Pretrained Model")
                        pretrained_response = get_pretrained_response(user_input)
                        st.write(pretrained_response)
                    
                    with col2:
                        st.subheader("Chatbot Model")
                        chatbot_response = get_chatbot_response(user_input)
                        st.write(chatbot_response)
            
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")
        else:
            st.warning("Please enter some text first!")

if __name__ == "__main__":
    main() 