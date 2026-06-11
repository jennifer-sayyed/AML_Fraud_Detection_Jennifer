import re


def detect_pii(text):

    patterns = [

        r"\d{12}",

        r"\d{10}",

        r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"
    ]

    for pattern in patterns:

        if re.search(pattern, text):

            return True

    return False


def detect_prompt_injection(text):

    keywords = [

        "ignore previous instructions",

        "reveal prompt",

        "show system prompt"
    ]

    text = text.lower()

    return any(
        word in text
        for word in keywords
    )


def detect_off_topic(text):

    banking_words = [

        "aml",

        "fraud",

        "bank",

        "transaction",

        "sar",

        "sanction",

        "kyc"
    ]

    text = text.lower()

    return not any(
        word in text
        for word in banking_words
    )