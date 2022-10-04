from typing import Callable
from streamlit.runtime.uploaded_file_manager import UploadedFile
from .csv_parser import parse as csv_parser
from .json_parser import parse as json_parser
from .md_parser import parse as md_parser
from .excel_parser import parse as excel_parser
from .db_parser import parse as db_parser
import os


def file_extension(file_name: str) -> str:
    return os.path.splitext(file_name)[1]  

def get_parser(file: UploadedFile) -> Callable[[UploadedFile, dict[str, str]], tuple[list[list[str], list[str]]]]:
    octet_stream_switcher = {
        '.md': md_parser,
        '.db': db_parser,
        '.sqlite': db_parser
    }
    switcher = {
        'application/json': json_parser,
        'text/csv': csv_parser,
        'application/octet-stream': octet_stream_switcher.get(file_extension(file.name)),
        'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet': excel_parser
    }
    return switcher.get(file.type)