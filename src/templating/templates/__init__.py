from .default import Default
from .template_base import TemplateBase
from .simple_markdown import SimpleMarkdown

# Extend this list with new templates
_templates = [
    Default(),
    SimpleMarkdown(),
]

templates: dict[str, TemplateBase] = {x.name: x for x in _templates}
