from abc import ABC, abstractmethod
from streamlit.runtime.uploaded_file_manager import UploadedFile

from .help import Help

class ParserBase(ABC):
    
    @abstractmethod
    def parse(self, file: UploadedFile, args: dict[str, str]) -> tuple[list[str], list[list[str]]]:
        pass
    
    @abstractmethod
    def help(self) -> list[Help]:
        pass