import os
import streamlit as st
from dotenv import load_dotenv, find_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.chains import LLMChain, SequentialChain
from langchain.document_loaders import Docx2txtLoader
from tiktoken import get_encoding

import warnings
warnings.filterwarnings('ignore')

tokenizer = get_encoding("cl100k_base")

llm = ChatOpenAI(temperature=0.0)
_ = load_dotenv(find_dotenv()) # read local .env file

uploaded_doc = st.file_uploader("Upload doc here in docx format", label_visibility="collapsed", type=["docx"])

if uploaded_doc is not None:
    def save_doc(uploaded_doc):
        with open(os.path.join("uploaded_docs", uploaded_doc.name), "wb") as f:
            f.write(uploaded_doc.getbuffer())

    save_doc(uploaded_doc)
    loader = Docx2txtLoader(os.getcwd() + "\\" + "uploaded_docs" + "\\" + uploaded_doc.name)
    data = loader.load()
# data

    choosen_language = st.text_input("What language do you want the document converted into: ")

    # prompt template 1: translate to Given Language
    first_prompt = ChatPromptTemplate.from_template(
        f"Translate the following data to {choosen_language}. Keep the format of the text same as original format. Change each name in the text to a name more appropriate to the {choosen_language}:"
        "\n\n{Data}"
        "\n\n TRANSLATED TEXT"
    )

# chain 1: input= Review and output= English_Review
    chain_one = LLMChain(llm=llm, prompt=first_prompt,
                        output_key="translated_data"
                        )

    overall_chain = SequentialChain(
        chains=[chain_one],
        input_variables=["Data"],
        output_variables=["translated_data"],
        verbose=False
    )

    data = loader.load()
# st.write(overall_chain(data))

    import aspose.words as aw

# create document object
    doc = aw.Document()

# create a document builder object
    builder = aw.DocumentBuilder(doc)
    result=str(overall_chain(data))
# add text to the document
    builder.write(result)

    # save document
    doc.save("out.docx")

    st.download_button(label= "Download Translated data", data=str(overall_chain(data)))
