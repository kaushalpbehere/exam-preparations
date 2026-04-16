const fs = require('fs');
const path = require('path');

const targetDir = path.join(__dirname, 'exams', 'itil', 'v5-foundation');
const targetFile = path.join(targetDir, 'flashcards.html');

const template = `<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ITIL v5 Foundation - Flashcards</title>
    <style>
        :root {
            --bg-color: #0d1117;
            --container-bg: #161b22;
            --text-main: #c9d1d9;
            --accent: #58a6ff;
            --border-muted: #30363d;
        }

        body {
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
            background-color: var(--bg-color);
            color: var(--text-main);
            margin: 0;
            padding: 20px;
            display: flex;
            flex-direction: column;
            align-items: center;
            min-height: 100vh;
        }

        .header {
            width: 100%;
            max-width: 600px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 20px;
        }

        .back-btn {
            color: var(--accent);
            text-decoration: none;
            font-weight: 600;
        }

        .flashcard-container {
            width: 100%;
            max-width: 600px;
            height: 400px;
            perspective: 1000px; /* 3D effect */
            margin-bottom: 30px;
        }

        .flashcard {
            width: 100%;
            height: 100%;
            background-color: var(--container-bg);
            border: 1px solid var(--border-muted);
            border-radius: 12px;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 30px;
            box-sizing: border-box;
            text-align: center;
            font-size: 1.5rem;
            line-height: 1.4;
            cursor: pointer;
            transition: transform 0.6s cubic-bezier(0.4, 0, 0.2, 1);
            transform-style: preserve-3d;
            box-shadow: 0 8px 24px rgba(0,0,0,0.2);
        }

        /* Flip Action */
        .flashcard.flipped {
            transform: rotateX(180deg);
        }

        .card-face {
            position: absolute;
            width: 100%;
            height: 100%;
            backface-visibility: hidden;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            padding: 24px;
            box-sizing: border-box;
        }

        .card-front {
            /* Front is default */
        }

        .card-back {
            transform: rotateX(180deg);
            color: #7ee787; /* Greenish tint for the answer */
            font-size: 1.2rem;
            overflow-y: auto; /* In case explanation is long */
        }
        
        .card-label {
            position: absolute;
            top: 20px;
            font-size: 0.8rem;
            color: #8b949e;
            text-transform: uppercase;
            letter-spacing: 1px;
        }

        .controls {
            display: flex;
            gap: 20px;
            align-items: center;
        }

        .nav-btn {
            background-color: var(--border-muted);
            color: var(--text-main);
            border: none;
            padding: 12px 24px;
            border-radius: 6px;
            font-size: 1rem;
            cursor: pointer;
            transition: background-color 0.2s;
        }

        .nav-btn:hover {
            background-color: #484f58;
        }

        .nav-btn:disabled {
            opacity: 0.5;
            cursor: not-allowed;
        }

        .progress {
            font-size: 1rem;
            color: #8b949e;
            min-width: 80px;
            text-align: center;
        }
        
        .instructions {
            margin-top: 40px;
            color: #8b949e;
            font-size: 0.9rem;
            text-align: center;
        }

    </style>
</head>
<body>

    <div class="header">
        <a href="../../index.html" class="back-btn">← Dashboard</a>
        <h2>ITIL v5 Flashcards</h2>
        <div style="width: 80px;"></div> <!-- Spacer -->
    </div>

    <div class="flashcard-container" onclick="flipCard()">
        <div class="flashcard" id="card">
            <div class="card-face card-front">
                <span class="card-label">Question</span>
                <div id="question-text">Loading...</div>
            </div>
            <div class="card-face card-back">
                <span class="card-label">Answer</span>
                <div id="answer-text">Loading...</div>
            </div>
        </div>
    </div>

    <div class="controls">
        <button class="nav-btn" id="prev-btn" onclick="prevCard()">&lt; Prev</button>
        <div class="progress" id="progress-text">1 / 50</div>
        <button class="nav-btn" id="next-btn" onclick="nextCard()">Next &gt;</button>
    </div>
    
    <div class="instructions">
        Tap the card to flip. Use Prev/Next buttons or Left/Right arrow keys to navigate.
    </div>

    <script>
        const cards = [
            { q: "What is a 'Complex System'?", a: "A non-linear, unpredictable environment where the whole is greater than the sum of its parts. Change should be managed via small, safe-to-fail experiments." },
            { q: "What is the primary goal of AIOps in ITIL v5?", a: "To use Machine Learning to reduce alert noise, correlate events, and automatically identify root causes to speed up Incident Management." },
            { q: "Define 'Shift-Left'.", a: "Moving tasks (like security testing or Level 1 support) earlier in the lifecycle/pipeline or closer to the user to increase speed and reduce costs." },
            { q: "What is 'Toil' (SRE context)?", a: "Manual, repetitive, automatable, tactical work devoid of enduring value that scales linearly as a service grows. It must be eliminated." },
            { q: "RTO vs RPO?", a: "RTO (Recovery Time Objective): Max acceptable downtime. RPO (Recovery Point Objective): Max acceptable data loss (measured in time)." },
            { q: "SlAs vs XLAs?", a: "SLAs measure technical outputs (99% uptime). XLAs (Experience Level Agreements) measure human outcomes and user satisfaction." },
            { q: "What does 'Value Co-creation' mean?", a: "Value isn't delivered BY the provider TO the consumer. It is jointly created when the consumer actively uses the service to achieve an outcome." },
            { q: "What is a 'Service Offering'?", a: "A package combining Goods (laptop), Access to Resources (VPN), and Service Actions (Helpdesk support) designed for a target consumer group." },
            { q: "What is 'Chaos Engineering'?", a: "Proactively injecting failures (knocking a server offline) into a production system to ensure automated recovery mechanisms actually work." },
            { q: "When is a CAB (Change Advisory Board) needed?", a: "Only for significant 'Normal Changes' requiring broad cross-functional risk assessment. Routine/Standard changes bypass the CAB." },
            { q: "Explain the 'Focus on Value' principle.", a: "Everything the organization does must eventually map back to creating perceived value for the stakeholders/consumers." },
            { q: "Explain 'Start Where You Are'.", a: "Avoid 'rip and replace'. Objectively assess the current state by directly observing it, and leverage what already works." },
            { q: "What does 'Keep it Simple and Practical' advocate?", a: "Eliminating pure waste. If a process step, metric, or report provides no value, stop doing it completely." },
            { q: "Why 'Optimize and Automate' in that order?", a: "If you automate an inefficient, broken process, you just create a bad outcome faster. Simplify and optimize first." },
            { q: "Name the Four Dimensions of Service Management.", a: "1. Organizations & People\\n2. Information & Technology\\n3. Partners & Suppliers\\n4. Value Streams & Processes." },
            { q: "What does 'Organizations and People' focus on?", a: "Culture, roles, skills, trust, and breaking down silos to ensure psychological safety and collaboration." },
            { q: "What is the 'Service Value System' (SVS)?", a: "The core ITIL architecture showing how Opportunity/Demand feeds into the system and is transformed into Value." },
            { q: "What are the components of the SVS?", a: "Guiding Principles, Governance, Service Value Chain, Practices, and Continual Improvement." },
            { q: "Name the 6 activities of the Service Value Chain (SVC).", a: "Plan, Improve, Engage, Design & Transition, Obtain/Build, Deliver & Support." },
            { q: "Which SVC activity acts as the front door?", a: "Engage. It provides understanding of stakeholder needs and continual transparent engagement." },
            { q: "Deployment vs Release?", a: "Deployment: Moving code to production. Release: Making that code available for the user to actually use (often via feature flags)." },
            { q: "What is the Continual Improvement Register (CIR)?", a: "A centralized, visible database used to track and prioritize improvement ideas from identification to final action." },
            { q: "What does ITAM (IT Asset Management) manage?", a: "The costs, risks, compliance (licensing), and entire lifecycle of software, hardware, and cloud assets." },
            { q: "Service Configuration Management vs ITAM?", a: "ITAM tracks the financial/license state. Configuration Mgmt (CMDB) tracks the technical relationships and dependencies between components." },
            { q: "What is an 'Exception Event'?", a: "An event indicating a component is operating abnormally or has failed, typically triggering an Incident automatically." },
            { q: "What is the 'Watermelon Effect'?", a: "When IT metrics (SLAs) are all green on the outside, but the actual user experience is terrible (red on the inside)." },
            { q: "Service Desk's primary role?", a: "To capture demand for incident resolution and service requests, acting as the Single Point of Contact (SPOC)." },
            { q: "Incident vs Service Request?", a: "Incident: An unplanned interruption (fix what's broken). Service Request: A planned request for a standard service (install software)." },
            { q: "Problem vs Incident?", a: "Incident: The actual outage. Problem: The underlying root cause of one or more incidents." },
            { q: "What is a 'Known Error'?", a: "A problem where the root cause is understood, and a workaround is identified, but a permanent structural fix hasn't been deployed yet." },
            { q: "Role of a 'Service Broker'?", a: "Acts as an intermediary, integrating services from multiple distinct suppliers to present a unified service to the business." },
            { q: "What is 'Blue/Green Deployment'?", a: "Maintaining two identical production environments to route traffic instantly between versions, allowing for zero-downtime releases and rapid rollbacks." },
            { q: "What is 'Canary Release'?", a: "Gradually routing a small percentage of user traffic to a new version to test for errors before rolling it out to everyone." },
            { q: "What is a 'Workaround'?", a: "A temporary solution (like rebooting) that restores service (resolves Incident) while developers find the permanent fix (solves Problem)." },
            { q: "Utility vs Warranty?", a: "Utility: Fit for purpose (has the right features). Warranty: Fit for use (is available, secure, and performant). Value needs both." },
            { q: "What does 'Organizational Change Management' (OCM) do?", a: "Manages the 'People' side of change, dealing with resistance and ensuring staff adapt to new tools or workflows." },
            { q: "What is a 'Major Incident'?", a: "An outage with severe business impact requiring an immediate, coordinated, cross-team emergency response (often using Swarming)." },
            { q: "What is a 'Post-Incident Review' (PIR)?", a: "A blameless analysis conducted after a major incident to find the root cause and implement systemic improvements." },
            { q: "What is 'Technical Debt'?", a: "The implied cost of rework caused by choosing a fast, 'hacky' solution now instead of doing it right the first time." },
            { q: "What is 'Value Stream Mapping'?", a: "A Lean technique to visually map the end-to-end flow of work to identify bottlenecks, waste, and areas for automation." },
            { q: "What is a 'T-shaped' professional?", a: "Someone with deep expertise in one specific area (the vertical bar) but broad knowledge across many areas to facilitate collaboration (the horizontal bar)." },
            { q: "Dark Launching?", a: "Deploying a feature to production but hiding it from the UI, testing its backend performance on real traffic before users see it." },
            { q: "Define 'IT Service'.", a: "A means of enabling value co-creation by facilitating outcomes customers want, without them having to manage specific costs and risks." },
            { q: "What is a 'Standard Change'?", a: "A low-risk, pre-authorized, repeatable change (like a password reset) that does not require CAB approval." },
            { q: "What is 'Shadow IT'?", a: "When business units buy/use tech (SaaS apps) without IT's knowledge, creating hidden security risks and fragmented data." },
            { q: "What is 'Omnichannel' support?", a: "Providing seamless IT support across multiple interconnected channels (chat, email, phone, portal) based on user preference." },
            { q: "What does the 'Service Catalogue' provide?", a: "A consumer-facing menu of all active service offerings, detailing what is available, costs, and SLAs." },
            { q: "Output vs Outcome?", a: "Output: A physical deliverable (a sales report). Outcome: The business result of using that output (sales increased by 10%). Value is in Outcomes." },
            { q: "What is 'Swarming'?", a: "A modern incident response where multiple experts collaborate instantly (often in ChatOps) instead of bouncing tickets between tiered support levels." },
            { q: "What is 'Cloud FinOps'?", a: "Financial management for the cloud, tracking variable spend models to ensure maximum business value and cost optimization." }
        ];

        let currentIndex = 0;
        const cardElem = document.getElementById('card');
        const qText = document.getElementById('question-text');
        const aText = document.getElementById('answer-text');
        const progressText = document.getElementById('progress-text');
        const prevBtn = document.getElementById('prev-btn');
        const nextBtn = document.getElementById('next-btn');

        function renderCard() {
            // Reset rotation
            cardElem.classList.remove('flipped');
            
            // Wait for flip animation to finish before changing text (optional, but looks better)
            setTimeout(() => {
                qText.textContent = cards[currentIndex].q;
                aText.textContent = cards[currentIndex].a;
                progressText.textContent = \`\${currentIndex + 1} / \${cards.length}\`;
                
                prevBtn.disabled = currentIndex === 0;
                nextBtn.disabled = currentIndex === cards.length - 1;
            }, 100); 
        }

        function flipCard() {
            cardElem.classList.toggle('flipped');
        }

        function nextCard() {
            if (currentIndex < cards.length - 1) {
                currentIndex++;
                renderCard();
            }
        }

        function prevCard() {
            if (currentIndex > 0) {
                currentIndex--;
                renderCard();
            }
        }

        // Keyboard navigation
        document.addEventListener('keydown', (e) => {
            if (e.key === 'ArrowRight') nextCard();
            if (e.key === 'ArrowLeft') prevCard();
            if (e.key === ' ' || e.key === 'Enter') {
                flipCard();
                e.preventDefault(); // Prevent scrolling
            }
        });

        // Init
        renderCard();

    </script>
</body>
</html>`;

fs.writeFileSync(targetFile, template, 'utf8');
console.log('Flashcards generated successfully at: ' + targetFile);
