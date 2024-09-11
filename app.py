import streamlit as st
import os
from dotenv import load_dotenv

# Load the .env file from the root directory
load_dotenv(".env", override=True)

# Create two columns
col1, col2 = st.columns([3, 1])

with col1:
    # Setting the title and configuring the layout of the Streamlit page
    st.title("Financial Data Agent")


with col2:
    # Ensure the environment variable for the figure path is correctly set
    logo_file_path = "artifacts/arcurve_logo.png"
    print(logo_file_path)
    if logo_file_path and os.path.exists(logo_file_path):
        st.image(logo_file_path, width=200)
    else:
        st.error("Figure path is not set correctly or the file does not exist.")
# Introducing Descriptive Analytics
st.write("""The financial data agent leverages Retrieval Augmented Generation method to sythesize answer to the user query solely based on the in-house documents""")


import numpy as np
base_nodes = np.load('index/base_nodes.npy', allow_pickle=True).tolist()
objects = np.load('index/objects.npy', allow_pickle=True).tolist()
from llama_index.core import VectorStoreIndex

recursive_index = VectorStoreIndex(nodes=base_nodes + objects)

recursive_query_engine = recursive_index.as_query_engine(
    similarity_top_k=5
)

# Query the model

query = st.text_input('Enter your query here', 'What is the highest financial revenue in 2023?')
if st.button("Submit"):
    with st.spinner("Processing your query..."):
        response = recursive_query_engine.query(query)
        st.write(response.response)


