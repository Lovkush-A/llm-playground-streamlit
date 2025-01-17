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
You can provide steering instructions and choose how much to steer the model.
If this is your first time, we recommend using default strengths of 0 (so no steering) and 0.5.
""")

# User inputs
steering_instructions = st.text_area("Steering Instructions:", height=100)
steering_strength_1 = st.slider("Steering Strength 1", min_value=-1., max_value=1.0, value=0., step=0.01)
steering_strength_2 = st.slider("Steering Strength 2", min_value=-1., max_value=1.0, value=0.5, step=0.01)
user_input = st.text_area("Enter your text:", height=100)

# Button between text box and columns
generate_button = st.button("Generate Responses")

# Create two columns for side-by-side comparison
col1, col2 = st.columns(2)

# Headers and response display
with col1:
    st.subheader("First steering strength")
    if user_input and generate_button:
        try:
            with st.spinner("Generating responses..."):
                loop = asyncio.new_event_loop()
                asyncio.set_event_loop(loop)
                unsteered_response = generate_goodfire_response(user_input, steering_instructions, steering_strength_1)
                st.write(unsteered_response)
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")

with col2:
    st.subheader("Second steering strength")
    if user_input and generate_button:
        try:
            with st.spinner("Generating responses..."):
                loop = asyncio.new_event_loop()
                asyncio.set_event_loop(loop)
                steered_response = generate_goodfire_response(user_input, steering_instructions, steering_strength_2)
                st.write(steered_response)
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")

if generate_button and not user_input:
    st.warning("Please enter some text first!")