# Exam Platform Backlog

### Structural Golden Rules for Every Exam
- **Folder Containment**: Everything related to an exam (Mock Exams, Revision Guides, Flashcards) MUST be together in a single dedicated folder inside `exams/`. No exam assets should live in the root directory.
- **Universal Template**: Every single exam MUST be developed on the exact same template and features as GCP Digital Leader. Everything must be linked together in the `index.html` dashboard.
- **Mock Exams**: Minimum of 5 full sets per certification.
- **Revision Guide**: At least 1 comprehensive revision HTML file per exam inside its folder.
- **Flashcards**: Dedicated set of flashcards per exam inside its folder.
  - *Must be minimalistic:* Front and back content displayed on the same face.
  - *Navigation:* Clicking the right half of the screen goes to the next card, clicking the left half goes to the previous card. No tiny buttons.
  - *Volume:* Must comprehensively cover the exam topics, significantly more than 10 cards.
- **Cleanup Strictness**: No Python, no generation scripts, no scatter in the main or exam folders. Everything old/dev must be moved to `to-be-deleted/`. Cloudflare compatibility is paramount (HTML/CSS/JS only).

---

# Exam Platform Master Backlog

## Structural Golden Rules for Every Exam
- **Top-Level Vendor Hierarchies**: All ML certification paths must be grouped under three primary vendor directories: `exams/aws/`, `exams/azure/`, and `exams/gcp/`. Adding ITIL as a core methodology path under `exams/itil/`.
- **Progression Paths**: Each vendor folder must contain a logical progression of exams, from foundational knowledge to the Professional ML certification.
- **Folder Containment**: Everything related to an individual exam (Mock Exams, Revision Guides, Flashcards) MUST be strictly contained in its dedicated sub-folder (e.g., `exams/aws/ml-specialty/`). No exam assets should live in the root directory.
- **Universal Template**: Every single exam MUST be developed on the exact same template. Everything must be linked together in a simplified `index.html` dashboard under its respective vendor.
- **Mock Exams**: Minimum of 5 full sets per certification step.
- **Revision Guide**: At least 1 comprehensive revision HTML file per exam inside its folder.
- **Flashcards**: Dedicated set of flashcards per exam inside its folder.
  - *Must be minimalistic:* Front and back content displayed on the same face.
  - *Navigation:* Clicking the right half of the screen goes to the next card, clicking the left half goes to the previous card. No tiny buttons.
  - *Volume:* Must comprehensively cover the exam topics, significantly more than 10 cards.
- **Cleanup Strictness**: No Python, no generation scripts, no scatter in the main or exam folders. Everything old/dev must be moved to `to-be-deleted/`. Cloudflare compatibility is paramount (HTML/CSS/JS only).

---

## 1. Google Cloud ML Path (`exams/gcp/`)

### Step 1: Cloud Digital Leader (Foundations)
*Currently exists at `exams/gcp-digital-leader/`. Needs to be moved to `exams/gcp/digital-leader/`.*
- [ ] **Infrastructure Setup**
  - [x] Create dedicated folder (`exams/gcp/`)
  - [x] Move existing folder to new `exams/gcp/` hierarchy
- [ ] **Mock Exams Generation**
  - [x] Verify Set 1 of 5
  - [x] Verify Set 2 of 5
  - [x] Verify Set 3 of 5
  - [x] Verify Set 4 of 5
  - [x] Verify Set 5 of 5
- [ ] **Revision Guide Creation**
  - [x] Verify comprehensive `revision.html`
- [ ] **Flashcards Creation**
  - [x] Verify Minimalistic Flashcards (> 50 cards, `flashcards.html`)
  - [x] Verify right/left click navigation
- [ ] **Integration**
  - [x] Link securely in simplified dashboard
  - [x] Verify mobile-first UI constraints

### Step 2: Professional Machine Learning Engineer
- [ ] **Infrastructure Setup**
  - [ ] Create dedicated folder (`exams/gcp/pro-ml/`)
  - [ ] Copy Universal Template structure (HTML/CSS/JS)
- [ ] **Mock Exams Generation**
  - [ ] Generate Set 1 of 5 (50+ questions with explanations)
  - [ ] Generate Set 2 of 5
  - [ ] Generate Set 3 of 5
  - [ ] Generate Set 4 of 5
  - [ ] Generate Set 5 of 5
- [ ] **Revision Guide Creation**
  - [ ] Aggregate key topics
  - [ ] Generate comprehensive `revision.html`
- [ ] **Flashcards Creation**
  - [ ] Extract Q&A pairs
  - [ ] Generate Minimalistic Flashcards (> 50 cards, `flashcards.html`)
  - [ ] Implement right/left click navigation
