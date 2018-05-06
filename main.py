import yaml
import jinja2


data = "resume.yml"
template = "template.html.j2"
output = "index.html"

if __name__ == '__main__':
    
    with open(data) as f:
        context = yaml.load(f)

    html = jinja2.Environment(
        loader=jinja2.FileSystemLoader('./'),
        trim_blocks=True,
        lstrip_blocks=True
    ).get_template(template).render(context)

    with open(output, 'w') as f:
        f.write(html)