document.addEventListener('DOMContentLoaded', () => {
    const questions = document.querySelectorAll('.q-block');
    const examId = document.body.dataset.examId;

    if (!examId) return; // Not an exam page

    let totalQs = questions.length;
    let answered = 0;
    let correct = 0;

    // Load saved progress
    const savedProgress = JSON.parse(localStorage.getItem(`exam_${examId}`) || '{}');

    // Create scoreboard
    const scoreBoard = document.createElement('div');
    scoreBoard.id = 'score-board';
    scoreBoard.innerHTML = `
        <div>Score: <span id="score-correct">0</span> / <span id="score-total">0</span> (<span id="score-percent">0</span>%)</div>
        <div id="pass-fail">--</div>
    `;

    const wrapper = document.createElement('div');
    wrapper.className = 'content-wrapper';

    // Wrap existing content
    while(document.body.firstChild) {
        wrapper.appendChild(document.body.firstChild);
    }

    document.body.appendChild(scoreBoard);
    document.body.appendChild(wrapper);

    const scoreCorrectEl = document.getElementById('score-correct');
    const scoreTotalEl = document.getElementById('score-total');
    const scorePercentEl = document.getElementById('score-percent');
    const passFailEl = document.getElementById('pass-fail');

    function updateScoreDisplay() {
        scoreCorrectEl.textContent = correct;
        scoreTotalEl.textContent = answered;

        let percent = answered === 0 ? 0 : Math.round((correct / answered) * 100);
        scorePercentEl.textContent = percent;

        if (answered > 0) {
            if (percent >= 70) {
                passFailEl.textContent = 'PASS';
                passFailEl.style.color = '#0f0';
            } else {
                passFailEl.textContent = 'FAIL';
                passFailEl.style.color = '#f00';
            }
        }

        // Save overall progress for dashboard
        let overallProgress = JSON.parse(localStorage.getItem('exam_progress') || '{}');
        overallProgress[examId] = {
            correct: correct,
            answered: answered,
            total: totalQs,
            percent: percent
        };
        localStorage.setItem('exam_progress', JSON.stringify(overallProgress));
    }

    questions.forEach((q, index) => {
        const qId = `q_${index}`;
        const aLine = q.querySelector('.a-line');
        aLine.classList.add('hidden');

        const controls = document.createElement('div');
        controls.className = 'score-controls hidden';
        controls.innerHTML = `
            <button class="score-btn correct" data-val="1">Correct</button>
            <button class="score-btn incorrect" data-val="0">Incorrect</button>
        `;
        q.appendChild(controls);

        // Toggle answer visibility
        q.querySelector('.q-line').addEventListener('click', (e) => {
            aLine.classList.toggle('hidden');
            controls.classList.toggle('hidden');
        });

        // Restore state if saved
        if (savedProgress[qId] !== undefined) {
            answered++;
            if (savedProgress[qId] === 1) {
                correct++;
                controls.querySelector('.correct').classList.add('active');
            } else {
                controls.querySelector('.incorrect').classList.add('active');
            }
        }

        // Handle scoring buttons
        controls.querySelectorAll('.score-btn').forEach(btn => {
            btn.addEventListener('click', (e) => {
                e.stopPropagation(); // Don't toggle answer

                const val = parseInt(btn.dataset.val);
                const prevVal = savedProgress[qId];

                // Remove active class from both
                controls.querySelectorAll('.score-btn').forEach(b => b.classList.remove('active'));

                if (prevVal === undefined) {
                    answered++;
                    if (val === 1) correct++;
                } else if (prevVal !== val) {
                    // Changed answer
                    if (val === 1) correct++;
                    else correct--;
                } else if (prevVal === val) {
                    // Toggled off
                    answered--;
                    if (val === 1) correct--;
                    delete savedProgress[qId];
                    localStorage.setItem(`exam_${examId}`, JSON.stringify(savedProgress));
                    updateScoreDisplay();
                    return;
                }

                btn.classList.add('active');
                savedProgress[qId] = val;
                localStorage.setItem(`exam_${examId}`, JSON.stringify(savedProgress));
                updateScoreDisplay();
            });
        });
    });

    updateScoreDisplay();
});