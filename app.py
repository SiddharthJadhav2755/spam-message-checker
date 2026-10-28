"""
Spam Message Checker - Streamlit Application
A beginner-friendly, lightweight web application for detecting potential spam messages.
Author: College Project / Educational Demo
Technologies: Python, Streamlit
"""

import re
import streamlit as st


# ==============================================================================
# 1. SPAM DETECTION ENGINE (Rule-Based Heuristic Logic)
# ==============================================================================

def analyze_message(message: str) -> dict:
    """
    Analyzes an input string against established heuristic spam patterns.

    Args:
        message (str): Text message provided by the user.

    Returns:
        dict: A dictionary containing:
            - is_empty (bool): True if message is blank/whitespace.
            - is_spam (bool): True if any spam indicator is triggered.
            - reasons (list): Specific descriptions of triggered rules.
            - score (int): Total number of indicator categories triggered.
    """
    cleaned = message.strip()
    if not cleaned:
        return {
            "is_empty": True,
            "is_spam": False,
            "reasons": [],
            "score": 0
        }

    reasons = []
    lower_msg = cleaned.lower()

    # Rule 1: Prize, Lottery, & Reward Bait
    prize_keywords = [
        "winner", "you have won", "you won", "claim your prize", "claim prize",
        "claim now", "jackpot", "lottery", "gift card", "selected for a reward",
        "free prize", "congratulations"
    ]
    matched_prizes = [kw for kw in prize_keywords if kw in lower_msg]
    if matched_prizes:
        formatted = ", ".join(f"'{k}'" for k in matched_prizes)
        reasons.append(f"Prize / lottery claims detected: {formatted}")

    # Rule 2: Financial Bait & Get-Rich-Quick Claims
    financial_keywords = [
        "free money", "instant cash", "make money fast", "double your income",
        "cash bonus", "crypto giveaway", "no fees", "risk-free", "earn $"
    ]
    matched_fin = [kw for kw in financial_keywords if kw in lower_msg]
    if matched_fin:
        formatted = ", ".join(f"'{k}'" for k in matched_fin)
        reasons.append(f"Financial bait keywords detected: {formatted}")

    # Rule 3: Artificial Urgency & High-Pressure Marketing
    urgency_keywords = [
        "limited offer", "limited time", "act now", "urgent action",
        "urgent:", "expires today", "exclusive deal", "call immediately"
    ]
    matched_urgency = [kw for kw in urgency_keywords if kw in lower_msg]
    if matched_urgency:
        formatted = ", ".join(f"'{k}'" for k in matched_urgency)
        reasons.append(f"Urgency / promotional pressure detected: {formatted}")

    # Rule 4: Credential Phishing & Sensitive Information Requests
    phishing_keywords = [
        "otp", "one time password", "password", "cvv", "pin",
        "bank account", "credit card", "debit card", "verify your account",
        "update your payment", "account suspended", "security alert",
        "confirm your identity"
    ]
    matched_phish = []
    for kw in phishing_keywords:
        # Require word boundaries for short terms like 'otp' or 'pin'
        if len(kw) <= 4:
            if re.search(r"\b" + re.escape(kw) + r"\b", lower_msg):
                matched_phish.append(kw)
        else:
            if kw in lower_msg:
                matched_phish.append(kw)
    if matched_phish:
        formatted = ", ".join(f"'{k}'" for k in matched_phish)
        reasons.append(f"Sensitive credential / phishing keywords detected: {formatted}")

    # Rule 5: Suspicious Links / URLs
    url_pattern = r"https?://[^\s]+|www\.[^\s]+"
    urls = re.findall(url_pattern, cleaned)
    if urls:
        formatted = ", ".join(f"'{u}'" for u in urls)
        reasons.append(f"Suspicious web link(s) detected: {formatted}")

    # Rule 6: Formatting Anomalies (Excessive Punctuation & ALL CAPS)
    if re.search(r"!{2,}", cleaned):
        reasons.append("Excessive exclamation marks ('!!' or more)")
    if re.search(r"\${2,}", cleaned):
        reasons.append("Excessive currency symbols ('$$' or more)")

    letters = [c for c in cleaned if c.isalpha()]
    if len(letters) >= 12:
        caps_ratio = sum(1 for c in letters if c.isupper()) / len(letters)
        if caps_ratio > 0.6:
            reasons.append(f"Abnormally high uppercase ratio ({caps_ratio * 100:.0f}% ALL CAPS)")

    is_spam = len(reasons) > 0
    return {
        "is_empty": False,
        "is_spam": is_spam,
        "reasons": reasons,
        "score": len(reasons)
    }


