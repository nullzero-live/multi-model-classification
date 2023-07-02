import os
from data_process import gc_auth, process_data
import streamlit as st
import openai
from langchain.llms import OpenAI




def main():
    # App title
    st.title("Running multiple models in a Streamlit app")
    st.header("Logistic Regression & Random Forest Classifiers")
    
    api_key = st.text_input("Enter your OpenAPI Key Here...")
    if api_key:
        openai.api_key = api_key
    else:
        print("Error with API key")
    
    llm = OpenAI(model_name="text-davinci-003", openai_api_key=api_key)
    
    # Query response
    textarea = st.text("Response Text",)
    if st.button("Start"):
            # Start the spinner
            with st.spinner("Running functions..."):
                textarea.write("authenticating...")
                df=gc_auth()
                textarea.write("Authenticated successfully...")
                results = process_data(df)
                
                textarea.write("Results are in...")
                for classifier, accuracy, aorc in zip(results["Classifier"], results["Accuracy"],results["AORC"]):
                    st.header(f"{classifier:}")
                    st.markdown(f"Accuracy: {accuracy:}")
                    st.markdown(f"AORC: {aorc:}")
    summaryarea=st.text("Summary Text",)
    summaryarea.write("This is a summary of the results...")
    summaryarea.write(llm(f"summarize: {results}"))
    
    
    
                
