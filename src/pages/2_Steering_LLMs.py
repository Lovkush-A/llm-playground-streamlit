import streamlit as st
from utils import generate_goodfire_response
import asyncio
import nest_asyncio

# Enable nested event loops
nest_asyncio.apply()

st.set_page_config(
    page_title="Steering LLMs",
    page_icon="🎯"
)

st.title("Steering LLMs")

st.markdown("""
This page demonstrates the power of steering LLMs using SAE features.
This is done using [Goodfire's tools](https://docs.goodfire.ai/introduction).
You can provide steering instructions to guide the model's behavior and compare it with the unsteered response.

The steering instructions allow you to specify how you want the model to behave, for example:
- "Be more concise"
- "Be hilarious"
- "Star Wars"
- "Golden Gate Bridge"
""")

# User inputs
steering_instructions = st.text_area("Steering Instructions:", height=100)
user_input = st.text_area("Enter your text:", height=100)

# Button between text box and columns
generate_button = st.button("Generate Responses")

# Create two columns for side-by-side comparison
col1, col2 = st.columns(2)

# Headers and response display
with col1:
    st.subheader("Unsteered Response")
    if user_input and generate_button:
        try:
            with st.spinner("Generating responses..."):
                loop = asyncio.new_event_loop()
                asyncio.set_event_loop(loop)
                unsteered_response = generate_goodfire_response(user_input)
                st.write(unsteered_response)
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")

with col2:
    st.subheader("Steered Response")
    if user_input and generate_button:
        try:
            with st.spinner("Generating responses..."):
                loop = asyncio.new_event_loop()
                asyncio.set_event_loop(loop)
                steered_response = generate_goodfire_response(user_input, steering_instructions)
                st.write(steered_response)
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")

if generate_button and not user_input:
    st.warning("Please enter some text first!")