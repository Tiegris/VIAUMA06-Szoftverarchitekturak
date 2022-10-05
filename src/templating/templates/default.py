from templating.escapers.escaper import Escaper
from .template_base import TemplateBase

import templating.escapers as esc

class Default(TemplateBase):

    @property
    def name(self) -> str:
        return 'Default LateX'

    @property
    def template_path(self) -> str:
        return 'default.tex.j2'

    @property
    def help(self) -> str:
        return """
        tabular = <all centered>
        """.strip()

    _escaper = Escaper(esc.latex_escape_table)
    @property
    def escaper(self) -> esc.Escaper:
        return self._escaper