import os
import re

files = ["index.html", "dashboard.html", "digital-twin.html", "css-opt.html", "srp-opt.html", "analytics.html", "alerts.html"]
base_dir = r"c:\Users\shrey\oil-well-optimization\frontend"

links = [
    ("index.html", "Home"),
    ("dashboard.html", "Dashboard"),
    ("digital-twin.html", "Digital Twin"),
    ("css-opt.html", "CSS Optimization"),
    ("srp-opt.html", "SRP Optimization"),
    ("analytics.html", "Analytics"),
    ("alerts.html", "Alerts")
]

for file in files:
    filepath = os.path.join(base_dir, file)
    if not os.path.exists(filepath): continue
    
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    new_nav = '<ul class="nav-links">\n'
    for link, name in links:
        active_class = ' class="active"' if link == file else ''
        new_nav += f'            <li><a href="{link}"{active_class}>{name}</a></li>\n'
    new_nav += '        </ul>'
    
    content = re.sub(r'<ul class="nav-links">.*?</ul>', new_nav, content, flags=re.DOTALL)
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
