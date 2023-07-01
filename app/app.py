import os
from data_process import gc_auth, process_data
import streamlit as st

def main():
    # App title
    st.title("Running multiple models in a Streamlit app")
    st.header("Logistic Regression")
    st.header("Random Forest")
    
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
                
