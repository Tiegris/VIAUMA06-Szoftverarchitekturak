import streamlit as st
from parsers import get_parser
from context import TemplateContext
from template_renderer import render
from utils import list_templates

def main():
    file = st.file_uploader("File upload", type=["json", "csv", "xlsx", "md", "db", "sqlite"], accept_multiple_files=False)
    
    if file is None:
        st.error("No file were uploaded")
            
    parser_args = st.text_area('Parser arguments', help='Key-value pairs for the parser engine. Put every entry in a new line.', placeholder='key_1=value_2\nkey_2=value_2')
    template_params = st.text_area('Template parameters', help='Key-value pairs for the template. Put every entry in a new line.', placeholder='key_1=value_2\nkey_2=value_2')
    selected_template = st.selectbox('Template selector', options=list_templates())
    
    context = TemplateContext(file, parser_args, template_params, selected_template)
    st.button('Render', on_click=click_handler, disabled=(file is None), kwargs={'context':context})

def click_handler(context):
    render(context)
    st.text_area('Rendered')


if __name__ == "__main__":
    main()
