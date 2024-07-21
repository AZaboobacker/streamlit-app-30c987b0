# import necessary libraries
import streamlit as st
import openai

# Title of the app
st.title('Personal Finance App')

# App description
st.write("Welcome to the Personal Finance App. Please enter your OpenAI API key to proceed.")

# Input for OpenAI API key
openai_api_key = st.text_input('Enter your OpenAI API Key')

if openai_api_key:
    # Setting OpenAI API key
    openai.api_key = openai_api_key

    # Authenticate with OpenAPI and use it for further processes
    # Fill in with the data or research code here

    st.success("Your OpenAI API key was accepted and is ready to use.")

    # Follow up actions or handling with OpenAI API using the key goes here

else:
    st.write("Please enter your OpenAI API key to proceed.")