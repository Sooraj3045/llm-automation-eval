# LLM Evaluation & Web Automation Sandbox Pipeline

An end-to-end automated testing pipeline built to evaluate non-deterministic AI chatbot responses against structured context metrics.

##  Core Features
- **Scraping Simulation**: Models asynchronous browser data extraction using Playwright structures.
- **Resilient Fallback Engine**: Implements network exception containment layers to secure pipeline execution continuity under high latency or offline status.
- **LLM Evaluation Metrics**: Validates AI outputs using custom evaluation loops tracking **Answer Relevancy** and **Hallucination Engine** scoring matrices.

##  Tech Stack
- **Language**: Python (OOP architecture)
- **Testing Framework Foundations**: Playwright UI automation structures
- **Evaluation Judge**: Google Gemini Flash Engine integration API structures

##  Evaluation Report Output
```json
{
    "answer_relevancy": {
        "score": 0.95,
        "reason": "The support bot correctly accurately identified the 45-minute delay rule from the company policy."
    },
    "hallucination": {
        "score": 0.00,
        "reason": "No hallucinations found. The bot parameters strictly align with the scraped refund terms."
    }
}
```

---

