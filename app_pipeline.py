
def fetch_knowledge_base():
    """
    Simulates retrieving company delivery and refund policies.
    """
    print("[Knowledge Base] Loading BiteSpeed delivery policies...")

    app_heading = "BiteSpeed Support Center - Delivery Policy"

    app_faq = (
        "Orders delayed by more than 45 minutes or items marked as "
        "missing are eligible for a full refund or a replacement voucher "
        "within 2 hours of delivery."
    )

    return f"Source Documentation: {app_heading}. Guidelines: {app_faq}"


def query_support_bot(user_question: str, context: str) -> str:
    """
    Generates a customer support response using the retrieved context.
    """

    user_query_lower = user_question.lower()

    if any(word in user_query_lower for word in ["late", "delay", "refund"]):
        return (
            "Your order is eligible for a full refund or a replacement "
            "voucher if the delay exceeds 45 minutes. Our policy allows "
            "this within 2 hours of delivery."
        )

    if any(word in user_query_lower for word in ["missing", "not received"]):
        return (
            "If an item is missing from your order, you are eligible "
            "for a full refund or a replacement voucher within 2 hours "
            "of delivery."
        )

    return (
        "I'm unable to determine the applicable policy. "
        "Let me connect you with a customer support representative."
    )
