from dataclasses import dataclass, field

@dataclass
class TemplateContext:
    args: str
    tdata: list[list[str]]

