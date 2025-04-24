# LLM Playground

This is a streamlit app that allows you to play around with LLMs.
You can find it [here](https://lovkushs-llm-playground.streamlit.app/).

## Pre-trained model vs chatbot model

The outcome of pre-training is a model that tries to predict the next word, as if the text appeared somewhere on the internet.
This is not the same as having a helpful chatbot, which is why there are extra steps (like scaffolding, fine tuning or RLHF).

## Steering with SAEs

In the past year or so, Sparse Autoencoders (SAEs) have been a major tool in the field of Mechanistic Interpretability.
A highlight was Anthropic finding a 'Golden Gate Bridge' SAE feature and then [steering Claude to be obsessed with it](https://www.reddit.com/r/ClaudeAI/comments/1cz37d2/has_anyone_tried_golden_gate_claude_yet/).
