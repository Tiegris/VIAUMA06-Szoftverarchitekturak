from streamlit.runtime.uploaded_file_manager import UploadedFile
import pandas as pd

from .parser_base import ParserBase
from .help import Help

class ExcelParser(ParserBase):

    def parse(self, file: UploadedFile, args: dict[str, str]) -> tuple[list[str], list[list[str]]]:
        pass


    def help(self) -> list[Help]:
        pass