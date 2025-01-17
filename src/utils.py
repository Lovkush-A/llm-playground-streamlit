import replicate
import goodfire
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def _generate_response(text, model_name, max_length):
    """Helper function to make API calls to Replicate API"""
    if text == "test":
        return f"test_{model_name}_{max_length}"

    # Get API token from environment variable
    REPLICATE_API_TOKEN = os.environ.get('REPLICATE_API_TOKEN')
    if not REPLICATE_API_TOKEN:
        raise Exception("REPLICATE_API_TOKEN environment variable not set")
        
    # Configure replicate client
    client = replicate.Client(api_token=REPLICATE_API_TOKEN)
    
    # Run inference using the specified model
    output = replicate.run(
        model_name,
        input={
            "prompt": text,
            "max_length": max_length
        }
    )
    
    if not output:
        raise Exception("Failed to get response from Replicate API")
        
    return ''.join(output)

def get_pretrained_response(text):
    """Get response from pretrained model"""
    return _generate_response(text, "meta/meta-llama-3-8b", max_length=50)

def get_chatbot_response(text):
    """Get response from chatbot model"""
    return _generate_response(text, "meta/meta-llama-3-8b-instruct", max_length=50) 


def generate_goodfire_response(text, steering_instructions=""):
    """Get response from goodfire model.
    
    Based on https://docs.goodfire.ai/quickstart
    """
    # get api key from environment variable
    GOODFIRE_API_KEY = os.environ.get('GOODFIRE_API_KEY')
    if not GOODFIRE_API_KEY:
        raise Exception("GOODFIRE_API_KEY environment variable not set")

    client = goodfire.Client(api_key=GOODFIRE_API_KEY)
    variant = goodfire.Variant("meta-llama/Meta-Llama-3.1-8B-Instruct")

    if steering_instructions:
        edits = client.features.AutoSteer(
            specification=steering_instructions,
            model=variant,
        )
        variant.set(edits)

    output = ""
    for token in client.chat.completions.create(
        [{"role": "user", "content": text}],
        model=variant,
        stream=True,
        max_completion_tokens=50,
    ):
        output += token.choices[0].delta.content

    return output
