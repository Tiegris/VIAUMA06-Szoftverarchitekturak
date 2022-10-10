from streamlit.runtime.uploaded_file_manager import UploadedFile

from exceptions import MalformedUploadedFileError, ParserEngineError

from .parser_base import ParserBase
from .help import Help

class MdParser(ParserBase):

    _arg_starting_line_index = 'line', '1'
    _arg_encoding = 'encoding', 'UTF-8'

    def parse(self, file: UploadedFile, args: dict[str, str]) -> tuple[list[str], list[list[str]]]:
        try:
            starting_line_index = int(args.get(*self._arg_starting_line_index)) - 1
            encoding = args.get(*self._arg_encoding)
        except ValueError:
            raise ParserEngineError('Value of argument: "line", is not an integer.')

        lines = file.readlines()
        # Length + 3, because a md table is at least 3 lines long.
        if starting_line_index > len(lines) + 3:
            raise ParserEngineError('File has less lines than provided starting line.')
    
        header = _parse_line(lines[starting_line_index], encoding)
        expected_len = len(header)
        aligners = _parse_line(lines[starting_line_index + 1], encoding)
        
        if len(aligners) != expected_len:
            raise MalformedUploadedFileError('Malformed table.')

        result = []
        for i in range(starting_line_index + 2, len(lines)):
            line = _parse_line(lines[i], encoding)
            if len(line) != expected_len:
                raise MalformedUploadedFileError('Malformed table.')
            result.append(line)
            
        return header, result


    def help(self) -> list[Help]:
        return [
            Help(*self._arg_starting_line_index, 'First line if the table inside the MD file. Indexed from 1.'),
            Help(*self._arg_encoding, 'File encoding.'),
        ]


def _split_line(line: str) -> list[str]:
    splitted = line.split('|')[1:-1]
    col_count = 0
    prev = ''
    for c in line:
        if prev == '\\':
            continue
        if c == '|':
            col_count += 1
    col_count -= 1
    result = ['' for i in range(col_count)]
    
    consumed_index = 0
    for i in range(col_count):
        while True:
            if consumed_index >= len(splitted):
                raise MalformedUploadedFileError('Malformed table.')
            consumed = splitted[consumed_index]
            consumed_index += 1
            result[i] = consumed        
            if consumed == '' or consumed[-1] != '//':
                break
            else:
                result[i] = result[i][0:-1]

    return result
    

def _parse_line(line: bytes, encoding: str) -> list[str] :
    decoded_line = line.strip().decode(encoding)
    if len(decoded_line) == 0 or decoded_line[0] != '|' or decoded_line[-1] != '|':
        raise MalformedUploadedFileError('Malformed table.')
    return [x.strip() for x in _split_line(decoded_line)]