- [ ] **Integration**
  - [ ] Link assets securely in the platform dashboard
  - [ ] Verify mobile-first UI constraints

---

## 2. AWS ML Path (`exams/aws/`)

### Step 1: AWS Certified Cloud Practitioner
- [ ] **Infrastructure Setup**
  - [ ] Create dedicated folder (`exams/aws/cloud-practitioner/`)
  - [ ] Copy Universal Template structure (HTML/CSS/JS)
- [ ] **Mock Exams Generation**
  - [ ] Generate Set 1 of 5 (50+ questions with explanations)
  - [ ] Generate Set 2 of 5
  - [ ] Generate Set 3 of 5
  - [ ] Generate Set 4 of 5
  - [ ] Generate Set 5 of 5
- [ ] **Revision Guide Creation**
  - [ ] Aggregate key topics
  - [ ] Generate comprehensive `revision.html`
- [ ] **Flashcards Creation**
  - [ ] Extract Q&A pairs
  - [ ] Generate Minimalistic Flashcards (> 50 cards, `flashcards.html`)
  - [ ] Implement right/left click navigation
- [ ] **Integration**
  - [ ] Link assets securely in the platform dashboard
  - [ ] Verify mobile-first UI constraints

### Step 2: AWS Certified AI Practitioner (Data/AI Foundations)
*Can salvage data from `to-be-deleted/aws_ai.html`.*
- [ ] **Infrastructure Setup**
  - [ ] Create dedicated folder (`exams/aws/ai-practitioner/`)
  - [ ] Copy Universal Template structure (HTML/CSS/JS)
- [ ] **Mock Exams Generation**
  - [ ] Extract existing data and generate Set 1 of 5
  - [ ] Generate Set 2 of 5
  - [ ] Generate Set 3 of 5
  - [ ] Generate Set 4 of 5
  - [ ] Generate Set 5 of 5
- [ ] **Revision Guide Creation**
  - [ ] Aggregate key topics
  - [ ] Generate comprehensive `revision.html`
- [ ] **Flashcards Creation**
  - [ ] Extract Q&A pairs
  - [ ] Generate Minimalistic Flashcards (> 50 cards, `flashcards.html`)
  - [ ] Implement right/left click navigation
- [ ] **Integration**
  - [ ] Link assets securely in the platform dashboard
  - [ ] Verify mobile-first UI constraints

### Step 3: AWS Certified Machine Learning - Specialty
*Currently exists at `exams/aws-ml/`. Needs to be moved to `exams/aws/ml-specialty/`.*
- [ ] **Infrastructure Setup**
  - [x] Create new hierarchy `exams/aws/ml-specialty/` and move assets
- [ ] **Mock Exams Generation**
  - [x] Verify Set 1 of 5 exists using identical template
  - [x] Verify Set 2 of 5
  - [x] Verify Set 3 of 5
  - [x] Verify Set 4 of 5
  - [x] Verify Set 5 of 5
- [ ] **Revision Guide Creation**
  - [x] Verify comprehensive Revision Guide (`revision.html`) exists
- [ ] **Flashcards Creation**
  - [x] Verify Minimalistic Flashcards (> 50 cards, `flashcards.html`) exist
  - [x] Verify right/left click navigation
- [ ] **Integration**
  - [ ] Link securely in simplified dashboard
  - [ ] Verify mobile-first UI constraints

---

## 3. Azure ML Path (`exams/azure/`)

### Step 1: Azure AI Fundamentals (AI-900)
- [ ] **Infrastructure Setup**
  - [ ] Create dedicated folder (`exams/azure/ai-900/`)
  - [ ] Copy Universal Template structure (HTML/CSS/JS)
- [ ] **Mock Exams Generation**
  - [ ] Generate Set 1 of 5 (50+ questions with explanations)
  - [ ] Generate Set 2 of 5
  - [ ] Generate Set 3 of 5
  - [ ] Generate Set 4 of 5
  - [ ] Generate Set 5 of 5
- [ ] **Revision Guide Creation**
  - [ ] Aggregate key topics
  - [ ] Generate comprehensive `revision.html`
- [ ] **Flashcards Creation**
  - [ ] Extract Q&A pairs
  - [ ] Generate Minimalistic Flashcards (> 50 cards, `flashcards.html`)
  - [ ] Implement right/left click navigation
- [ ] **Integration**
  - [ ] Link assets securely in the platform dashboard
  - [ ] Verify mobile-first UI constraints

