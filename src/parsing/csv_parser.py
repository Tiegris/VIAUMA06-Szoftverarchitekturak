from streamlit.runtime.uploaded_file_manager import UploadedFile
import pandas as pd

from parsing.parser_base import ParserBase
from parsing.help import Help

class CsvParser(ParserBase):

    _arg_delimiter = 'delimiter', ','

    def parse(self, file: UploadedFile, args: dict[str, str]) -> tuple[list[str], list[list[str]]]:
        delimiter = args.get(*self._arg_delimiter)
        parsed = pd.read_csv(file, delimiter = delimiter)
        return [i for i in parsed.columns], [[j for j in i] for i in parsed.values]


    def help(self) -> list[Help]:
        return [
            Help(*self._arg_delimiter, 'Char to separate csv by.'),
        ]
