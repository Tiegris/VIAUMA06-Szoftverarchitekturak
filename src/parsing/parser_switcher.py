from streamlit.runtime.uploaded_file_manager import UploadedFile

from parsing.parser_base import ParserBase
from parsing.csv_parser import CsvParser
from parsing.json_parser import JsonParser
from parsing.md_parser import MdParser
from parsing.excel_parser import ExcelParser
from parsing.db_parser import DbParser

import os


def _file_extension(file_name: str) -> str:
    return os.path.splitext(file_name)[1]

_octet_stream_switcher = {
    '.md': MdParser(),
    '.db': DbParser(),
    '.sqlite': DbParser(),
}
_switcher = {
    'application/json': JsonParser(),
    'text/csv': CsvParser(),
    'application/octet-stream': _octet_stream_switcher,
    'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet': ExcelParser(),
    'text/markdown': MdParser(),
}

def get_parser(file: UploadedFile) -> ParserBase:
    result =  _switcher.get(file.type)
    if type(result) == dict:
        return result.get(_file_extension(file.name))
    return result