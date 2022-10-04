import os

def list_templates() -> list[str]:
    return os.listdir('src/templates')