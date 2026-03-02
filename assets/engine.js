document.addEventListener('DOMContentLoaded', () => {
    // Explanation toggling logic
    const qBlocks = document.querySelectorAll('.q-block');
    qBlocks.forEach(block => {
        block.addEventListener('click', function(e) {
            // Only toggle if not clicking on score controls
            if (!e.target.closest('.score-controls')) {
                const aLine = this.querySelector('.a-line');
                if (aLine) {
                    aLine.classList.toggle('hidden');
                }
            }
        });

        // Hide answers by default
        const aLine = block.querySelector('.a-line');
        if (aLine) {
            aLine.classList.add('hidden');
        }
    });

    // Score Tracking Logic
    const examId = document.body.getAttribute('data-exam-id');
    if (examId) {
        let progress = JSON.parse(localStorage.getItem('exam_progress') || '{}');
        if (!progress[examId]) {
            progress[examId] = { correct: 0, answered: 0, percent: 0 };
        }

        // Add Score Board UI if not present
        if (!document.getElementById('score-board')) {
            const scoreBoard = document.createElement('div');
            scoreBoard.id = 'score-board';
            scoreBoard.innerHTML = `
                <div>Score: <span id="correct-count">0</span> / <span id="answered-count">0</span></div>
                <div><span id="percent-count">0</span>%</div>
            `;
            document.body.prepend(scoreBoard);

            const contentWrapper = document.createElement('div');
            contentWrapper.className = 'content-wrapper';
            // Wrap everything except score board
            while (document.body.childNodes.length > 1) {
                const node = document.body.childNodes[1];
                if (node !== scoreBoard && node !== contentWrapper && node.tagName !== 'SCRIPT') {
                    contentWrapper.appendChild(node);
                } else {
                    break;
                }
            }
            document.body.insertBefore(contentWrapper, document.body.childNodes[1]);
        }

        // Add score controls to questions if not present
        qBlocks.forEach((block, index) => {
             if (!block.querySelector('.score-controls')) {
                 const controls = document.createElement('div');
                 controls.className = 'score-controls';
                 controls.innerHTML = `
                     <button class="score-btn correct" data-correct="true" data-qindex="${index}">Correct</button>
                     <button class="score-btn incorrect" data-correct="false" data-qindex="${index}">Incorrect</button>
                 `;
                 block.appendChild(controls);
             }
        });

        const updateScoreBoard = () => {
            document.getElementById('correct-count').textContent = progress[examId].correct;
            document.getElementById('answered-count').textContent = progress[examId].answered;
            const percent = progress[examId].answered === 0 ? 0 : Math.round((progress[examId].correct / progress[examId].answered) * 100);
            document.getElementById('percent-count').textContent = percent;
            progress[examId].percent = percent;
            localStorage.setItem('exam_progress', JSON.stringify(progress));
        };

        const scoreBtns = document.querySelectorAll('.score-btn');
        scoreBtns.forEach(btn => {
            btn.addEventListener('click', function(e) {
                e.stopPropagation(); // prevent block toggle
                const isCorrect = this.getAttribute('data-correct') === 'true';
                const qIndex = this.getAttribute('data-qindex');
                const controls = this.closest('.score-controls');

                // If this button is already active, do nothing or untoggle?
                if (this.classList.contains('active')) {
                     return;
                }

                // Remove active from sibling
                const siblings = controls.querySelectorAll('.score-btn');
                siblings.forEach(s => s.classList.remove('active'));

                this.classList.add('active');

                // Logic to update counts
                // If it was answered before, we adjust. If it wasn't, we add to answered
                const wasAnswered = this.closest('.q-block').getAttribute('data-answered') === 'true';
                const wasCorrectBefore = this.closest('.q-block').getAttribute('data-was-correct') === 'true';

                if (!wasAnswered) {
                    progress[examId].answered += 1;
                    if (isCorrect) {
                        progress[examId].correct += 1;
                    }
                    this.closest('.q-block').setAttribute('data-answered', 'true');
                    this.closest('.q-block').setAttribute('data-was-correct', isCorrect.toString());
                } else {
                    // Changing answer
                    if (isCorrect && !wasCorrectBefore) {
                         progress[examId].correct += 1;
                    } else if (!isCorrect && wasCorrectBefore) {
                         progress[examId].correct -= 1;
                    }
                    this.closest('.q-block').setAttribute('data-was-correct', isCorrect.toString());
                }

                updateScoreBoard();
            });
        });

        updateScoreBoard();
    }
});
