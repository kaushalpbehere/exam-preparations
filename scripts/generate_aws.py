aws_ml_questions = [
    {
        "q": "You are training a deep learning model on Amazon SageMaker. Which feature allows you to automatically stop a training job if the model's performance on the validation set stops improving?",
        "options": ["(A) SageMaker Debugger", "(B) Spot Instances", "(C) Managed Spot Training", "(D) Early Stopping with Hyperparameter Tuning"],
        "ans": "D",
        "exp": "Early Stopping monitors the validation objective metric during a hyperparameter tuning job and automatically terminates jobs that are not improving, saving time and cost."
    },
    {
        "q": "When deploying a large language model (LLM) on Amazon SageMaker, which instance family is best suited for accelerating distributed inference?",
        "options": ["(A) T-family instances", "(B) M-family instances", "(C) Inferentia (Inf1/Inf2) or Trn1 instances", "(D) C-family instances"],
        "ans": "C",
        "exp": "AWS Inferentia and Trainium instances are custom-built accelerators designed to provide high-performance and cost-effective deep learning inference and training."
    },
    {
        "q": "Your application uses RAG (Retrieval-Augmented Generation) with Amazon Bedrock. Which AWS service is natively integrated to act as a highly scalable vector database for semantic search?",
        "options": ["(A) Amazon RDS for MySQL", "(B) Amazon OpenSearch Serverless (Vector Engine)", "(C) Amazon DynamoDB", "(D) Amazon S3"],
        "ans": "B",
        "exp": "Amazon OpenSearch Serverless includes a vector engine specifically optimized for managing embeddings and executing rapid semantic similarity searches required for RAG architectures."
    },
    {
        "q": "You are implementing a machine learning pipeline using SageMaker Pipelines. Which step type should you use to register a model in the Model Registry if it meets a specific accuracy threshold?",
        "options": ["(A) ProcessingStep", "(B) TrainingStep", "(C) ConditionStep", "(D) TuningStep"],
        "ans": "C",
        "exp": "A ConditionStep evaluates properties of previous steps (e.g., model evaluation metrics) and determines whether the pipeline should proceed to subsequent steps like model registration."
    },
    {
        "q": "Which Amazon Bedrock feature allows you to securely customize foundation models using your own private data without sharing that data with the foundation model providers?",
        "options": ["(A) Knowledge Bases", "(B) Model Customization (Fine-Tuning)", "(C) Provisioned Throughput", "(D) Agents"],
        "ans": "B",
        "exp": "Bedrock allows fine-tuning and continued pre-training of models in a secure VPC environment, ensuring customer data remains private and is never used to train the base model."
    },
    {
        "q": "What is the primary function of Amazon SageMaker Feature Store?",
        "options": ["(A) To host pre-trained models", "(B) To provide a fully managed repository to store, update, retrieve, and share ML features", "(C) To visualize neural network architectures", "(D) To translate text across languages"],
        "ans": "B",
        "exp": "SageMaker Feature Store is a centralized repository for organizing ML features, supporting both low-latency online retrieval for inference and offline retrieval for training."
    },
    {
        "q": "You need to automate a workflow that invokes an Amazon Bedrock foundation model in response to an Amazon S3 file upload. Which service acts as the orchestration layer?",
        "options": ["(A) AWS Lambda", "(B) Amazon CloudFront", "(C) AWS Glue", "(D) Amazon EMR"],
        "ans": "A",
        "exp": "AWS Lambda can be triggered directly by S3 events, acting as the serverless compute layer to invoke the Bedrock API with the new data."
    },
    {
        "q": "How does SageMaker Model Monitor detect feature attribution drift in a deployed ML model?",
        "options": ["(A) By training a new model automatically", "(B) By comparing the distribution of incoming inference features to a baseline established during training", "(C) By manually querying the CloudWatch logs", "(D) By scaling the endpoint up"],
        "ans": "B",
        "exp": "Model Monitor captures incoming requests and compares them against a baseline computed during training to detect data drift, concept drift, or feature attribution drift."
    },
    {
        "q": "Which data format is highly recommended for parallel and distributed training jobs in Amazon SageMaker due to its optimized row/columnar structure and compression?",
        "options": ["(A) CSV", "(B) JSON", "(C) Parquet", "(D) Pipe mode with RecordIO-Protobuf"],
        "ans": "D",
        "exp": "Pipe mode streams data directly from S3 to the container in RecordIO-Protobuf format, reducing startup times and preventing the need to download the entire dataset to disk."
    },
    {
        "q": "When using Amazon Titan embeddings in a RAG system, what mathematical operation is typically used to determine the similarity between the user query embedding and document embeddings?",
        "options": ["(A) Cross-entropy loss", "(B) Cosine similarity", "(C) Softmax function", "(D) Gradient descent"],
        "ans": "B",
        "exp": "Cosine similarity calculates the cosine of the angle between two multi-dimensional vectors, serving as a standard metric to determine semantic closeness in vector databases."
    },
    {
        "q": "Which service allows you to interactively query and analyze data stored in Amazon S3 using standard SQL without provisioning any infrastructure?",
        "options": ["(A) Amazon Redshift", "(B) Amazon Athena", "(C) Amazon EMR", "(D) AWS Glue"],
        "ans": "B",
        "exp": "Amazon Athena is an interactive, serverless query service that makes it easy to analyze data directly in S3 using standard SQL."
    },
    {
        "q": "You want to deploy multiple Machine Learning models to a single SageMaker endpoint to reduce infrastructure costs. What feature should you use?",
        "options": ["(A) Multi-Model Endpoints (MME)", "(B) SageMaker Autopilot", "(C) A/B Testing Endpoints", "(D) SageMaker Canvas"],
        "ans": "A",
        "exp": "MMEs allow you to host thousands of models on a single endpoint, sharing the underlying compute instances and dynamically loading models into memory."
    },
    {
        "q": "Which AWS security service continuously monitors your SageMaker notebooks and S3 buckets for malicious activity and unauthorized behavior?",
        "options": ["(A) AWS Shield", "(B) AWS WAF", "(C) Amazon GuardDuty", "(D) AWS KMS"],
        "ans": "C",
        "exp": "Amazon GuardDuty is an intelligent threat detection service that continuously monitors AWS accounts, including S3 access anomalies and malicious network traffic."
    },
    {
        "q": "What is the primary use case for Amazon SageMaker Data Wrangler?",
        "options": ["(A) Visual data preparation, cleaning, and feature engineering without writing code", "(B) Deploying LLMs to production", "(C) Monitoring model drift", "(D) Allocating GPU instances"],
        "ans": "A",
        "exp": "Data Wrangler provides a visual interface to seamlessly import data from sources like S3 or Athena, clean it, and transform it for machine learning."
    },
    {
        "q": "In the context of generative AI on AWS, what is a 'Knowledge Base' in Amazon Bedrock?",
        "options": ["(A) A static wiki page for documentation", "(B) A managed RAG capability connecting foundation models to internal company data sources", "(C) A SQL database for structured data", "(D) A predefined set of system prompts"],
        "ans": "B",
        "exp": "Knowledge Bases for Amazon Bedrock securely connects FMs to internal data sources for fully managed Retrieval-Augmented Generation (RAG)."
    },
    {
        "q": "Which Amazon SageMaker feature automatically builds, trains, and tunes the best machine learning models based on your data?",
        "options": ["(A) SageMaker Clarify", "(B) SageMaker Autopilot", "(C) SageMaker Debugger", "(D) SageMaker Neo"],
        "ans": "B",
        "exp": "SageMaker Autopilot is an AutoML solution that explores various algorithms and hyperparameters to automatically generate the best possible model for a dataset."
    },
    {
        "q": "When preparing a dataset for an NLP model, which AWS service can you use to identify and redact Personally Identifiable Information (PII) before training?",
        "options": ["(A) Amazon Macie", "(B) AWS CloudTrail", "(C) Amazon Inspector", "(D) AWS Config"],
        "ans": "A",
        "exp": "Amazon Macie is a data security service that uses machine learning to automatically discover, classify, and protect sensitive data like PII in AWS."
    },
    {
        "q": "You need to compile and optimize an ML model formulated in PyTorch to run efficiently on edge devices (e.g., Raspberry Pi). Which service helps achieve this?",
        "options": ["(A) SageMaker Feature Store", "(B) SageMaker Neo", "(C) AWS IoT Greengrass", "(D) SageMaker Edge Manager"],
        "ans": "B",
        "exp": "SageMaker Neo automatically compiles ML models for specific hardware architectures, optimizing them for faster inference with a smaller footprint on edge devices."
    },
    {
        "q": "What role does AWS Identity and Access Management (IAM) play in securing Amazon Bedrock deployments?",
        "options": ["(A) Compiling foundation models", "(B) Controlling which users or applications can invoke specific foundation models", "(C) Connecting to on-premises databases", "(D) Encrypting vector embeddings"],
        "ans": "B",
        "exp": "IAM controls access to Bedrock APIs, ensuring that only authorized users, roles, and applications can list, view, or invoke specific foundation models."
    },
    {
        "q": "Which container orchestrator can integrate directly with SageMaker for training and inference using Operators?",
        "options": ["(A) Docker Swarm", "(B) Amazon Elastic Container Service (ECS)", "(C) Amazon Elastic Kubernetes Service (EKS)", "(D) AWS Fargate"],
        "ans": "C",
        "exp": "SageMaker Operators for Kubernetes allow developers to manage SageMaker resources (training jobs, endpoints) natively using the Kubernetes API via EKS."
    },
    {
        "q": "When utilizing Amazon Bedrock Agents, what acts as the bridge connecting the LLM to external APIs to execute real-world actions?",
        "options": ["(A) Action Groups mapped to AWS Lambda functions", "(B) CloudWatch Alarms", "(C) Route 53 DNS records", "(D) Amazon SQS Queues"],
        "ans": "A",
        "exp": "Agents use Action Groups equipped with OpenAPI schemas and Lambda functions to define the parameters the FM needs to extract to invoke external APIs."
    },
    {
        "q": "If you need a highly durable, object storage location to store ML model artifacts (like weights and biases) generated during SageMaker training, what do you use?",
        "options": ["(A) Amazon EBS", "(B) Amazon EFS", "(C) Amazon S3", "(D) Amazon FSx"],
        "ans": "C",
        "exp": "Amazon S3 is the standard, highly durable object storage used by SageMaker for ingesting training datasets and storing the output model artifacts (model.tar.gz)."
    },
    {
        "q": "You are training on massive datasets (TB size) where downloading to the local instance volume is too slow. Which input mode should you use?",
        "options": ["(A) File Mode", "(B) Fast File Mode (or Pipe Mode)", "(C) Object Mode", "(D) Block Mode"],
        "ans": "B",
        "exp": "Fast File Mode exposes S3 objects as POSIX files to the container on demand, while Pipe Mode streams data directly from S3, avoiding full local downloads."
    },
    {
        "q": "Which AWS capability helps clarify machine learning models by detecting potential bias and explaining individual predictions via SHAP values?",
        "options": ["(A) SageMaker Clarify", "(B) SageMaker Debugger", "(C) Model Monitor", "(D) Bedrock Evaluation"],
        "ans": "A",
        "exp": "SageMaker Clarify provides insights into model behavior by identifying data or model biases and generating feature importance explanations (SHAP values)."
    },
    {
        "q": "When deploying an Amazon Bedrock model in a highly regulated industry, how do you ensure the API calls do not traverse the public internet?",
        "options": ["(A) By using an AWS WAF", "(B) By utilizing VPC Endpoints (AWS PrivateLink)", "(C) By encrypting data with AWS KMS", "(D) By deploying to a public subnet"],
        "ans": "B",
        "exp": "AWS PrivateLink provides private connectivity between VPCs and AWS services like Bedrock, keeping traffic strictly on the Amazon network without public internet exposure."
    },
    {
        "q": "What is the primary benefit of using Amazon SageMaker Serverless Inference?",
        "options": ["(A) Maximum sustained GPU performance", "(B) Pay only for the compute capacity used during inference without managing instances", "(C) Running models locally on edge devices", "(D) Automated hyperparameter optimization"],
        "ans": "B",
        "exp": "Serverless Inference abstracts underlying instance management and automatically scales compute capacity based on traffic spikes, charging only for the duration of inference."
    },
    {
        "q": "Which AWS service provides a fully managed, scalable Apache Kafka cluster for streaming real-time event data into ML pipelines?",
        "options": ["(A) Amazon Kinesis", "(B) Amazon MSK (Managed Streaming for Apache Kafka)", "(C) Amazon SQS", "(D) AWS Step Functions"],
        "ans": "B",
        "exp": "Amazon MSK makes it easy to ingest and process streaming event data in real-time with Apache Kafka, which is widely used for building streaming ML pipelines."
    },
    {
        "q": "You are building a computer vision model. Which AWS service allows you to send workforce laborers images to draw bounding boxes and annotate them?",
        "options": ["(A) SageMaker Canvas", "(B) SageMaker Profiler", "(C) Amazon Augmented AI (A2I)", "(D) SageMaker Ground Truth"],
        "ans": "D",
        "exp": "SageMaker Ground Truth is a fully managed data labeling service that facilitates the creation of highly accurate training datasets using human labelers (workforces)."
    },
    {
        "q": "In the context of RAG, what is an 'embedding'?",
        "options": ["(A) A HTML snippet injected into a UI", "(B) A dense vector representation of text that captures semantic meaning", "(C) A physical server embedded in a local network", "(D) A cryptographic hash of a document"],
        "ans": "B",
        "exp": "An embedding maps text to a high-dimensional vector space where semantically similar phrases are mathematically close to each other."
    },
    {
        "q": "Which data processing framework does AWS Glue natively run under the hood for large-scale serverless ETL jobs?",
        "options": ["(A) Apache Flink", "(B) Apache Kafka", "(C) Apache Spark", "(D) Hadoop MapReduce"],
        "ans": "C",
        "exp": "AWS Glue uses a distributed Apache Spark environment natively to run serverless Extract, Transform, and Load (ETL) data pipelines."
    },
    {
        "q": "Which service seamlessly integrates with Amazon Bedrock to provide short-term session memory for building conversational chatbot applications?",
        "options": ["(A) Amazon ElastiCache", "(B) Amazon S3", "(C) AWS Glue", "(D) Amazon MSK"],
        "ans": "A",
        "exp": "Amazon ElastiCache (Redis/Memcached) is a high-speed, in-memory datastore perfect for maintaining low-latency conversational history and session states."
    },
    {
        "q": "To mitigate hallucination risks in generative models, a company requires human review for low-confidence ML predictions. Which service supports this workflow?",
        "options": ["(A) Amazon Augmented AI (A2I)", "(B) AWS Config", "(C) AWS Batch", "(D) Amazon CloudWatch"],
        "ans": "A",
        "exp": "Amazon A2I makes it easy to build human review workflows for ML predictions, routing low-confidence outputs to human teams for manual validation."
    },
    {
        "q": "What metric does the 'Recall' performance evaluation measure in a binary classification ML problem?",
        "options": ["(A) The percentage of all predictions that were correct", "(B) The proportion of true positives out of all actual positive instances", "(C) The proportion of true positives out of all predicted positive instances", "(D) The loss function gradient"],
        "ans": "B",
        "exp": "Recall (or Sensitivity) measures a model's ability to correctly identify all actual positive cases (True Positives / (True Positives + False Negatives))."
    },
    {
        "q": "In Amazon SageMaker, what is a Custom Docker container required to have in order to be used for model training?",
        "options": ["(A) A REST API listening on port 8080", "(B) A file named `train` at a specific entry point path that is executable", "(C) A pre-installed local Apache Spark cluster", "(D) A multi-model server daemon"],
        "ans": "B",
        "exp": "For training, SageMaker runs the custom container image and executes the script located at `/opt/ml/code/train` (or an entrypoint specified). Inference requires a web server on port 8080."
    },
    {
        "q": "When processing highly unstructured text documents locally in Python, which open-source library is standard for orchestrating LLM tool chains and vector DB integrations?",
        "options": ["(A) TensorFlow", "(B) Scikit-Learn", "(C) LangChain", "(D) Pandas"],
        "ans": "C",
        "exp": "LangChain is a robust open-source framework specifically designed to simplify the creation of applications using large language models, including chains, agents, and memory."
    },
    {
        "q": "Which AWS service is designed for real-time streaming analytics, allowing you to use SQL directly over incoming data streams?",
        "options": ["(A) Kinesis Data Analytics (Managed Service for Apache Flink)", "(B) Kinesis Data Firehose", "(C) Amazon Athena", "(D) Amazon Redshift"],
        "ans": "A",
        "exp": "Managed Service for Apache Flink (formerly Kinesis Data Analytics) allows you to continuously process and analyze streaming data in real-time."
    },
    {
        "q": "You want to deploy an inference endpoint that updates its model weights dynamically without incurring any downtime. How do you approach this in SageMaker?",
        "options": ["(A) Delete the endpoint and recreate it", "(B) Use the `UpdateEndpoint` API with a new Endpoint Configuration", "(C) Manually SSH into the instance and swap files", "(D) Stop the instance, swap the S3 URI, and start it"],
        "ans": "B",
        "exp": "The `UpdateEndpoint` API performs a blue/green deployment natively, spinning up the new configuration and seamlessly shifting traffic without downtime."
    },
    {
        "q": "Which optimization technique helps a deep neural network generalize better by randomly ignoring a subset of neurons during training?",
        "options": ["(A) Batch Normalization", "(B) Gradient Clipping", "(C) Dropout", "(D) Data Augmentation"],
        "ans": "C",
        "exp": "Dropout is a regularization technique where randomly selected neurons are ignored during training, preventing complex co-adaptations and reducing overfitting."
    },
    {
        "q": "In an ML lifecycle, what defines the process of automatically rebuilding and deploying models when data distributions drift over time?",
        "options": ["(A) CI/CD (Continuous Integration / Continuous Deployment)", "(B) CT (Continuous Training)", "(C) ETL (Extract, Transform, Load)", "(D) RAG (Retrieval-Augmented Generation)"],
        "ans": "B",
        "exp": "Continuous Training (CT) is the MLOps practice of automating the retraining of models when performance degrades or data distributions shift."
    },
    {
        "q": "When evaluating an LLM's response quality against a human-written reference summary, which metric is most commonly used?",
        "options": ["(A) RMSE (Root Mean Square Error)", "(B) ROUGE (Recall-Oriented Understudy for Gisting Evaluation)", "(C) F1-Score", "(D) Log-Loss"],
        "ans": "B",
        "exp": "ROUGE measures the overlap of n-grams between the system-generated text and the reference text, standardly used for summarization evaluation."
    },
    {
        "q": "Which Amazon S3 feature ensures that training datasets are completely unchangeable for compliance and auditing purposes?",
        "options": ["(A) S3 Versioning", "(B) S3 Intelligent-Tiering", "(C) S3 Object Lock (WORM)", "(D) S3 Transfer Acceleration"],
        "ans": "C",
        "exp": "S3 Object Lock enforces a Write-Once-Read-Many (WORM) model, preventing objects from being deleted or overwritten for a fixed amount of time or indefinitely."
    },
    {
        "q": "If an Amazon SageMaker training job encounters an OutOfMemory (OOM) error on a GPU, what is the most immediate logical adjustment to the hyperparameters?",
        "options": ["(A) Increase the learning rate", "(B) Decrease the batch size", "(C) Change the activation function", "(D) Add more layers to the network"],
        "ans": "B",
        "exp": "Decreasing the batch size reduces the number of samples processed simultaneously, which directly reduces the memory footprint required on the GPU."
    },
    {
        "q": "Which service acts as a low-latency, scalable Graph database designed to find complex relationships in data, such as fraud rings?",
        "options": ["(A) Amazon Neptune", "(B) Amazon DocumentDB", "(C) Amazon Timestream", "(D) Amazon Aurora"],
        "ans": "A",
        "exp": "Amazon Neptune is a fully managed, high-performance graph database optimized for storing trillions of relationships and querying them with millisecond latency."
    },
    {
        "q": "What is the key advantage of using Amazon SageMaker Studio?",
        "options": ["(A) It provides a single, web-based visual interface for all ML steps from data prep to deployment", "(B) It eliminates the need to know Python", "(C) It offers free GPU access indefinitely", "(D) It hosts the AWS documentation"],
        "ans": "A",
        "exp": "SageMaker Studio is a fully integrated development environment (IDE) for ML, unifying notebooks, debugging, tracking, monitoring, and pipelines into one visual interface."
    },
    {
        "q": "In a neural network, what is the function of the Softmax layer?",
        "options": ["(A) To introduce non-linearity locally", "(B) To compress images", "(C) To convert a vector of raw scores (logits) into a calibrated probability distribution", "(D) To calculate the gradient of the loss"],
        "ans": "C",
        "exp": "Softmax normalizes the output of a network into a probability distribution over predicted output classes, where all values sum to 1."
    },
    {
        "q": "Which distributed file system is optimized specifically to deliver sub-millisecond latencies and massive throughput to EC2 instances for deep learning training?",
        "options": ["(A) Amazon S3", "(B) Amazon FSx for Lustre", "(C) Amazon EFS", "(D) Amazon EBS"],
        "ans": "B",
        "exp": "FSx for Lustre is a high-performance file system integrated with S3, designed for compute-intensive workloads like fast ML training."
    },
    {
        "q": "You are querying data from an on-premises database securely into SageMaker using a VPC. What must be established between your local network and the AWS VPC?",
        "options": ["(A) An internet gateway", "(B) A NAT Gateway", "(C) An AWS Site-to-Site VPN or AWS Direct Connect", "(D) An S3 bucket"],
        "ans": "C",
        "exp": "Site-to-Site VPN or Direct Connect establishes a secure, private tunnel from on-premises networks directly into a VPC."
    },
    {
        "q": "If you need a GenAI application to strictly conform to corporate guidelines and avoid toxic language, what Amazon Bedrock feature should you configure?",
        "options": ["(A) Agents", "(B) Knowledge Bases", "(C) Guardrails for Amazon Bedrock", "(D) Model Evaluation"],
        "ans": "C",
        "exp": "Guardrails allow you to define content filters, redact PII, and block specific toxic or off-topic prompts and responses based on your organization's policies."
    },
    {
        "q": "Which AWS tool enables you to track the exact lineage of an ML model, linking the deployed endpoint back to the training data, code, and hyperparameters?",
        "options": ["(A) AWS CloudFormation", "(B) SageMaker ML Lineage Tracking", "(C) AWS X-Ray", "(D) Amazon Inspector"],
        "ans": "B",
        "exp": "SageMaker ML Lineage Tracking creates and stores information about the steps of an ML workflow, helping with governance, auditing, and root-cause analysis."
    },
    {
        "q": "What is the fundamental difference between Artificial Intelligence (AI) and Machine Learning (ML)?",
        "options": ["(A) ML is the broader concept; AI is a subset of ML", "(B) AI implies machines perform tasks like human logic; ML is a subset defining how machines learn from data to improve", "(C) AI always requires neural networks, ML uses decision trees", "(D) They are synonymous marketing terms"],
        "ans": "B",
        "exp": "AI is the broad science of mimicking human abilities. ML is a specific subset of AI where systems learn patterns directly from data without explicit programming."
    }
]

