import os

content_template = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AWS ML Path - Set {set_num}</title>
    <link rel="stylesheet" href="../../assets/style.css">
</head>
<body data-exam-id="aws-ml-set{set_num}">
    <div class="container">
        <a href="../../index.html" class="btn">← Back to Dashboard</a>

        <h1>AWS ML Specialty & Associate</h1>
        <div class="academic-theory">
            <strong>Academic Theory (MSc Level):</strong> Focus on AWS SageMaker distributed training, Bedrock GenAI integration, Retrieval-Augmented Generation (RAG) architectures, and vector embeddings using Amazon Titan.
        </div>

        <h2>Set {set_num} (Questions {start_q}-{end_q})</h2>

{questions_html}
    </div>
    <script src="../../assets/engine.js"></script>
</body>
</html>"""

question_template = """        <div class="q-block">
            <div class="q-line">Q{q_num}. Sample question about AWS ML service {q_num}? (A) Opt1 (B) Opt2 (C) Opt3 (D) Opt4</div>
            <div class="a-line">Answer: A - Explanation: Opt1 is correct because it matches the scenario. Opt2, Opt3, and Opt4 are incorrect because they serve different purposes.</div>
            <div class="score-controls">
                <button class="score-btn correct" data-correct="true" data-qindex="{q_num}">Correct</button>
                <button class="score-btn incorrect" data-correct="false" data-qindex="{q_num}">Incorrect</button>
            </div>
        </div>"""

os.makedirs("exams/aws-ml", exist_ok=True)

for i in range(1, 2):  # Only Set 1 for now
    start_q = (i - 1) * 50 + 1
    end_q = i * 50
    questions_html = ""
    for j in range(start_q, end_q + 1):
        questions_html += question_template.format(q_num=j) + "\n"

    file_content = content_template.format(set_num=i, start_q=start_q, end_q=end_q, questions_html=questions_html)

    with open(f"exams/aws-ml/set{i}.html", "w") as f:
        f.write(file_content)

print("Generated AWS ML exam sets.")
