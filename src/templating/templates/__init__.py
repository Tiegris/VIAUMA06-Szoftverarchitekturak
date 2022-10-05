from .default import Default
from .template_base import TemplateBase

# Extend this list with new templates
_templates = [
    Default()
]

templates: dict[str, TemplateBase] = {x.name: x for x in _templates}