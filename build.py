import argparse
import shutil
import os

import yaml
import jinja2


CONFIG = './config.yaml'


def get_argument_parser():
    parser = argparse.ArgumentParser(
        description="Generates HTML resumes",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    defaults = yaml_from_path(CONFIG)
    parser.add_argument(
        "-sf", "--specification-file",
        help="YAML file specifying resume high-level properties and layout",
        default=defaults['specification_file']
    )
    parser.add_argument(
        "-r", "--records-file",
        help="YAML file containing records, used to populate resume",
        default=defaults['records_file']
    )
    parser.add_argument(
        "-t", "--template-file",
        help="J2 HTML template file for resume presentation logic",
        default=defaults['template_file']
    )
    parser.add_argument(
        "-sd", "--static-dir",
        help="Directory containing static resources (e.g. images and css)",
        default=defaults['static_dir']
    )
    parser.add_argument(
        "-d", "--deploy-dir",
        help="Build directory for deployment",
        default=defaults['deploy_dir']
    )
    return parser

def yaml_from_path(path):
    with open(path) as f:
        return yaml.safe_load(f)

def build_context(specification_file, records_file):
    context = yaml_from_path(specification_file)
    records = yaml_from_path(records_file)
    for page in context['pages']:
        for section in page:
            section['records'] = [
                records[name] for name in section["records"]
            ]
    return context

def render_html(template_file, context):
    return jinja2.Environment(
        loader=jinja2.FileSystemLoader("./"),
        trim_blocks=True,
        lstrip_blocks=True,
        line_statement_prefix="#"
    ).get_template(template_file).render(context)

def build(html, static_dir, deploy_dir):
    shutil.copytree(
        static_dir,
        os.path.join(deploy_dir, 'static'),
        dirs_exist_ok=True
    )
    output = os.path.join(deploy_dir, 'index.html')
    with open(output, "w") as f:
        f.write(html)

def main(specification_file, records_file, template_file, static_dir, deploy_dir):
    context = build_context(
        specification_file,
        records_file
    )
    html = render_html(
        template_file,
        context
    )
    build(
        html,
        static_dir,
        deploy_dir
    )


if __name__ == "__main__":
    opts = get_argument_parser().parse_args()
    main(
        **vars(opts)
    )
