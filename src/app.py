import streamlit as st

st.set_page_config(
    page_title="LLM Playground",
    page_icon="🤖",
    layout="wide"
)

st.title("Welcome to Lovkush's LLM Playground! 🤖")

st.markdown("""
1. **Pre-trained model vs chatbot model**
The outcome of pre-training is a model that tries to predict the next word, as if the text appeared somewhere on the internet.
This is not the same as having a helpful chatbot, which is why there are extra steps (like scaffolding, fine tuning or RLHF).
This page allows you to send text to both types of models and explicitly see the difference.
2. **Page 1** - Coming soon!
3. **Page 2** - Coming soon!
""")

# # Add some space
# st.markdown("---")

# # Add some example or featured content
# st.subheader("Featured Content")
# st.write("Explore our different pages to experiment with various LLM capabilities!") 