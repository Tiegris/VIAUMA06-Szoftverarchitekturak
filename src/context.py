from dataclasses import dataclass, field
from streamlit.runtime.uploaded_file_manager import UploadedFile
from parsers import get_parser

@dataclass
class TemplateContext:
    file: UploadedFile
    parser_args: dict[str, str]
    template_params: dict[str, str]
    template_name: str
    
    def __init__(self, file: UploadedFile, parser_args: list[str], template_params: list[str], template_name: str):
        self.file = file
        self.parser_args = parse_kvs(parser_args)
        self.template_params = parse_kvs(template_params)
        self.template_name = template_name
        
    @property
    def tdata(self):
        if self._tdata is None:
            self._tdata = get_parser(self.file)(self.file)
        return self.__tdata


def parse_kvs(kvs: list[str]) -> dict[str, str]:
    return { '='.split(kv)[0]:'='.split(kv)[1] for kv in kvs}
