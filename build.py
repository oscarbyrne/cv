import argparse
import copy

import yaml
import jinja2


parser = argparse.ArgumentParser(
    description="Generates HTML resumes"
)
parser.add_argument(
    "-c", "--config",
    help="yaml file containing layout + basic configuration",
    default="./resume/config.yaml"
)
parser.add_argument(
    "-r", "--records",
    help="yaml file containing records, used to populate resume",
    default="./resume/records.yaml"
)
parser.add_argument(
    "-s", "--style_sheet",
    help="css file",
    default="./resume/style.css"
)
parser.add_argument(
    "-t", "--template",
    help="template Jinja2 HTML file",
    default="./resume/template.j2"
)
parser.add_argument(
    "-o", "--output",
    help="output HTML file",
    default="./index.html"
)


def build_context(config, records, style_sheet):
    with open(config) as f: config = yaml.safe_load(f)
    with open(records) as f: records = yaml.safe_load(f)
    context = copy.copy(config)
    context["style_sheet"] = style_sheet
    for page in context["pages"]:
        for section in page:
            section["records"] = [
                records[name] for name in section["records"]
            ]
    return context

def main(config, records, style_sheet, template, output):
    context = build_context(config, records, style_sheet)
    html = jinja2.Environment(
        loader=jinja2.FileSystemLoader("./"),
        trim_blocks=True,
        lstrip_blocks=True,
        line_statement_prefix="#"
    ).get_template(template).render(context)
    with open(output, "w") as f:
        f.write(html)


if __name__ == "__main__":
    opts = parser.parse_args()
    main(
        **vars(opts)
    )

