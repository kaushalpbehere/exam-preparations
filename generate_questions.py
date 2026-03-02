import os

content_template = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>GCP Digital Leader - Set {set_num}</title>
    <link rel="stylesheet" href="../../assets/style.css">
</head>
<body data-exam-id="set{set_num}">
    <div class="container">
        <a href="../../index.html" class="btn">← Back to Dashboard</a>

        <h1>GCP Digital Leader (2026)</h1>
        <div style="background:#222; padding: 10px; margin-bottom: 20px; border: 1px solid #0f0; color: #0f0;">
            LAST-MINUTE CRAM (2026 Focus):
            GKE = Kubernetes, Cloud Run = Serverless Containers, Cloud Functions = Serverless Code,
            BigQuery = Data Warehouse, Cloud Spanner = Immutable Ledger, Vertex AI = GenAI/ML platform.
        </div>

        <h2>Set {set_num} (Questions {start_q}-{end_q})</h2>

{questions_html}
    </div>
    <script src="../../assets/exam-engine.js"></script>
</body>
</html>"""

question_template = """        <div class="q-block">
            <div class="q-line">Q{q_num}. Sample question about GCP service {q_num}? (A) Opt1 (B) Opt2 (C) Opt3 (D) Opt4</div>
            <div class="a-line">Answer: A - Explanation: Because Opt1 is the best fit for this scenario.</div>
        </div>"""

for i in range(1, 6):
    start_q = (i - 1) * 50 + 1
    end_q = i * 50
    questions_html = ""
    for j in range(start_q, end_q + 1):
        questions_html += question_template.format(q_num=j) + "\n"

    file_content = content_template.format(set_num=i, start_q=start_q, end_q=end_q, questions_html=questions_html)

    with open(f"exams/gcp-digital-leader/set{i}.html", "w") as f:
        f.write(file_content)

print("Generated 5 exam sets.")
