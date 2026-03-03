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
- **Top-Level Vendor Hierarchies**: All ML certification paths must be grouped under three primary vendor directories: `exams/aws/`, `exams/azure/`, and `exams/gcp/`.
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
- [x] Move existing folder to new `exams/gcp/` hierarchy.
- [x] Ensure 5 sets, Revision Guide, and Flashcards follow the Universal Template.
- [x] Link securely in simplified dashboard.

### Step 2: Professional Machine Learning Engineer
- [ ] Create dedicated folder (`exams/gcp/pro-ml/`)
- [ ] Generate 5 full mock exam sets using the Universal Template
- [ ] Generate comprehensive Revision Guide (`revision.html`)
- [ ] Generate Minimalistic Flashcards (> 50 cards, `flashcards.html`)
- [ ] Link securely in simplified dashboard.

---

## 2. AWS ML Path (`exams/aws/`)
### Step 1: AWS Certified Cloud Practitioner
- [ ] Create dedicated folder (`exams/aws/cloud-practitioner/`)
- [ ] Generate 5 full mock exam sets using the Universal Template
- [ ] Generate comprehensive Revision Guide (`revision.html`)
- [ ] Generate Minimalistic Flashcards (> 50 cards, `flashcards.html`)
- [ ] Link securely in simplified dashboard.

### Step 2: AWS Certified AI Practitioner (Data/AI Foundations)
*Can salvage data from `to-be-deleted/aws_ai.html`.*
- [ ] Create dedicated folder (`exams/aws/ai-practitioner/`)
- [ ] Generate 5 full mock exam sets using the Universal Template
- [ ] Generate comprehensive Revision Guide (`revision.html`)
- [ ] Generate Minimalistic Flashcards (> 50 cards, `flashcards.html`)
- [ ] Link securely in simplified dashboard.

### Step 3: AWS Certified Machine Learning - Specialty
*Currently exists at `exams/aws-ml/`. Needs to be moved to `exams/aws/ml-specialty/`.*
- [x] Create new hierarchy `exams/aws/ml-specialty/` and move assets.
- [x] Verify 5 mock exam sets exist using identical template.
- [x] Verify comprehensive Revision Guide (`revision.html`) exists.
- [x] Verify Minimalistic Flashcards (> 50 cards, `flashcards.html`) exist.
- [ ] Link securely in simplified dashboard.

---

## 3. Azure ML Path (`exams/azure/`)
### Step 1: Azure AI Fundamentals (AI-900)
- [ ] Create dedicated folder (`exams/azure/ai-900/`)
- [ ] Generate 5 full mock exam sets using the Universal Template
- [ ] Generate comprehensive Revision Guide (`revision.html`)
- [ ] Generate Minimalistic Flashcards (> 50 cards, `flashcards.html`)
- [ ] Link securely in simplified dashboard.

### Step 2: Azure Data Scientist Associate (DP-100)
*Currently exists at `exams/azure-ml/`. Needs to be moved to `exams/azure/dp-100/`.*
- [ ] Create new hierarchy `exams/azure/dp-100/` and move assets.
- [x] Verify 5 mock exam sets exist using identical template.
- [x] Verify comprehensive Revision Guide (`revision.html`) exists.
- [x] Verify Minimalistic Flashcards (> 50 cards, `flashcards.html`) exist.
- [x] Link securely in simplified dashboard.

---

## 4. Legacy Expansions
```markdown
- [ ] Create dedicated folder (`exams/itil-v4/`)
```
- [ ] Generate 5 full mock exam sets using the Universal Template (extracting data from `to-be-deleted/itil-v4-exam.html`)

### GitHub Certification (GH300)
- [ ] Create dedicated folder (`exams/gh300/`)
- [ ] Generate 5 full mock exam sets using the Universal Template (extracting data from `to-be-deleted/gh300.html`)

### Life in the UK
- [ ] Create dedicated folder (`exams/life-in-uk/`)
- [ ] Generate 5 full mock exam sets using the Universal Template (extracting data from `to-be-deleted/life_in_uk.html`)

---

## 4. Creative ML Master's Path (`exams/creative-ml/`) (Deprioritized)
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

## 5. Final Deprecation Pipeline
*The `to-be-deleted/` folder is temporarily preserved as a data source for rebuilding legacy exams into the Universal Template. Once extraction is complete, it must be purged to avoid content duplication.*
- [ ] Verify all useful content has been extracted from `to-be-deleted/`.
- [ ] Delete the `to-be-deleted/` directory and all its contents entirely.