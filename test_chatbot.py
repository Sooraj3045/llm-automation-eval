import os
from deepeval.test_case import LLMTestCase
# Importing official DeepEval metrics instead of building our own
from deepeval.metrics import AnswerRelevancyMetric, HallucinationMetric
from deepeval import evaluate
from app_pipeline import fetch_knowledge_base, query_support_bot

def run_deepeval_suite():
    print("\n🚀 RUNNING OFFICIAL DEEPEVAL METRIC EVALUATION...")
    
    # 1. Fetch data simulation via our app pipeline 
    company_context = fetch_knowledge_base()
    test_user_complaint = "My dinner order is 50 minutes late, my food is cold, and I want my money back!"
    
    # 2. Get the generated bot response
    bot_response = query_support_bot(test_user_complaint, company_context)
    
    # 3. Pack parameters into DeepEval's formal TestCase structure
    test_case = LLMTestCase(
        input=test_user_complaint,
        actual_output=bot_response,
        retrieval_context=[company_context]
    )
    
    # 4. Initialize DeepEval metrics with strict thresholds
    # We pass async_mode=False to keep execution stable on your Python version
    relevancy_metric = AnswerRelevancyMetric(threshold=0.7, async_mode=False)
    hallucination_metric = HallucinationMetric(threshold=0.5, async_mode=False)
    
    # 5. Execute DeepEval's direct evaluation function
    # This bypasses the broken CLI test runner completely!
    evaluate(
        test_cases=[test_case], 
        metrics=[relevancy_metric, hallucination_metric]
    )

if __name__ == "__main__":
    # Ensure your Gemini API Key is stored safely in your terminal environment before running
    run_deepeval_suite()
