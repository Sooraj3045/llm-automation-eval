
from app_pipeline import fetch_knowledge_base, query_support_bot


def test_playwright_fetches_knowledge_base():
    context = fetch_knowledge_base()

    assert "Delivery Policy" in context
    assert "Missing Items Policy" in context
    assert "Refund Policy" in context


def test_late_order_response():
    context = fetch_knowledge_base()

    response = query_support_bot(
        "My order is late and I want a refund",
        context
    )

    assert "refund" in response.lower()


def test_missing_item_response():
    context = fetch_knowledge_base()

    response = query_support_bot(
        "My item is missing",
        context
    )

    assert "missing" in response.lower()


def test_unknown_query():
    context = fetch_knowledge_base()

    response = query_support_bot(
        "Tell me about your company history",
        context
    )

    assert "unable to determine" in response.lower()
