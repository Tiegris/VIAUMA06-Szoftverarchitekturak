from dataclasses import dataclass, field

@dataclass
class Help:
    argument: str
    default: str
    description: str
    
    def __init__(self, argument, default, description):
        self.argument = argument
        self.default = default if default is not None else 'None'
        self.description = description
    
    def serialize(self):
        return f'{self.argument:<12} {"=":^1}  {self.default:<12} {"#":>20} {self.description}'

    
    
