from streamlit.runtime.uploaded_file_manager import UploadedFile
import pandas as pd

from .parser_base import ParserBase
from .help import Help

class ExcelParser(ParserBase):

    def parse(self, file: UploadedFile, args: dict[str, str]) -> tuple[list[str], list[list[str]]]:
        parsed = pd.read_excel(file)
        return [i if type(i) == str else str(i) for i in parsed.columns], [[j if type(j) == str else str(j) for j in i] for i in parsed.values]


    def help(self) -> list[Help]:
        return [
            
        ]