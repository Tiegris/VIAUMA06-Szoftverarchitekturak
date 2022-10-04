from streamlit.runtime.uploaded_file_manager import UploadedFile
import pandas as pd

def parse(file: UploadedFile, args: dict[str, str]) -> tuple[list[str], list[list[str]]]:
    delimiter = args.get('delimeter', ',')
    parsed = pd.read_csv(file, delimiter = delimiter)
    return [i for i in parsed.columns], [[j for j in i] for i in parsed.values]
