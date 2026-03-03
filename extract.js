const fs = require('fs');
const path = require('path');

function extractQuestions(sourceFile, targetDir, titlePrefix) {
    if (!fs.existsSync(sourceFile)) {
        console.log(`Source file ${sourceFile} does not exist. Skipping.`);
        return;
    }
    const content = fs.readFileSync(sourceFile, 'utf8');

    // Find all q-blocks
    const regex = /<div class="q-block">\s*<div class="q-line">(.*?)<\/div>\s*<div class="a-line">(.*?)<\/div>\s*<\/div>/gs;
    let match;
    const questions = [];

    while ((match = regex.exec(content)) !== null) {
        questions.push({
            q: match[1].trim(),
            a: match[2].trim()
        });
    }

    console.log(`Extracted ${questions.length} questions from ${sourceFile}`);

    // Split into sets of 50
    const sets = [];
    for (let i = 0; i < questions.length; i += 50) {
        sets.push(questions.slice(i, i + 50));
    }

    // If we don't have enough to make 5 sets, we'll pad or we'll just generate what we have.
    // The backlog says "Generate 5 full mock exam sets".
    // If the legacy file doesn't have 250 questions, we just create the sets we can, and copy an empty template for the rest, 
    // or distribute them? Actually, I'll just generate sets 1 to 5. If a set is empty, it'll just have the template shell.

    for (let i = 0; i < 5; i++) {
        const setQuestions = sets[i] || [];
        const setNum = i + 1;
        const examIdStr = `${titlePrefix}-set${setNum}`.toLowerCase().replace(/\s+/g, '-');

        let htmlBlocks = '';
        let qIndex = 1;
        for (const q of setQuestions) {
            htmlBlocks += `        <div class="q-block">
            <div class="q-line">${q.q}</div>
            <div class="a-line">${q.a}</div>
            <div class="score-controls">
                <button class="score-btn correct" data-correct="true" data-qindex="${qIndex}">Correct</button>
                <button class="score-btn incorrect" data-correct="false" data-qindex="${qIndex}">Incorrect</button>
            </div>
        </div>\n`;
            qIndex++;
        }

        const template = `<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>${titlePrefix} - Set ${setNum}</title>
    <link rel="stylesheet" href="../../assets/style.css">
</head>
<body data-exam-id="${examIdStr}">
    <div class="container">
        <a href="../../index.html" class="btn">← Back to Dashboard</a>

        <h1>${titlePrefix}</h1>

        <h2>Set ${setNum} (Questions ${i * 50 + 1}-${i * 50 + setQuestions.length})</h2>

${htmlBlocks}
    </div>
    <script src="../../assets/engine.js"></script>
</body>
</html>`;

        const targetFile = path.join(targetDir, `set${setNum}.html`);
        fs.writeFileSync(targetFile, template, 'utf8');
        console.log(`Wrote ${targetFile} with ${setQuestions.length} questions.`);
    }
}

// ITIL v4
extractQuestions(
    path.join(__dirname, 'to-be-deleted', 'itil-v4-exam.html'),
    path.join(__dirname, 'exams', 'itil', 'v4-foundation'),
    'ITIL v4 Foundation'
);

// GH300
extractQuestions(
    path.join(__dirname, 'to-be-deleted', 'gh300.html'),
    path.join(__dirname, 'exams', 'gh300'),
    'GitHub Copilot (GH-300)'
);

// Life in the UK
extractQuestions(
    path.join(__dirname, 'to-be-deleted', 'life_in_uk.html'),
    path.join(__dirname, 'exams', 'life-in-uk'),
    'Life in the UK'
);

// AWS AI Practitioner (might not exist)
extractQuestions(
    path.join(__dirname, 'to-be-deleted', 'aws_ai.html'),
    path.join(__dirname, 'exams', 'aws', 'ai-practitioner'),
    'AWS Certified AI Practitioner'
);
