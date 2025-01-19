import streamlit as st

st.set_page_config(
    page_title="LLM Playground",
    page_icon="🤖",
    layout="wide"
)

st.title("Welcome to Lovkush's LLM Playground! 🤖")

st.markdown("""
The LLM Playground is a collection of user-friendly tools for playing around with LLMs, to help you understand more how they work.

### Pre-trained model vs chatbot model
The outcome of pre-training is a model that tries to predict the next word, as if the text appeared somewhere on the internet.
This is not the same as having a helpful chatbot, which is why there are extra steps (like scaffolding, fine tuning or RLHF).
This page allows you to send text to both types of models and explicitly see the difference.

### Steering with SAEs
In the past year or so, Sparse Autoencoders (SAEs) have been a major tool in the field of Mechanistic Interpretability.
A highlight was Anthropic finding a 'Golden Gate Bridge' SAE feature and then [steering Claude to be obsessed with it](https://www.reddit.com/r/ClaudeAI/comments/1cz37d2/has_anyone_tried_golden_gate_claude_yet/).
This page allows you to play around with SAE feature steering, using Goodfire's API.
            
### Coming soon
- Playing with tokenizers.
""")

# # Add some space
# st.markdown("---")

# # Add some example or featured content
# st.subheader("Featured Content")
# st.write("Explore our different pages to experiment with various LLM capabilities!") 