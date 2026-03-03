import os
import re
from bs4 import BeautifulSoup

def create_cloud_practitioner():
    source_file = r'to-be-deleted\aws_combined.html'
    dest_dir = r'exams\aws\cloud-practitioner'
    
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    with open(source_file, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'html.parser')

    # Extract revision concepts
    cram_sections = soup.find_all('div', class_='cram-section')
    revision_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AWS Cloud Practitioner - Revision Guide</title>
    <link rel="stylesheet" href="../../assets/style.css">
    <style>
        .concept-card {{
            background: #2a2a2a;
            border: 1px solid #444;
            border-radius: 8px;
            padding: 20px;
            margin-bottom: 15px;
        }}
        .concept-card h3 {{ margin-top: 0; color: #ff9900; }}
        pre {{ white-space: pre-wrap; }}
    </style>
</head>
<body>
    <div class="container">
        <a href="../../index.html" class="btn">← Back to Dashboard</a>
        <h1>AWS Certified Cloud Practitioner</h1>
        <h2>Revision Guide</h2>
        <div style="background:#222; padding: 10px; margin-bottom: 20px; border: 1px solid #ff9900; color: #ff9900;">
            LAST-MINUTE CRAM: Master the 6 Pillars of Well-Architected Framework, Storage Cheatsheet, and core AWS service value propositions (TCO, OpEx vs CapEx).
        </div>
"""
    for section in cram_sections:
        revision_html += f"        <div class='concept-card'>\n{section.decode_contents()}        </div>\n"
        
    revision_html += """    </div>
</body>
</html>"""

    with open(os.path.join(dest_dir, 'revision.html'), 'w', encoding='utf-8') as f:
        f.write(revision_html)

    # Extract all questions
    q_blocks = soup.find_all('div', class_='q-block')
    
    # Generate 5 sets of 20 questions (or whatever remainder)
    set_size = 20
    for set_idx in range(5):
        start_idx = set_idx * set_size
        end_idx = min(start_idx + set_size, len(q_blocks))
        if start_idx >= len(q_blocks):
            break
            
        subset = q_blocks[start_idx:end_idx]
        
        set_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AWS Cloud Practitioner - Set {set_idx+1}</title>
    <link rel="stylesheet" href="../../assets/style.css">
</head>
<body data-exam-id="aws-cp-set{set_idx+1}">
    <div class="container">
        <a href="../../index.html" class="btn">← Back to Dashboard</a>

        <h1>AWS Certified Cloud Practitioner</h1>
        <h2>Set {set_idx+1} (Questions {start_idx+1}-{end_idx})</h2>
"""
        for i, block in enumerate(subset):
            # Sometimes q-line has child elements, so wait for text
            q_line_elem = block.find('div', class_='q-line')
            a_line_elem = block.find('div', class_='a-line')
            if not q_line_elem or not a_line_elem:
                continue
            
            q_line = q_line_elem.text.strip()
            a_line = a_line_elem.text.strip()
            
            # Universal Template format
            set_html += f"""
        <div class="q-block">
            <div class="q-line">{q_line}</div>
            <div class="a-line">{a_line}</div>
            <div class="score-controls">
                <button class="score-btn correct" data-correct="true" data-qindex="{i+1}">Correct</button>
                <button class="score-btn incorrect" data-correct="false" data-qindex="{i+1}">Incorrect</button>
            </div>
        </div>"""

        set_html += """
    </div>
    <script src="../../assets/engine.js"></script>
</body>
</html>"""

        with open(os.path.join(dest_dir, f'set{set_idx+1}.html'), 'w', encoding='utf-8') as f:
            f.write(set_html)

    # Generate Flashcards
    flashcards_html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>AWS Cloud Practitioner - Flashcards</title>
    <link rel="stylesheet" href="../../assets/style.css">
</head>
<body>
    <div class="container">
        <a href="../../index.html" class="btn">← Back to Dashboard</a>
        <h1>AWS Cloud Practitioner</h1>
        <h2>Flashcards</h2>
        <div class="flashcard-container" id="fc-container">
            <div class="flashcard" id="card">
                <div class="card-inner" id="card-inner">
                    <div class="card-front" id="card-front">Loading...</div>
                    <div class="card-back" id="card-back">Loading...</div>
                </div>
            </div>
        </div>
        
        <div class="fc-controls">
            <button class="btn" id="prev-btn">← Prev</button>
            <span id="counter" style="color:#aaa; font-family:monospace; padding:0 15px;">1 / 1</span>
            <button class="btn" id="next-btn">Next →</button>
        </div>
    </div>

    <script>
        const cards = [
"""
    for block in q_blocks:
        q_line_elem = block.find('div', class_='q-line')
        a_line_elem = block.find('div', class_='a-line')
        if not q_line_elem or not a_line_elem:
            continue
            
        q_line = q_line_elem.text.strip()
        a_line = a_line_elem.text.strip()
        # Clean up question text slightly for flashcard front (remove "Q1. ", etc)
        q_text = re.sub(r'^Q\d+\.\s*', '', q_line).replace("'", "\\'").replace("\\", "\\\\").replace("\n", " ")
        a_text = a_line.replace("'", "\\'").replace("\\", "\\\\").replace("\n", " ")
        
        flashcards_html += f"            {{ f: '{q_text}', b: '{a_text}' }},\n"

    flashcards_html += """        ];
        
        let currentIndex = 0;
        const frontEl = document.getElementById('card-front');
        const backEl = document.getElementById('card-back');
        const innerEl = document.getElementById('card-inner');
        const counterEl = document.getElementById('counter');
        const prevBtn = document.getElementById('prev-btn');
        const nextBtn = document.getElementById('next-btn');

        function updateCard() {
            frontEl.textContent = cards[currentIndex].f;
            backEl.textContent = cards[currentIndex].b;
            counterEl.textContent = `${currentIndex + 1} / ${cards.length}`;
            innerEl.classList.remove('is-flipped');
        }

        document.getElementById('card').addEventListener('click', () => {
            innerEl.classList.toggle('is-flipped');
        });

        nextBtn.addEventListener('click', () => {
            if (currentIndex < cards.length - 1) {
                currentIndex++;
                updateCard();
            }
        });

        prevBtn.addEventListener('click', () => {
            if (currentIndex > 0) {
                currentIndex--;
                updateCard();
            }
        });

        // Initialize
        updateCard();
    </script>
</body>
</html>"""

    with open(os.path.join(dest_dir, 'flashcards.html'), 'w', encoding='utf-8') as f:
        f.write(flashcards_html)

    print(f"Successfully generated {len(q_blocks)} questions across 5 sets + revision guide + flashcards in {dest_dir}")

if __name__ == '__main__':
    create_cloud_practitioner()
