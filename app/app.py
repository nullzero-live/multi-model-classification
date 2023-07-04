import os
import pinecone
from data_process import gc_auth, process_data
import streamlit as st
import openai
from langchain.llms import OpenAI
from sidebar import sidebar
from edit_embed import load_chain, query_refiner





def main():
    
    sidebar()
    # App title
    st.title("Running multiple models in a Streamlit app")
    st.header("Logistic Regression & Random Forest Classifiers")
    # Query response
    uploaded_file = st.file_uploader("Upload a cleaned, preprocessed csv file")
    target=st.text_input("Target Column Name",)
    
    textarea = st.text("Response Text",)
    if st.button("Start"):
        pinecone.init(
        api_key=str(os.environ['PINECONE_API_KEY']),  
        environment=str(os.environ['PINECONE_ENV'])  
        )
        index_name = str(os.environ['PINECONE_INDEX_NAME'])
        openai.api_key=os.environ['OPENAI_API_KEY']
        
            # Start the spinner
        with st.spinner("Running functions..."):
            llm = OpenAI(model_name="text-davinci-003", temperature=0.2)                
            textarea.write("authenticating...")
            df=gc_auth()
            textarea.write("Authenticated successfully...")
            results = process_data(uploaded_file, target)
            
            textarea.write("Results are in...")
            for classifier, accuracy, aorc in zip(results["Classifier"], results["Accuracy"],results["AORC"]):
                st.header(f"{classifier:}")
                st.markdown(f"Accuracy: {accuracy:}")
                st.markdown(f"AORC: {aorc:}")
        
        st.title("Summary of Results:")
        
        
        with st.spinner("Generating Summary..."):
            query = f"Key areas and metric results are: {results}"
            res = load_chain(query)
            print(f"###LOAD CHAIN###\n\n:{res}")
            summaryarea=st.text("Summary Text",)
            print("retrieved your vectors...next is summarize")
            summaryarea.write("This is a summary of the results...")
            print("generating summary")
            print(f"{res}\n *** \n {results}")
            
            output = query_refiner(f"You are an expert machine learning analyst. You are academic and technical. Combine {results}\n\n and {res}\n\n. Write a detailed analysis in a 3 paragraphs long report in detail explaining the results. Include references to the material. Think step by Step. Explain the metrics in detail. Use a casual tone like Andrej Karpathy. Start with 'The Model shows. Convert all floats into percentages'")
            
            summaryarea.write(output)
            
    
    
                
