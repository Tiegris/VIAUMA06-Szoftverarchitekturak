from abc import ABC, abstractmethod
from streamlit.runtime.uploaded_file_manager import UploadedFile

from .help import Help

class ParserBase:
    
    def parse(self, file: UploadedFile, args: dict[str, str]) -> tuple[list[str], list[list[str]]]:
        pass
    
    def help(self) -> list[Help]:
        pass