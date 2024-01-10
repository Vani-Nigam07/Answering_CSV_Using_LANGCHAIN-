# -*- coding: utf-8 -*-
"""
Created on Sun Jan  7 01:49:18 2024
@author: HP
"""


from langchain_experimental.agents.agent_toolkits.csv.base import create_csv_agent
from langchain.llms import OpenAI
#from PIL import Image
from streamlit_chat import message

import os
import tempfile

# Set the OpenAI API key to an empty string (You should replace this with your actual API key)

import streamlit as st
import base64
def main():

    st.set_page_config(page_title="Knowwize Coding Assessment", page_icon="🦜")
    prin = st.secrets.keys()
    os.environ["OPENAI_API_KEY"] = st.secrets["general"]["KEY"]
    st.header("Knowwize Coding Assessment")
    st.write("This CSV includes Placement related statistics of an institute👋")

    with st.chat_message("user"): 
        st.write("Upload your CSV here" + " ".join(prin))
    file = st.file_uploader("", type="csv")  

    if file is not None:

        with tempfile.NamedTemporaryFile(mode='w+', suffix=".csv", delete=False) as f:  
            data_str = file.getvalue().decode('utf-8')
            f.write(data_str)
            f.flush()
            llm = OpenAI(temperature=0)
            with st.chat_message("human"):
                user_input = st.text_input(" What is your question?")
                ##messsage("What is your question?")
                if st.button("Click for the answer", type="primary"): 
                    agent = create_csv_agent(llm, f.name, verbose=True)
                    if user_input:
                        response = agent.run(user_input)
                        st.write(response)
                        print("Vani")


if __name__ == "__main__": 
    main()

