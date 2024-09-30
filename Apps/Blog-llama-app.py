import streamlit as st 
from langchain.prompts import PromptTemplate
from langchain_community.llms import CTransformers


#################### Fucniton to call the llama model
def getLLamaResponse(input_text, no_words, blog_style):
    llm = CTransformers(model='../models/llama-2-7b-chat.ggmlv3.q8_0.bin',
                        model_type='llama',
                        config={
                            'max_new_tokens':256,
                            'temperature': 0.01
                        })
    
    # prompt tamplate
    template = """
        Write a blog for {blog_style} for a topic {input_text} withing {no_words} words.
    """
    prompt = PromptTemplate(input_variables=['style', 'text', 'no_words'], template=template)
    
    #generate the response
    response = llm(prompt.format(blog_style=blog_style, input_text=input_text, no_words=no_words))
    print(response)
    return response


##################### Streealmit app
st.set_page_config(
    page_title='Generate Blogs',
    layout='centered',
    initial_sidebar_state='collapsed'
)

st.header("Generate Blogs")
input_text = st.text_input('Enter the Blog topic')

#creatign 2 more columns for additional input

col1, col2 = st.columns([5,5])

with col1:
    no_words = st.text_input('No of words')
with col2:
    blog_style = st.selectbox('Writing the blog for ', ('Researcher', 'Professionals', 'Students', 'Common People'), index=0)


submit = st.button('Generate')

## final response here
if submit:
    st.write(getLLamaResponse(input_text, no_words, blog_style))