### Step 2: Azure Data Scientist Associate (DP-100)
*Currently exists at `exams/azure-ml/`. Needs to be moved to `exams/azure/dp-100/`.*
- [ ] **Infrastructure Setup**
  - [ ] Create new hierarchy `exams/azure/dp-100/` and move assets
- [ ] **Mock Exams Generation**
  - [x] Verify Set 1 of 5 exists using identical template
  - [x] Verify Set 2 of 5
  - [x] Verify Set 3 of 5
  - [x] Verify Set 4 of 5
  - [x] Verify Set 5 of 5
- [ ] **Revision Guide Creation**
  - [x] Verify comprehensive Revision Guide (`revision.html`) exists
- [ ] **Flashcards Creation**
  - [x] Verify Minimalistic Flashcards (> 50 cards, `flashcards.html`) exist
  - [x] Verify right/left click navigation
- [ ] **Integration**
  - [x] Link securely in simplified dashboard
  - [ ] Verify mobile-first UI constraints

---

## 4. ITIL Path (`exams/itil/`)

### Step 1: ITIL v4 Foundation
*Can salvage data from `to-be-deleted/itil-v4-exam.html`.*
- [ ] **Infrastructure Setup**
  - [ ] Create dedicated folder (`exams/itil/v4-foundation/`)
  - [ ] Copy Universal Template structure (HTML/CSS/JS)
- [ ] **Mock Exams Generation**
  - [ ] Extract existing data and generate Set 1 of 5
  - [ ] Generate Set 2 of 5
  - [ ] Generate Set 3 of 5
  - [ ] Generate Set 4 of 5
  - [ ] Generate Set 5 of 5
- [ ] **Revision Guide Creation**
  - [ ] Aggregate key topics
  - [ ] Generate comprehensive `revision.html`
- [ ] **Flashcards Creation**
  - [ ] Extract Q&A pairs
  - [ ] Generate Minimalistic Flashcards (> 50 cards, `flashcards.html`)
  - [ ] Implement right/left click navigation
- [ ] **Integration**
  - [ ] Link assets securely in the platform dashboard
  - [ ] Verify mobile-first UI constraints

### Step 2: ITIL v5 Foundation
- [ ] **Infrastructure Setup**
  - [ ] Create dedicated folder (`exams/itil/v5-foundation/`)
  - [ ] Copy Universal Template structure (HTML/CSS/JS)
- [ ] **Mock Exams Generation**
  - [ ] Generate Set 1 of 5 (50+ questions with explanations)
  - [ ] Generate Set 2 of 5
  - [ ] Generate Set 3 of 5
  - [ ] Generate Set 4 of 5
  - [ ] Generate Set 5 of 5
- [ ] **Revision Guide Creation**
  - [ ] Aggregate key topics
  - [ ] Generate comprehensive `revision.html`
- [ ] **Flashcards Creation**
  - [ ] Extract Q&A pairs
  - [ ] Generate Minimalistic Flashcards (> 50 cards, `flashcards.html`)
  - [ ] Implement right/left click navigation
- [ ] **Integration**
  - [ ] Link assets securely in the platform dashboard
  - [ ] Verify mobile-first UI constraints

### Step 3: ITIL Specialty Certificate
- [ ] **Infrastructure Setup**
  - [ ] Create dedicated folder (`exams/itil/specialty-certificate/`)
  - [ ] Copy Universal Template structure (HTML/CSS/JS)
- [ ] **Mock Exams Generation**
  - [ ] Generate Set 1 of 5 (50+ questions with explanations)
  - [ ] Generate Set 2 of 5
  - [ ] Generate Set 3 of 5
  - [ ] Generate Set 4 of 5
  - [ ] Generate Set 5 of 5
- [ ] **Revision Guide Creation**
  - [ ] Aggregate key topics
  - [ ] Generate comprehensive `revision.html`
- [ ] **Flashcards Creation**
  - [ ] Extract Q&A pairs
  - [ ] Generate Minimalistic Flashcards (> 50 cards, `flashcards.html`)
  - [ ] Implement right/left click navigation
- [ ] **Integration**
  - [ ] Link assets securely in the platform dashboard
  - [ ] Verify mobile-first UI constraints

---

## 5. Legacy Expansions

### GitHub Certification (GH300)
- [ ] **Infrastructure Setup**
  - [ ] Create dedicated folder (`exams/gh300/`)
  - [ ] Copy Universal Template structure (HTML/CSS/JS)
- [ ] **Mock Exams Generation**
  - [ ] Extract data from `to-be-deleted/gh300.html` and generate Set 1 of 5
  - [ ] Generate Set 2 of 5
  - [ ] Generate Set 3 of 5
  - [ ] Generate Set 4 of 5
  - [ ] Generate Set 5 of 5
