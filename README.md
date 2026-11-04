# LLM Evaluation & Web Automation Sandbox Pipeline

An end-to-end automated testing pipeline designed to evaluate non-deterministic AI chatbot responses against structured company knowledge and contextual evaluation metrics.

## Core Features

- **Web Scraping Simulation:** Simulates asynchronous browser-based data extraction using Playwright automation structures.
- **Knowledge Base Integration:** Retrieves company policies and contextual information to generate accurate customer support responses.
- **LLM Evaluation Framework:** Uses the official **DeepEval framework** to evaluate chatbot response quality.
- **Answer Relevancy:** Measures how accurately the chatbot response addresses the customer's query.
- **Hallucination Detection:** Identifies unsupported or fabricated information by comparing chatbot responses against the retrieved context.
- **Automated Test Execution:** Uses DeepEval's `LLMTestCase` and `evaluate()` functions to execute evaluation metrics against chatbot responses.

## Tech Stack

- **Language:** Python
- **Web Automation:** Playwright
- **Chatbot Pipeline:** Custom Python application pipeline
- **Evaluation Framework:** DeepEval
- **Evaluation Metrics:** AnswerRelevancyMetric, HallucinationMetric
- **LLM Evaluation Backend:** Google Gemini API
- **Data Handling:** JSON

## Evaluation Workflow

1. Fetch company policies from the knowledge base.
2. Submit a customer complaint to the chatbot.
3. Generate a chatbot response using the application pipeline.
4. Construct a DeepEval `LLMTestCase` containing the input, actual output, and retrieval context.
5. Execute Answer Relevancy and Hallucination metrics.
6. Generate evaluation results based on the configured metric thresholds.

## Evaluation Report

The evaluation pipeline assesses chatbot responses using two primary metrics:

| Metric | Threshold | Purpose |
|---|---:|---|
| Answer Relevancy | 0.70 | Measures response relevance |
| Hallucination | 0.50 | Measures factual consistency with retrieved context |

*Note: Actual scores and evaluation results depend on the LLM judge and the chatbot response. No fixed evaluation scores are assumed.*

---
