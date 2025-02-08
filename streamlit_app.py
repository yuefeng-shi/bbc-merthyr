import streamlit as st

from full_chain import retri_gen_QA, retri_gen_QA_final
from vector_store import create_vector_db
from local_loader import get_document_text
from splitter import split_documents


st.set_page_config(page_title="BBC Merthyr Project (Correspondence)")
st.title("🦜🔗 BBC Merthyr Project")

openai_api_key = st.sidebar.text_input("OpenAI API Key", type="password")

st.write('Please choose the Large Lange Model.')
llm_type = st.selectbox('Select', ['GPT-3.5-Turbo', 'GPT-4-Turbo'])


with st.form("my_form"):
    text = st.text_area(
        "Enter text:",
    )
    submitted = st.form_submit_button("Submit")
    if not openai_api_key.startswith("sk-"):
        st.warning("Please enter your OpenAI API key!", icon="⚠")
    if llm_type not in ['GPT-3.5-Turbo', 'GPT-4-Turbo']:
        st.warning("Please select the LLM, or it cannot work", icon="⚠")

    if submitted and openai_api_key.startswith("sk-"):
        type = ''    
        if llm_type == 'GPT-3.5-Turbo':
            type = 'gpt-3.5'
        else:
            type = 'gpt-4'
        
        if text == '':
            st.warning("Please input texts", icon="⚠")

        # data = get_document_text('filtered.json', './text_files')
        # data_chunks = split_documents(data)
        # dbvector = create_vector_db(data_chunks, openai_api_key)

    
        # res = retri_gen_QA(dbvector, openai_api_key, text, llm_type=type)

        res = retri_gen_QA_final(vectordb_dir='faiss_emb' , keys= openai_api_key, query = text, llm_type=type)

        st.write('Generated Answers:')
        st.info(res['answer'])
        st.write('References:')
        for i, item in enumerate(res['context']):
            # st.info('Text ID and Date for Reference ' + str(i) + ': \n' + item.metadata['source'][11:-4] + ';' + item.metadata['date'])
            st.info('Text ID and Date for Reference ' + str(i + 1) + ':')
            st.info( item.metadata['source'][11:-4] )
            st.info(item.metadata['date'])
