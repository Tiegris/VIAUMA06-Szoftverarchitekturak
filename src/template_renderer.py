from jinja2 import Environment, FileSystemLoader
import os
from context import TemplateContext

def render(context: TemplateContext, template_file_name: str):
    if template_file_name is None:
        template_file_name = "default.tex"

    template_path = os.path.dirname(os.path.realpath(__file__))
    env = Environment(loader=FileSystemLoader(template_path))
    template = env.get_template(template_file_name)
    rendered = template.render(tdata=context.tdata, args=context.args)
    return rendered

