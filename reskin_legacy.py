import os
import re

legacy_dir = "to-be-deleted"
css_link = '<link rel="stylesheet" href="../assets/style.css">'
js_link = '<script src="../assets/engine.js"></script>'

for filename in os.listdir(legacy_dir):
    if filename.endswith(".html"):
        filepath = os.path.join(legacy_dir, filename)
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        # Update CSS links if they exist, or insert one
        content = re.sub(r'<style>.*?</style>', '', content, flags=re.DOTALL)
        content = re.sub(r'<link rel="stylesheet".*?>', '', content)

        # Insert new CSS link before </head>
        if '</head>' in content:
            content = content.replace('</head>', f'    {css_link}\n</head>')

        # Basic cleanup of old inline styles and JS to fit brute-force
        content = re.sub(r'style="[^"]*"', '', content)

        # Ensure script is included before </body>
        if '<script src="../assets/engine.js"></script>' not in content:
            if '</body>' in content:
                content = content.replace('</body>', f'    {js_link}\n</body>')

        # To match the brute force, wrap main content in <div class="container"> if not already
        if '<div class="container">' not in content:
            content = re.sub(r'<body.*?>', '<body>\n<div class="container">', content)
            content = content.replace('</body>', '</div>\n</body>')

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)

print("Legacy files reskinned.")
