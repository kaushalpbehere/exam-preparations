import os
import re

css_path = 'assets/style.css'
with open(css_path, 'r') as f:
    css_content = f.read()

errors = []

if 'font-family: monospace' not in css_content:
    errors.append("CSS missing 'font-family: monospace'")
if 'font-size: 13px' not in css_content:
    errors.append("CSS missing 'font-size: 13px'")
if 'min-height: 44px' not in css_content:
    errors.append("CSS missing 'min-height: 44px' (touch targets)")

def check_html_files(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.html'):
                filepath = os.path.join(root, file)
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()

                # Check for script tag
                if 'assets/engine.js' not in content and 'script>' not in content and 'index.html' not in filepath and 'flashcards.html' not in filepath and 'revision.html' not in filepath:
                    errors.append(f"{filepath} might be missing engine.js")

                # Check for styles link
                if 'assets/style.css' not in content and 'index.html' not in filepath and 'flashcards.html' not in filepath and 'revision.html' not in filepath:
                    errors.append(f"{filepath} might be missing style.css")

check_html_files('exams')
check_html_files('to-be-deleted')

if errors:
    print("Verification Failed:")
    for error in errors:
        print(f"- {error}")
    exit(1)
else:
    print("All automated checks passed successfully!")
