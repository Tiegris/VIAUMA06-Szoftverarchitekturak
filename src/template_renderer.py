from jinja2 import Environment, FileSystemLoader
import os

from context import TemplateContext

def render(context: TemplateContext):
    # TODO: Prevent ../../ out of template folder
    # TODO: template dir from env var
    template_file_name = context.template_name
    
    template_path = os.path.dirname(os.path.realpath(__file__))
    env = Environment(loader=FileSystemLoader('src/templates'))
    template = env.get_template(template_file_name)
    rendered = template.render(tdata=context.tdata, args=context.args)
    return rendered

