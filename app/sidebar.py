import streamlit as st
#from components import chat

#Set session state for sidebar
### REFACTOR TO INCLUDE ALL THREE??? ###
def set_openai_api_key(api_key_input: str):
    st.session_state["OPENAI_API_KEY"] = api_key_input

def set_openai_org(oai_org: str):    
    st.session_state["OPENAI_ORG"] = oai_org
    
def set_pinecone_api_key(pinecone_api_key: str):    
    st.session_state["PINECONE_API_KEY"] = pinecone_api_key
    
def set_pinecone_env(pinecone_env: str):    
    st.session_state["PINECONE_ENV"] = pinecone_env


def sidebar():
    with st.sidebar:
        st.markdown(
            "## How to use\n"
            "1. Enter your [OpenAI API key](https://platform.openai.com/account/api-keys) below🔑\n"  # noqa: E501
            "2. Upload a pdf, docx, or txt file📄\n"
            "3. Ask a question about the document💬\n"
            "4. Chat with GPT generally🤖\n"
        )
        api_key_input = st.text_input(
            "OpenAI API Key",
            type="password",
            placeholder="Paste your OpenAI API key here (sk-...)",
            help="You can get your API key from https://platform.openai.com/account/api-keys.",  # noqa: E501
            # session_state usage = remains only for session
            value=st.session_state.get("OPENAI_API_KEY", ""),
        )
        pinecone_key_input = st.text_input(
            "Pinecone API Key",
            type="password",
            placeholder="Paste your Pinecone API key here", # noqa: E501
            # session_state usage = remains only for session
            value=st.session_state.get("PINECONE_API_KEY", ""),
        )
        pinecone_env_input = st.text_input(
            "Pinecone Environment",
            type="password",
            placeholder="Paste your Pinecone Env key here", # noqa: E501
            # session_state usage = remains only for session
            value=st.session_state.get("PINECONE_ENV", ""),
        )
        
        ### IF REQUIRED FOR GPT-4 ###
        '''org_input = st.text_input(
            "OpenAI Organization ID",
            type="password",
            placeholder="Paste your OpenAI Organization ID here",
        
            # session_state usage = remains only for session
            value=st.session_state.get("OPENAI_ORG", ""),
        )'''
        
        

        if api_key_input:
            set_openai_api_key(api_key_input)
            set_pinecone_api_key(pinecone_key_input)
            set_pinecone_env(pinecone_env_input)
            #set_openai_org(org_input)
            
        
        st.markdown("---")
        
        clear_button = st.button("reset", key="clear_button")
    
        ### Placeholdr for choice ###
        
        
        # Map model names to OpenAI model IDs
        #if model_name == "GPT-3.5":
        model = "gpt-3.5-turbo"
        #else:
            #model = "gpt-4"

        # reset everything
        if clear_button:
            st.session_state['generated'] = []
            st.session_state['past'] = []
            st.session_state['messages'] = [
                {"role": "system", "content": "You are a helpful assistant."}
            ]
            st.session_state['number_tokens'] = []
            st.session_state['model_name'] = []
            st.session_state['cost'] = []
            st.session_state['total_cost'] = 0.0
            st.session_state['total_tokens'] = []
            #counter_placeholder.write(f"Total cost of this conversation: ${st.session_state['total_cost']:.5f}")



        
