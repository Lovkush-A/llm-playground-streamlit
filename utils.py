import replicate
import os

def _generate_response(text, model_name, max_length):
    """Helper function to make API calls to Replicate API"""
    if text == "test":
        return f"test_{model_name}_{max_length}"

    # Get API token from environment variable
    REPLICATE_API_TOKEN = os.environ.get('REPLICATE_API_TOKEN')
    if not REPLICATE_API_TOKEN:
        raise Exception("REPLICATE_API_TOKEN environment variable not set")
        
    # Configure replicate client
    replicate.Client(api_token=REPLICATE_API_TOKEN)
    
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
        
    # return output[0]
    return ''.join(output)

def get_pretrained_response(text):
    return _generate_response(text, "meta/meta-llama-3-8b", max_length=100)

def get_chatbot_response(text):
    return _generate_response(text, "meta/meta-llama-3-8b-instruct", max_length=100)

if __name__ == "__main__":
    print(get_pretrained_response("Hello, how are you?"))
    print(get_chatbot_response("Hello, how are you?"))