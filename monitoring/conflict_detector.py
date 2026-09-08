def detect_conflict(logs):
    positive_words = [
        "correct","accurate","good"
    ]

    negative_words = [
        "wrong","incorrect","bad"

    ]

    conflicts = []
    for log in logs:
        message = (
            log["message"].lower()

        )

        has_positive = any(
            word in message for word in positive_words
        )

        has_negative = any(
            word in message for word in negative_words
        )

        if has_positive and has_negative:
            conflicts.append(log)

        return {
            "conflict_detected": (
            len(conflicts) > 0
        ),
        "conflicts": conflicts
        }    
