import copy

import yaml
import jinja2


data = "resume.yml"
template = "resume.html.j2"
output = "index.html"


def build_context(config, records):
    context = copy.copy(config)
    for page in context["pages"]:
        for section in page:
            section["records"] = [
                records[name] for name in section["records"]
            ]
    return context

if __name__ == "__main__":
    
    with open(data) as f:
        # TODO: move to different files?
        config = yaml.load(f)
        records = config.pop("records")

    context = build_context(config, records)

    html = jinja2.Environment(
        loader=jinja2.FileSystemLoader("./"),
        trim_blocks=True,
        lstrip_blocks=True,
        line_statement_prefix="#"
    ).get_template(template).render(context)

    with open(output, "w") as f:
        f.write(html)