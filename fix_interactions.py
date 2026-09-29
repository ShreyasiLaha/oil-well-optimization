import os

files = {
    'frontend/index.html': [
        ('href="/dashboard.html"', 'href="dashboard.html"'),
        ('href="#explore"', 'href="digital-twin.html"')
    ],
    'frontend/dashboard.html': [
        ('href="#" class="btn btn-primary ai-btn"', 'href="srp-opt.html" class="btn btn-primary ai-btn"')
    ],
    'frontend/alerts.html': [
        ('<button class="btn btn-secondary alert-btn">View Details</button>', '<button class="btn btn-secondary alert-btn" onclick="alert(\'Opening simulated alert details...\')">View Details</button>')
    ]
}

for filepath, replacements in files.items():
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        for old_str, new_str in replacements:
            content = content.replace(old_str, new_str)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {filepath}")
