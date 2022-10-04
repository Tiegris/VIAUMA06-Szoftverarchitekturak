from streamlit.runtime.uploaded_file_manager import UploadedFile
import pandas as pd
from sqlite3 import connect
import uuid
import os

def parse(file: UploadedFile, args: dict[str, str]) -> tuple[list[str], list[list[str]]]:
    try:
        generated_name = f'{uuid.uuid4()}.db'
        with open(generated_name, 'w') as f:
            f.write(file.read())
        
        conn = connect(generated_name)
        pd.read_sql('SELECT * from demo;', conn)
    finally: 
        conn.close()
        os.remove(generated_name)