- [ ] **Revision Guide Creation**
  - [ ] Aggregate key topics
  - [ ] Generate comprehensive `revision.html`
- [ ] **Flashcards Creation**
  - [ ] Extract Q&A pairs
  - [ ] Generate Minimalistic Flashcards (> 50 cards, `flashcards.html`)
  - [ ] Implement right/left click navigation
- [ ] **Integration**
  - [ ] Link securely in simplified dashboard
  - [ ] Verify mobile-first UI constraints

### Life in the UK
- [ ] **Infrastructure Setup**
  - [ ] Create dedicated folder (`exams/life-in-uk/`)
  - [ ] Copy Universal Template structure (HTML/CSS/JS)
- [ ] **Mock Exams Generation**
  - [ ] Extract data from `to-be-deleted/life_in_uk.html` and generate Set 1 of 5
  - [ ] Generate Set 2 of 5
  - [ ] Generate Set 3 of 5
  - [ ] Generate Set 4 of 5
  - [ ] Generate Set 5 of 5
- [ ] **Revision Guide Creation**
  - [ ] Aggregate key topics
  - [ ] Generate comprehensive `revision.html`
- [ ] **Flashcards Creation**
  - [ ] Extract Q&A pairs
  - [ ] Generate Minimalistic Flashcards (> 50 cards, `flashcards.html`)
  - [ ] Implement right/left click navigation
- [ ] **Integration**
  - [ ] Link securely in simplified dashboard
  - [ ] Verify mobile-first UI constraints

---

## 6. Creative ML Master's Path (`exams/creative-ml/`) (Deprioritized)
*Objective: Build an in-depth, comprehensive "Master's Degree" shortcut for AI/ML. This is a learning journey, not an exam simulator. Chapter-wise, visual, with no fluff—based on the "Hands On Machine Learning with Scikit Learn and TensorFlow" textbook and supplemented by expert online knowledge.*

**Core Tasks:**
- [ ] Create interactive, no-fluff Revision Guides (`revision_chapter_X.html`) for every chapter.
- [ ] Create detailed Minimalistic Flashcards (`flashcards_chapter_X.html`) for every chapter.
- [ ] Optionally create quizzes (instead of strict mock exams) to test understanding.
- [ ] Link all chapters interactively in the `index.html` dashboard.

**Part 1: The Fundamentals of Machine Learning (Book Baseline)**
- [ ] Chapter 1: The Machine Learning Landscape
- [ ] Chapter 2: End-to-End Machine Learning Project
- [ ] Chapter 3: Classification
- [ ] Chapter 4: Training Models (Linear Regression, Gradient Descent, Logistic Regression)
- [ ] Chapter 5: Support Vector Machines
- [ ] Chapter 6: Decision Trees
- [ ] Chapter 7: Ensemble Learning and Random Forests
- [ ] Chapter 8: Dimensionality Reduction
- [ ] Chapter 9: Unsupervised Learning Techniques

**Part 2: Neural Networks and Deep Learning (Book Baseline)**
- [ ] Chapter 10: Introduction to Artificial Neural Networks with Keras
- [ ] Chapter 11: Training Deep Neural Networks
- [ ] Chapter 12: Custom Models and Training with TensorFlow
- [ ] Chapter 13: Loading and Preprocessing Data
- [ ] Chapter 14: Deep Computer Vision Using Convolutional Neural Networks
- [ ] Chapter 15: Processing Sequences Using RNNs and CNNs
- [ ] Chapter 16: Natural Language Processing with RNNs and Attention
- [ ] Chapter 17: Representation Learning and Generative Learning (Autoencoders and GANs)
- [ ] Chapter 18: Reinforcement Learning
- [ ] Chapter 19: Training and Deploying TensorFlow Models at Scale

**Part 3: Master's Degree Augmentation (Internet Research / Advanced)**
- [ ] Advanced NLP: Large Language Models (LLMs), Transformer Architectures deep-dive, RAG.
- [ ] Advanced Vision: Vision Transformers (ViTs), Diffusion Models.
- [ ] Specialized Architectures: Graph Neural Networks (GNNs).
- [ ] MLOps & Production: Advanced model monitoring, drift detection, and CI/CD for ML.

---

## 7. Final Deprecation Pipeline
*The `to-be-deleted/` folder is temporarily preserved as a data source for rebuilding legacy exams into the Universal Template. Once extraction is complete, it must be purged to avoid content duplication.*
- [ ] Verify all useful content has been extracted from `to-be-deleted/`.
- [ ] Delete the `to-be-deleted/` directory and all its contents entirely.