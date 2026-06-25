def classify_ticket(message):
    text = message.lower()

    phishing_keywords = [
        "otp", "pin", "password", "verification code",
        "fraud", "scam", "suspicious call",
        "ওটিপি", "পিন", "পাসওয়ার্ড", "প্রতারণা"
    ]

    wrong_transfer_keywords = [
        "wrong number", "wrong recipient",
        "wrong account", "sent by mistake",
        "ভুল নম্বর", "ভুল একাউন্ট",
        "ভুল অ্যাকাউন্ট", "ভুলে পাঠিয়েছি"
    ]

    payment_failed_keywords = [
        "payment failed",
        "transaction failed",
        "balance deducted",
        "money deducted",
        "failed transaction",
        "পেমেন্ট ব্যর্থ",
        "টাকা কাটা গেছে",
        "লেনদেন ব্যর্থ"
    ]

    refund_keywords = [
        "refund",
        "money back",
        "return payment",
        "reimburse",
        "রিফান্ড",
        "টাকা ফেরত"
    ]

    if any(k in text for k in phishing_keywords):
        return {
            "case_type": "phishing_or_social_engineering",
            "severity": "critical",
            "department": "fraud_risk",
            "agent_summary": "Customer reports a suspected phishing attempt.",
            "human_review_required": True,
            "confidence": 0.95
        }

    if any(k in text for k in wrong_transfer_keywords):
        return {
            "case_type": "wrong_transfer",
            "severity": "high",
            "department": "dispute_resolution",
            "agent_summary": "Customer reports sending money to the wrong recipient.",
            "human_review_required": True,
            "confidence": 0.90
        }

    if any(k in text for k in payment_failed_keywords):
        return {
            "case_type": "payment_failed",
            "severity": "high",
            "department": "payments_ops",
            "agent_summary": "Customer reports a failed payment and possible balance deduction.",
            "human_review_required": True,
            "confidence": 0.88
        }

    if any(k in text for k in refund_keywords):
        return {
            "case_type": "refund_request",
            "severity": "low",
            "department": "customer_support",
            "agent_summary": "Customer is requesting a refund.",
            "human_review_required": False,
            "confidence": 0.85
        }

    return {
        "case_type": "other",
        "severity": "low",
        "department": "customer_support",
        "agent_summary": "Customer reports an issue requiring further investigation.",
        "human_review_required": False,
        "confidence": 0.60
    }