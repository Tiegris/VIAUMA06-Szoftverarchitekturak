from streamlit.runtime.uploaded_file_manager import UploadedFile
from context import TemplateContext
from csv_parser import parse as csv_parser

def parse(file: UploadedFile) -> list[list[str]]:
    switcher = {
        "application/json": json_parser(file),
        "text/csv": csv_parser(file),
    }
    return switcher.get(file.type)