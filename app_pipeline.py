import os

def fetch_knowledge_base():
    """
    My custom scraping simulation function.
    Instead of hitting a live site and risking timeouts, this simulates pulling
    the latest delivery and refund rules from our internal company database.
    """
    print("[Playwright Hook] Simulating documentation scrape for 'https://bite-speed-delivery.com'...")
    
    # Setting up the company rules for missing or delayed food orders
    app_heading = "BiteSpeed Support Center - Delivery Policy"
    app_faq = "Orders delayed by more than 45 minutes or items marked as missing are eligible for a full refund or a replacement voucher within 2 hours of delivery."
    
    return f"Source Documentation: {app_heading}. Guidelines: {app_faq}"

def query_support_bot(user_question: str, context: str) -> str:
    """
    This models our AI chatbot logic processing a customer complaint.
    It takes the context data from above and attempts to answer the user query.
    """
    user_query_lower = user_question.lower()
    
    # Basic matching logic to generate a response string
    if "late" in user_query_lower or "delay" in user_query_lower or "refund" in user_query_lower:
        return "If your food delivery takes over 45 minutes, our team will process a full refund or send a voucher to your account immediately."
        
    return "I'm having trouble checking that policy. Let me connect you with a live delivery partner manager."
