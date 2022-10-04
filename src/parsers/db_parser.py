from streamlit.runtime.uploaded_file_manager import UploadedFile
import pandas as pd
from sqlite3 import connect
import uuid
import os

def parse(file: UploadedFile, args: dict[str, str]) -> tuple[list[str], list[list[str]]]:
    table = args.get('from')
    columns = args.get('select', '*')
    query = args.get('query')

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
        return [i for i in parsed.columns], [[j for j in i] for i in parsed.values]
    finally:
        try:
            conn.close()
        finally:
            os.remove(generated_name)