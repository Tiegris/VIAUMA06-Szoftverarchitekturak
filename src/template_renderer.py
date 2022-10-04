from jinja2 import Environment, FileSystemLoader
import os

from context import TemplateContext

def render(context: TemplateContext):
    # TODO: Prevent ../../ out of template folder
    # TODO: template dir from env var
    template_file_name = context.template_name
    
    template_folder = 'src/templates'
    env = Environment(loader=FileSystemLoader(template_folder))
    env.trim_blocks = True
    env.lstrip_blocks = True
    template = env.get_template(template_file_name)
    rendered = template.render(
        thead=context.thead,
        tdata=context.tdata,
        args=context.template_params,
    )
    return rendered.strip()

