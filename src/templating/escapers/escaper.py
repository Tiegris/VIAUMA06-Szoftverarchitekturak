class Escaper:    
    def __init__(self, escape_table: dict[str, str]):
        self._escape_table = escape_table
    
    def escape(self, word: str) -> str:
        for k, v in self._escape_table.items():
            word = word.replace(k, v)
        return word