import os
from jinja2 import Environment, FileSystemLoader

from context import TemplateContext
from .templates import templates
import parsing

def render(context: TemplateContext):
    parser = parsing.get_parser(context.file)
    template = templates.get(context.template_name)
    if template is None:
        raise Exception()
    
    head, body = parser.parse(context.file, context.parser_args)
    head = [template.escaper.escape(x) for x in head]
    body = [[template.escaper.escape(j) for j in i] for i in body]
    
    template_folder = f'{os.path.dirname(os.path.realpath(__file__))}/templates'
    env = Environment(loader=FileSystemLoader(template_folder))
    env.trim_blocks = True
    env.lstrip_blocks = True
    template = env.get_template(template.template_path)
    rendered = template.render(
        thead=head,
        tdata=body,
        args=context.template_params,
    )
    return rendered.strip()

