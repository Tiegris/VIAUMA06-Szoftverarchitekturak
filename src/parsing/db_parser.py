from streamlit.runtime.uploaded_file_manager import UploadedFile
import pandas as pd
from sqlite3 import connect
import uuid
import os

from .parser_base import ParserBase
from .help import Help

class DbParser(ParserBase):

    _arg_table = 'from', None
    _arg_columns = 'select', '*'
    _arg_query = 'query', None

    def parse(self, file: UploadedFile, args: dict[str, str]) -> tuple[list[str], list[list[str]]]:
        table = args.get(*self._arg_table)
        columns = args.get(*self._arg_columns)
        query = args.get(*self._arg_query)

        try:
            # TODO: do not write to disk, stream inside memory
            generated_name = f'{uuid.uuid4()}.db'
            data = file.read()
            with open(generated_name, 'wb') as f:
                f.write(data)
            conn = connect(generated_name)

            if query is None:
                if table is None:
                    table = pd.read_sql(
                        '''SELECT name FROM sqlite_master WHERE type='table';''',
                        conn
                    ).values[0][0]
                query = f'SELECT {columns} FROM {table};'

            # NOTE: This is SQL injection vulnerable, however it poses no threat, since the query is executed on a temporary copy of a user-uploaded database file.
            parsed = pd.read_sql(query, conn)
            return [i if type(i) == str else str(i) for i in parsed.columns], [[j if type(j) == str else str(j) for j in i] for i in parsed.values]
        finally:
            try:
                conn.close()
            finally:
                os.remove(generated_name)


    def help(self) -> list[Help]:
        return [
            Help(*self._arg_table, 'Name of the table. If not provided, the first table will be used.'),
            Help(*self._arg_columns, 'Selected columns.'),
            Help(*self._arg_query, 'Override query.'),
        ]
