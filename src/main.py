import click
import csv as _csv
from jinja2 import Environment, FileSystemLoader
import os

@click.group()
@click.pass_context
@click.option('template_args', '-t', '--template-arg', multiple=True, nargs=2, type=click.Tuple([str, str]))
@click.option('output_template_path', '--output-template-path', type=str)
@click.option('output_file_name', '-o', '--output-file', type=str)
def cli(ctx, template_args, output_template_path, output_file_name):
    ctx.ensure_object(dict)
    template_args_dict = {}
    for arg in template_args:
        template_args_dict[arg[0]] = arg[1]

    ctx.obj['template_args'] = template_args_dict
    ctx.obj['output_template_path'] = output_template_path
    ctx.obj['output_file_name'] = output_file_name


@cli.command('csv')
@click.pass_context
@click.argument('input_file')
def csv_command(ctx, input_file):
    with open(input_file) as csvfile:
        reader = _csv.reader(csvfile)
        list = [row for row in reader]
    ctx.obj['tdata'] = list
    export(ctx.obj)


def export(context):
    template_path = os.path.dirname(os.path.realpath(__file__))
    template_file_name = "default.tex"
    output_file_name = context['output_file_name']
    if output_file_name is None:
        extension = os.path.splitext(template_file_name)[1]
        output_file_name = f'output{extension}'

    env = Environment(loader=FileSystemLoader(template_path))
    template = env.get_template(template_file_name)
    rendered = template.render(tdata=context['tdata'], args=context['template_args'])

    with open(output_file_name, 'w') as writer:
        writer.write(rendered)


if __name__ == '__main__':
    cli()
