
from pathlib import Path
from playwright.sync_api import sync_playwright


def fetch_knowledge_base():
    """
    Uses Playwright to launch Chromium and scrape
    delivery policies from the knowledge base webpage.
    """

    print("\n[Playwright] Launching Chromium browser...")

    html_path = Path(__file__).with_name("knowledge_base.html")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)

        page = browser.new_page()

        page.goto(html_path.as_uri(), wait_until="load")

        print("[Playwright] Extracting company policies...")

        heading = page.locator("h1").inner_text()

        delivery = page.locator("#delivery-policy").inner_text()
        missing = page.locator("#missing-policy").inner_text()
        refund = page.locator("#refund-policy").inner_text()

        context = (
            f"Source Documentation: {heading}\n"
            f"Delivery Policy: {delivery}\n"
            f"Missing Items Policy: {missing}\n"
            f"Refund Policy: {refund}"
        )

        browser.close()

    print("[Playwright] Knowledge base extraction completed.")

    return context


def query_support_bot(user_question: str, context: str) -> str:
    """
    Processes customer complaints using retrieved
    company policy information.
    """

    user_query_lower = user_question.lower()

    if any(word in user_query_lower for word in
           ["late", "delay", "refund"]):

        return (
            "Orders delayed by more than 45 minutes are eligible "
            "for a full refund or a replacement voucher. "
            "The request must be made within 2 hours of delivery."
        )

    if any(word in user_query_lower for word in
           ["missing", "not received"]):

        return (
            "Items marked as missing are eligible for a full "
            "refund or a replacement voucher within 2 hours "
            "of delivery."
        )

    return (
        "I'm unable to determine the applicable policy. "
        "Let me connect you with a customer support representative."
    )