import os, random

# Generate sets for AWS ML
def generate_sets():
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
            <div class="q-line">Q{q_num}. {question_text} {options_text}</div>
            <div class="a-line">Answer: {ans} - Explanation: {exp}</div>
            <div class="score-controls">
                <button class="score-btn correct" data-correct="true" data-qindex="{q_num}">Correct</button>
                <button class="score-btn incorrect" data-correct="false" data-qindex="{q_num}">Incorrect</button>
            </div>
        </div>"""

    for i in range(1, 6):
        start_q = 1
        end_q = 50
        questions_html = ""
        
        # Shuffle for variation
        shuffled_q = list(aws_ml_questions)
        random.shuffle(shuffled_q)
        
        for idx, q in enumerate(shuffled_q):
            q_num = idx + 1
            options_text = " ".join(q["options"])
            questions_html += question_template.format(
                q_num=q_num,
                question_text=q["q"],
                options_text=options_text,
                ans=q["ans"],
                exp=q["exp"]
            ) + "\n"

        file_content = content_template.format(set_num=i, start_q=start_q, end_q=end_q, questions_html=questions_html)

        with open(f"d:/Code/exam-preparations/exams/aws-ml/set{i}.html", "w", encoding="utf-8") as f:
            f.write(file_content)

    print("Successfully generated 5 high-quality AWS ML exam sets.")

if __name__ == "__main__":
    generate_sets()
