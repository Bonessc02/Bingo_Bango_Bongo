# Sebastian Costa
# February 14, 2026
# Spam Finder for Email_Python Assignment

def get_spam_keywords():
    # Produces a log of commonly found spam words and associated phrases.
    return [
        "gift card", "amazon", "winner", "you have been selected", "congratulations",
        "verify", "account information", "claim now", "claim your", "amazon",
        "click here", "click the button", "limited time", "limited-time", "act now",
        "urgent", "immediately", "final notice", "your account will be", "suspended",
        "avoid termination", "confirm your details", "update your information", "security alert",
        "unusual activity", "prize", "reward", "free", "selected", "expires"
    ]



def analyze_message(message, spam_keywords):
    # Scans the message for spam keywords and spam phrases.
    # Returns spam score, matched words/phrases, and spam likelihood.

    message_lower = message.lower()
    spam_score = 0
    matched_keywords = []

    # Scan message for keywords
    for keyword in spam_keywords:
        keyword_lower = keyword.lower()

        # Count how many times the keyword appears
        occurrences = message_lower.count(keyword_lower)

        if occurrences > 0:
            spam_score += occurrences
            matched_keywords.append(keyword)

    # Determines spam likelihood
    if spam_score == 0:
        likelihood = "Very unlikely to be spam."
    elif spam_score <= 3:
        likelihood = "Low likelihood of spam."
    elif spam_score <= 6:
        likelihood = "Moderate likeliness of spam, proceed with caution..."
    elif spam_score <= 10:
        likelihood = "Very likely spam, ignore or utilize extreme caution!"
    else:
        likelihood = "Extremely likely or certain to be spam!"

    return spam_score, matched_keywords, likelihood


def main():
    spam_keywords = get_spam_keywords()

    print("=== Spam Detector Assistant Program ===")
    user_message = input("Enter your email message to analyze: ")

    score, triggers, likelihood = analyze_message(user_message, spam_keywords)

    print("=== Spam Likelihood Results ===")
    print(f"Spam Score: {score}")
    print(f"Spam Likelihood: {likelihood}")

    if triggers:
        print("Spam words or phrases detected via program:")
        for word in triggers:
            print(f"- {word}")
    else:
        print("No spam words or phrases detected.")


if __name__ == "__main__":
    main()
