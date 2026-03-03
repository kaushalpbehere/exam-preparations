import os

def create_gcp_pro_ml():
    dest_dir = r'exams\gcp\pro-ml'
    
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    # Generate Revision Guide
    revision_html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>GCP Pro ML Engineer - Revision Guide</title>
    <link rel="stylesheet" href="../../assets/style.css">
</head>
<body>
    <div class="container">
        <a href="../../index.html" class="btn">← Back to Dashboard</a>
        <h1>GCP Professional Machine Learning Engineer</h1>
        <h2>Revision Guide</h2>
        <div style="background:#222; padding: 10px; margin-bottom: 20px; border: 1px solid #34a853; color: #34a853;">
            LAST-MINUTE CRAM: Content to be generated. Focus on Vertex AI pipelines, BigQuery ML, TensorFlow/Keras on Google Cloud, MLOps, and scalable model deployment.
        </div>
    </div>
</body>
</html>"""

    with open(os.path.join(dest_dir, 'revision.html'), 'w', encoding='utf-8') as f:
        f.write(revision_html)

    # Generate 5 sets of 20 placeholder questions
    for set_idx in range(5):
        set_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>GCP Pro ML Engineer - Set {set_idx+1}</title>
    <link rel="stylesheet" href="../../assets/style.css">
</head>
<body data-exam-id="gcp-proml-set{set_idx+1}">
    <div class="container">
        <a href="../../index.html" class="btn">← Back to Dashboard</a>

        <h1>GCP Professional Machine Learning Engineer</h1>
        <h2>Set {set_idx+1} (Questions 1-20)</h2>
"""
        for i in range(20):
            set_html += f"""
        <div class="q-block">
            <div class="q-line">Q{i+1}. [GCP Pro ML Placeholder Question]</div>
            <div class="a-line">Answer: A - [Explanation to be generated]</div>
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
    <title>GCP Pro ML Engineer - Flashcards</title>
    <link rel="stylesheet" href="../../assets/style.css">
</head>
<body>
    <div class="container">
        <a href="../../index.html" class="btn">← Back to Dashboard</a>
        <h1>GCP Professional ML Engineer</h1>
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
            { f: '[GCP Pro ML Term Placeholder]', b: '[GCP Pro ML Definition Placeholder]' },
        ];
        
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

    print(f"Successfully generated placeholder files for exams\\gcp\\pro-ml")

if __name__ == '__main__':
    create_gcp_pro_ml()
