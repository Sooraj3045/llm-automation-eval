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

### Step 2: Push it Live using the VS Code Interface
We can skip the terminal completely here!

1. Click on the **Source Control** icon on the far left bar of VS Code (it looks like a branch with three circles).
2. You will see a blue button that says **"Initialize Repository"**. Click it!
3. In the message box that appears at the top of that side panel, type a simple note like: `Initial commit: Food-delivery LLM sandbox pipeline`
4. Click the blue **Commit** button right above or below the text box.
5. Once committed, the button will turn into a blue **Publish Branch** button. Click it!
6. VS Code will pop open a tiny dropdown at the top of your screen asking you to select a visibility option. Select **"Publish to GitHub public repository"**.
7. If prompted, click **Allow** to let VS Code securely connect to your GitHub profile. 

VS Code will automatically build the repository online, hook up the code files, block the messy cache folders (`.deepeval/`, `__pycache__/`) thanks to your `.gitignore`, and make it completely live!

<FollowUp>
Once the "Publishing..." loading bar finishes at the bottom right corner, check your GitHub profile to see your beautiful new repo! Are you ready to dive into the **top interview questions** they will ask you about this code?
</FollowUp>