# ==============================================================================
# 2. STREAMLIT USER INTERFACE
# ==============================================================================

def main():
    # Page configuration
    st.set_page_config(
        page_title="Spam Message Checker",
        page_icon="🛡️",
        layout="centered"
    )

    # 1. Project Title and 2. Short Description
    st.title("🛡️ Spam Message Checker")
    st.write(
        "A lightweight, rule-based web application to check whether a text message, "
        "SMS, or email snippet is **likely spam** or **likely not spam**."
    )

    st.markdown("---")

    # Session State Initialization for Input Text Area
    if "user_text" not in st.session_state:
        st.session_state.user_text = ""

    # Callback helper to clear the input
    def clear_text():
        st.session_state.user_text = ""

    # Optional quick sample buttons to assist evaluation
    st.caption("💡 Quick Test Pre-fills:")
    col_demo1, col_demo2, col_demo3 = st.columns(3)
    with col_demo1:
        if st.button("Sample: Normal Message"):
            st.session_state.user_text = (
                "Hey Rahul, are we still meeting for lunch tomorrow at 1 PM? Let me know."
            )
    with col_demo2:
        if st.button("Sample: Phishing Spam"):
            st.session_state.user_text = (
                "URGENT: Your bank account is locked! Verify your OTP immediately at http://bit.ly/secure-login-392"
            )
    with col_demo3:
        if st.button("Sample: Prize Spam"):
            st.session_state.user_text = (
                "Congratulations! You are the lucky winner of a $1000 gift card! Claim your prize now! Limited offer."
            )

    # 3. Multiline text box where users can enter a message
    user_input = st.text_area(
        label="Enter your message below:",
        key="user_text",
        height=150,
        placeholder="Type or paste any SMS, email subject, or promotional message here..."
    )

    # 4. Check Message button & 8. Clear button
    col_btn1, col_btn2 = st.columns([1, 1])
    with col_btn1:
        check_clicked = st.button("🔍 Check Message", type="primary", use_container_width=True)
    with col_btn2:
        st.button("🗑️ Clear Input", on_click=clear_text, use_container_width=True)

    # 5. Output section displaying prediction
    if check_clicked:
        # 7. Warning if user submits an empty message
        if not user_input.strip():
            st.warning("⚠️ Warning: Please enter a message before clicking 'Check Message'.")
        else:
            result = analyze_message(user_input)

            st.markdown("### Prediction Result")

            # 6. Clear visual distinction between spam and non-spam results
            if result["is_spam"]:
                st.error("🚨 **Likely Spam**: The message contains suspicious indicators.")
                st.markdown(
                    f"**Risk Level:** Elevated (Triggered **{result['score']}** heuristic flag(s))"
                )
                with st.expander("🔎 View Detected Red Flags", expanded=True):
                    for reason in result["reasons"]:
                        st.markdown(f"- 🚩 {reason}")
            else:
                st.success("✅ **Likely Not Spam**: No configured spam indicators were detected.")
                st.info("The message does not match known spam phrases, phishing keywords, or suspicious links.")

    # Educational Disclaimer Notice
    st.markdown("---")
    st.caption(
        "ℹ️ **Educational Demonstration Notice:** This application uses rule-based heuristic "
        "matching for educational purposes and cloud computing coursework demonstration. "
        "It is not a replacement for production-grade machine learning spam filters or security gateways."
    )


if __name__ == "__main__":
    main()

