# LLM Evaluation & Web Automation Sandbox Pipeline

An end-to-end Python-based testing pipeline that combines browser automation, chatbot response evaluation, REST API testing, and database validation. The project demonstrates how AI-powered customer support systems can be tested using automated evaluation metrics and structured test cases.

## Core Features

- **Web Automation:** Uses Playwright to retrieve company policy information from a local knowledge base.
- **Knowledge Base Integration:** Uses retrieved company policies as contextual information for customer support responses.
- **Chatbot Pipeline:** Processes customer queries and generates responses based on available support policies.
- **LLM Evaluation:** Integrates DeepEval to evaluate chatbot response quality using structured evaluation metrics.
- **Answer Relevancy:** Measures how relevant the chatbot's response is to the customer's original query.
- **Hallucination Detection:** Checks whether chatbot responses contain information unsupported by the retrieved context.
- **REST API:** Provides chatbot functionality through FastAPI endpoints.
- **Database Integration:** Uses SQLite to store and retrieve chatbot conversation history.
- **Automated Testing:** Uses pytest to validate API endpoints, database operations, and chatbot pipeline behaviour.
- **CI/CD:** Uses GitHub Actions to automate test execution during repository updates.

## Tech Stack

| Category | Technologies |
|---|---|
| Programming Language | Python |
| Web Automation | Playwright |
| AI Evaluation | DeepEval |
| Evaluation Metrics | AnswerRelevancyMetric, HallucinationMetric |
| API Framework | FastAPI |
| API Documentation | Swagger UI / OpenAPI |
| Database | SQLite |
| Testing Framework | Pytest |
| Evaluation Backend | Google Gemini API (when configured as the evaluation model) |
| Version Control | Git, GitHub |
| CI/CD | GitHub Actions |

## Evaluation Workflow

1. Retrieve company policies from the knowledge base using Playwright.
2. Receive a customer complaint or support query.
3. Process the query through the chatbot application pipeline.
4. Generate a response using the available support policies.
5. Construct a DeepEval `LLMTestCase` containing the input, actual output, and retrieval context.
6. Evaluate the response using Answer Relevancy and Hallucination metrics.
7. Compare evaluation results against configured metric thresholds.

## API Endpoints

The application exposes chatbot functionality through FastAPI.

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Checks API availability |
| POST | `/chat` | Submits a customer query and receives a chatbot response |

Interactive API documentation is available through Swagger UI at:

`http://127.0.0.1:8000/docs`

## Database Integration

The project uses SQLite to maintain chatbot conversation history.

Stored information includes:

- User messages
- Corresponding chatbot responses
- Conversation records for retrieval and validation

## Automated Testing

The project uses pytest to validate different components.

Current test coverage includes:

- Chatbot response and pipeline behaviour
- REST API endpoint validation
- Invalid request handling
- Database table creation and conversation storage
- Database retrieval operations

**Latest test result: 14 tests passed.**

## Evaluation Metrics

| Metric | Threshold | Purpose |
|---|---:|---|
| Answer Relevancy | 0.70 | Measures how relevant the response is to the user's query |
| Hallucination | 0.50 | Evaluates unsupported claims against the retrieved context |

*Actual evaluation scores depend on the chatbot output, evaluation model, and configured metric thresholds.*

## Project Structure

```text
llm-automation-eval/
│
├── app_pipeline.py
├── api.py
├── database.py
├── knowledge_base.html
├── test_chatbot.py
│
├── tests/
│   ├── test_api.py
│   ├── test_database.py
│   └── test_pipeline.py
│
├── README.md
├── requirements.txt
└── .gitignore
```

## Future Enhancements

- Postman-based REST API testing and collection automation.
- Advanced testing of non-deterministic LLM responses.
- Expanded Python OOP-based reusable testing architecture.
- Android mobile automation using Appium.
- Cloud-based testing and deployment using AWS services.
