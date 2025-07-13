from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML
import os

def render_pdf(persona_data, output_path):
    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template('persona_template.html')
    
    html_out = template.render(**persona_data)
    HTML(string=html_out).write_pdf(output_path)
    print(f"✅ PDF saved at {output_path}")
