from langchain_google_genai import ChatGoogleGenerativeAI # type: ignore

from dotenv import load_dotenv
load_dotenv()

import streamlit as st

#function to load model
def get_gemini_response(question):
    chatllm = ChatGoogleGenerativeAI(model="gemini-1.5-pro")
    response = chatllm.invoke(question)
    return response

# initialize the sremalit app
st.set_page_config(page_title='Q&A Demo')
st.header("LangChain QA application")

input = st.text_input("Input: ",key='input')
submit = st.button('Ask the question')


if submit:
    st.subheader("The response is ")
    response = get_gemini_response(input)
    # print(response.content)
    st.write(response.content)