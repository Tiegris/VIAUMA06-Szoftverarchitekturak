from typing import Callable

from templating.escapers.escaper import Escaper
from .template_base import TemplateBase

import templating.escapers as esc

class SimpleMarkdown(TemplateBase):

    @property
    def name(self) -> str:
        return 'Simple Markdown'

    @property
    def template_path(self) -> str:
        return 'simple_markdown.md.j2'

    @property
    def help(self) -> str:
        return """
        aligner = |-|-|...|-|
        """.strip()

    _escaper = Escaper(esc.md_escape_table)
    @property
    def escaper(self) -> esc.Escaper:
        return self._escaper