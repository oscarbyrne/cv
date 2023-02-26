import shutil
import os

import yaml
import jinja2


def yaml_from_path(path):
    with open(path) as f:
        return yaml.safe_load(f)

def build_context(specification, records):
    context = yaml_from_path(specification)
    records = yaml_from_path(records)
    for page in context['pages']:
        for section in page:
            section['records'] = [
                records[name] for name in section["records"]
            ]
    return context

def render_html(template, context):
    return jinja2.Environment(
        loader=jinja2.FileSystemLoader("./"),
        trim_blocks=True,
        lstrip_blocks=True,
        line_statement_prefix="#"
    ).get_template(template).render(context)

def build(html, static_dir, deploy_dir):
    shutil.copytree(
        static_dir,
        os.path.join(deploy_dir, 'static'),
        dirs_exist_ok=True
    )
    output = os.path.join(deploy_dir, 'index.html')
    with open(output, "w") as f:
        f.write(html)

def main(specification, records, template, static_dir, deploy_dir):
    context = build_context(
        specification,
        records
    )
    html = render_html(
        template,
        context
    )
    build(
        html,
        static_dir,
        deploy_dir
    )


if __name__ == "__main__":
    main(
        './resume/specification.yaml',
        './resume/records.yaml',
        './resume/template.j2',
        './resume/static',
        './deploy'
    )
