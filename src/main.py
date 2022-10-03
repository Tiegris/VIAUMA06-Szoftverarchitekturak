import streamlit as st
from parsers import parse

def main():
    file = st.file_uploader("File upload", type=["json", "csv", "xlsx", "md"], accept_multiple_files=False)

    if file is None:
        st.error("No file were uploaded")
    else:
        template_context = parse(file)
        
    pass 


if __name__ == "__main__":
    main()
