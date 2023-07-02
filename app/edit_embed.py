"""Python file to serve as the frontend"""
import streamlit as st
import pinecone
import os
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Pinecone
from dotenv import load_dotenv
from sidebar import sidebar
import openai

load_dotenv()

pinecone.init(
    api_key=str(os.environ['PINECONE_API_KEY']),  
    environment=str(os.environ['PINECONE_ENV'])  
)
index_name = str(os.environ['PINECONE_INDEX_NAME'])

embeddings = OpenAIEmbeddings()

openai.api_key=os.environ['OPENAI_API_KEY']

def query_refiner(query):
    response = openai.Completion.create(
    
    model="text-davinci-003",
    prompt=f"You revise the input given to you for grammatical clarity. Edit the following in a concise, clear way. Deliver only three sentences at a time. Ask if more information is required. Do not mention the user and only edit for clarity. \n\n Query is: {query}", #CONVERSATION LOG: \n{conversation}\n\nQuery: {query}\n\nRefined Query:"
    temperature=0.1,
    max_tokens=1000,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )
    return response['choices'][0]['text']


def load_chain(query):
    docsearch=Pinecone.from_existing_index(index_name, embeddings)
    chain = load_chain()

    docs = chain.similarity_search(query, k=1)
    output = query_refiner(docs[0].page_content.replace('\n',''))

    return docs, output



