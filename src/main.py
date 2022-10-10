import streamlit as st
from exceptions import AppException, MalformedUploadedFileException, ParserArgumentException, TemplateParameterException

from parsing import get_parser
from context import TemplateContext
from templating import render
import templating.templates as templates

def main():
    file = st.file_uploader("File upload", type=["json", "csv", "xlsx", "md", "db", "sqlite"], accept_multiple_files=False)
    
    if file is None:
        st.error("No file were uploaded")
        parser = None
    else:
        parser = get_parser(file)
        
    selected_template = st.selectbox('Template selector', options=templates.templates.keys())
    
    parser_args_help = 'Key-value pairs for the parser engine. Put every entry in a new line. Upload file to get specific help.'
    parser_args_placeholder = '# Upload file to get specific help.\nkey_1=value_2\nkey_2=value_2' if parser is None else '\n'.join([x.serialize() for x in parser.help()])
    
    template_params_help = 'Key-value pairs for the template. Put every entry in a new line.'
    template_params_placeholder = 'key_1=value_2\nkey_2=value_2' if selected_template is None else templates.templates[selected_template].help
            
    parser_args = st.text_area('Parser arguments', help=parser_args_help, placeholder=parser_args_placeholder)
    template_params = st.text_area('Template parameters', help=template_params_help, placeholder=template_params_placeholder)
    
    context = TemplateContext(file, parser_args, template_params, selected_template)
    st.button('Render', on_click=click_handler, disabled=(file is None), kwargs={'context':context})

def click_handler(context):
    rendered = render(context)
    height = 24 * (1 + len(rendered.split('\n')))
    st.text_area('Rendered', value=rendered, height=height)


if __name__ == "__main__":
    try:
        main()
    except ParserArgumentException:
        st.error('Error in parser arguments!')
    except TemplateParameterException:
        st.error('Error in template parameters!')
    except MalformedUploadedFileException:
        st.error('Malformed input file!')
    except:
        st.error('Unhandled exception occurred!')
