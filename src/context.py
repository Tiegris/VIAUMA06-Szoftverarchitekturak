from dataclasses import dataclass, field
from streamlit.runtime.uploaded_file_manager import UploadedFile
import streamlit as st

@dataclass
class TemplateContext:
    file: UploadedFile
    parser_args: dict[str, str]
    template_params: dict[str, str]
    template_name: str
    
    def __init__(self, file: UploadedFile, parser_args: str, template_params: str, template_name: str):
        self.file = file
        self.parser_args = parse_kvs(parser_args)
        self.template_params = parse_kvs(template_params)
        self.template_name = template_name


def parse_kvs(kvs: str) -> dict[str, str]:
    if kvs is None or kvs.strip() == '':
        return {}
    
    kvs = kvs.strip().split('\n')
    dict = {}
    for kv in kvs:
        splitted = kv.strip().split('=', 1)
        if len(splitted) != 2:
            st.error('Error in kv paris.')
            return {}
        dict[splitted[0].strip()] = splitted[1].strip()
    return dict
    
   
