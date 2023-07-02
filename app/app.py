import os
from data_process import gc_auth, process_data
import streamlit as st
import openai
from langchain.llms import OpenAI
from sidebar import sidebar

def main():
    sidebar()
    # App title
    st.title("Running multiple models in a Streamlit app")
    st.header("Logistic Regression & Random Forest Classifiers")
    # Query response
    textarea = st.text("Response Text",)
    if st.button("Start") and api_key:
            # Start the spinner
            with st.spinner("Running functions..."):
                openai.api_key = api_key
                llm = OpenAI(model_name="text-davinci-003", openai_api_key=api_key)
                textarea.write("authenticating...")
                df=gc_auth()
                textarea.write("Authenticated successfully...")
                results = process_data(df)
                
                textarea.write("Results are in...")
                for classifier, accuracy, aorc in zip(results["Classifier"], results["Accuracy"],results["AORC"]):
                    st.header(f"{classifier:}")
                    st.markdown(f"Accuracy: {accuracy:}")
                    st.markdown(f"AORC: {aorc:}")
    
                st.title("Summary of Results Incoming... Please Wait.")
                summaryarea=st.text("Summary Text",)
                summaryarea.write("This is a summary of the results...")
                summaryarea.write(llm(f"summarize: {results} as percentages and explain the meaning of the results as a separate paragraph. Be concise. In a new paragraph explain Accuracy and AORC in detail"))
                
    
    
                
